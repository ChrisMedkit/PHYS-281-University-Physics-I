from vpython import *
#GlowScript 3.2 VPython

scene.width = 800
scene.height = 600
scene.background = color.gray(0.2)
scene.caption = "<b>Penalty Kickz</b>\n Charge/Shoot [SPACE] \n Reset Camera [R]\n\n" #controls

#reset cam
def reset_camera():
    scene.center = vec(0, 1.5, -10)
    scene.range = 8
    scene.forward = vec(0, 0, -1) 
    scene.up = vec(0, 1, 0)
reset_camera()

# Sliders
scene.append_to_caption("<b>Sliders:</b>\n")
scene.append_to_caption("Wind:   ")
def set_wind(s):
    wt.text = '{:1.2f}'.format(s.value)
wind_slider = slider(min=-10, max=10, value=0, bind=set_wind)
wt = wtext(text='0')
scene.append_to_caption("\nGoalie: ")
def set_gspeed(s):
    gt.text = '{:1.1f}'.format(s.value)
goalie_slider = slider(min=1, max=10, value=3, bind=set_gspeed)
gt = wtext(text='3.0')
scene.append_to_caption("\n\n")

#Grass
ground = box(pos=vec(0, -0.1, -5), size=vec(40, 0.2, 50), color=color.green)
#Goal, size ok?
goal_z = -15
post_w = 10.0
post_h = 3.5
post_L = cylinder(pos=vec(-post_w/2, 0, goal_z), axis=vec(0, post_h, 0), radius=0.15, color=color.white)
post_R = cylinder(pos=vec(post_w/2, 0, goal_z), axis=vec(0, post_h, 0), radius=0.15, color=color.white)
crossbar = cylinder(pos=vec(-post_w/2, post_h, goal_z), axis=vec(post_w, 0, 0), radius=0.15, color=color.white)

#Goalie Class
class Goalie:
    def __init__(self):
        head = sphere(pos=vec(0, 2.5, 0), radius=0.4, color=color.red)
        torso = cylinder(pos=vec(0, 1.0, 0), axis=vec(0, 1.5, 0), radius=0.18, color=color.red)
        arm_L = cylinder(pos=vec(0, 2.2, 0), axis=vec(-1.2, -0.4, 0), radius=0.12, color=color.red)
        arm_R = cylinder(pos=vec(0, 2.2, 0), axis=vec(1.2, -0.4, 0), radius=0.12, color=color.red)
        leg_L = cylinder(pos=vec(0, 1.0, 0), axis=vec(-0.6, -1.0, 0), radius=0.15, color=color.red)
        leg_R = cylinder(pos=vec(0, 1.0, 0), axis=vec(0.6, -1.0, 0), radius=0.15, color=color.red)
        self.parts = compound([head, torso, arm_L, arm_R, leg_L, leg_R])#compound object
        
        #start spot
        self.start_pos = vec(0, 1.3, goal_z + 0.5)
        self.parts.pos = self.start_pos
        
        #mass and vel for rebound calculations
        self.mass = 90.0 
        self.vel = vec(0,0,0)
        self.is_hit = False
        
        #goalie movement logic
    def update(self, time, dt):
        if not self.is_hit:
            g_speed = goalie_slider.value
            
            #goalie movement math
            self.parts.pos.x = 3.2 * sin(time * g_speed)
            self.vel.x = 3.2 * g_speed * cos(time * g_speed) 
            self.vel.z = 0
        else:
            self.parts.pos = self.parts.pos + self.vel * dt #
            self.vel = self.vel * 0.95 

    def reset(self):
        self.parts.pos = self.start_pos
        self.vel = vec(0,0,0)
        self.is_hit = False

my_goalie = Goalie()

#Ball and other variables
ball_start_pos = vec(0, 0.2, -4)
ball = sphere(pos=ball_start_pos, radius=0.22, color=color.white, make_trail=True, trail_type="points", interval=5, retain=50)
ball.m = 0.45 
ball.v = vec(0,0,0)

aim_arrow = arrow(pos=ball.pos, axis=vec(0,0,-2), shaftwidth=0.1, color=color.yellow)

# Game state
score_p1 = 0
score_p2 = 0
current_turn = 1 
target_score = 5 

#scoreboard
turn_label = label(pos=vec(0, 6.0, goal_z), text="PLAYER 1'S TURN", height=30, box=False, color=color.white)
score_label = label(pos=vec(0, 4.5, goal_z), text="P1: 0  |  P2: 0", height=25, box=False, color=color.white)

g = vec(0, -9.8, 0)      
air_drag = 0.2        #packaged coeffiecitentasdasd   

is_flying = False
is_charging = False
current_power = 10
reset_timer = 0
t_game = 0               

#Functions
def reset_round():
    global is_flying, reset_timer, is_charging, current_power, current_turn
    is_flying = False
    is_charging = False
    current_power = 10
    
    ball.pos = ball_start_pos
    ball.v = vec(0,0,0)
    ball.clear_trail()
    
    reset_timer = 0
    my_goalie.reset() 

    if current_turn == 1:
        current_turn = 2
        ball.color = color.orange 
        turn_label.text = "PLAYER 2'S TURN"
        turn_label.color = color.orange
    else:
        current_turn = 1
        ball.color = color.white 
        turn_label.text = "PLAYER 1'S TURN"
        turn_label.color = color.white

    aim_arrow.visible = True
    aim_arrow.pos = ball.pos
    aim_arrow.color = color.yellow 

def check_collision_physics():
    g_pos = my_goalie.parts.pos
    g_size = my_goalie.parts.size
    
    collision = (abs(ball.pos.x - g_pos.x) < (g_size.x/2 + ball.radius) and abs(ball.pos.y - g_pos.y) < (g_size.y/2 + ball.radius) and abs(ball.pos.z - g_pos.z) < (g_size.z/2 + ball.radius))
                 
    if collision and not my_goalie.is_hit:
        my_goalie.is_hit = True
        
        #naming variables for collision equations
        m1 = ball.m
        m2 = my_goalie.mass
        v1 = ball.v.z 
        v2 = my_goalie.vel.z 
        #final velocities of the ball v1 and the goalie v2
        v1_final = ((m1 - m2)/(m1 + m2))*v1 + ((2*m2)/(m1 + m2))*v2
        v2_final = ((2*m1)/(m1 + m2))*v1 + ((m2 - m1)/(m1 + m2))*v2
        ball.v.z = v1_final     
        #applying the velocities
        ball.v.x = ball.v.x * 0.5 
        my_goalie.vel.z = v2_final * 5 
        return True
    return False

def check_goal():
    if (ball.pos.z < goal_z + 0.5 and ball.pos.z > goal_z - 1):
        if abs(ball.pos.x) < post_w/2 and ball.pos.y < post_h:
            return True
    return False

#Game Loop
while True:
    rate(60)
    dt = 1/60
    t_game += dt 
    
    my_goalie.update(t_game, dt)
    
    k = keysdown()
    if 'r' in k: reset_camera()

    if not is_flying:
        if ' ' in k:
            is_charging = True
            if current_power < 40: current_power += 80 * dt 
            aim_arrow.length = current_power * 0.15
            aim_arrow.color = vec(1, 1 - (current_power/40), 0) 
        else:
            if is_charging:
                is_charging = False
                is_flying = True
                aim_arrow.visible = False
                ball.v = aim_arrow.axis.norm() * current_power
            else:
                current_power = 10
                aim_arrow.length = 3
                aim_arrow.color = color.yellow
                angle_x = 1.2 * sin(t_game * 4) 
                aim_dir = vec(sin(angle_x), 0.3, -1).norm()
                aim_arrow.axis = aim_dir * 3
    else:
        F_grav = ball.m * g
        F_drag = -air_drag * ball.v
        F_wind = vec(wind_slider.value, 0, 0)
        F_net = F_grav + F_drag + F_wind
        
        ball.v = ball.v + (F_net / ball.m) * dt
        ball.pos = ball.pos + ball.v * dt
        
        if ball.pos.y < ball.radius:
            ball.pos.y = ball.radius
            ball.v.y = -ball.v.y * 0.7 
            ball.v.x = ball.v.x * 0.98
            ball.v.z = ball.v.z * 0.98
            
        check_collision_physics()
        
        if check_goal():
            if current_turn == 1:
                score_p1 += 1
                turn_label.text = "PLAYER 1 SCORED!"
            else:
                score_p2 += 1
                turn_label.text = "PLAYER 2 SCORED!"
            score_label.text = "P1: " + str(score_p1) + "  |  P2: " + str(score_p2)
            
            game_over = False
            if score_p1 >= target_score and (score_p1 - score_p2) >= 2:
                turn_label.text = "PLAYER 1 WINS!"
                turn_label.color = color.green
                game_over = True
            elif score_p2 >= target_score and (score_p2 - score_p1) >= 2:
                turn_label.text = "PLAYER 2 WINS!"
                turn_label.color = color.green
                game_over = True
                
            if game_over:
                scene.append_to_caption("\n\nGAME OVER! Click above to restart.")
                scene.waitfor('click')
                score_p1 = 0
                score_p2 = 0
                score_label.text = "P1: 0  |  P2: 0"
                
            reset_round()
            
        if ball.pos.z < goal_z - 2 or mag(ball.v) < 0.2 or ball.pos.z > -2:
            reset_timer += dt
            if reset_timer > 1.0: 
                turn_label.text = "MISS!"
                reset_round()