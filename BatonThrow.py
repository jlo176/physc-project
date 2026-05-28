Web VPython 3.2
 
# rod projectile sim
# shows baton flying with COM trail, spins independently
 
scene.background = color.black
scene.camera.pos = vec(8, 5, 20)
scene.camera.axis = vec(0, 0, -20)
g = -9.81; dt = 0.005; t = 0
speed = 12; angle = 45; L = 3; w = 4
m1 = 0.3; m2 = 0.3
 
rad = angle * pi / 180
vel = speed * vec(cos(rad), sin(rad), 0)
pos = vec(0, 0.01, 0)
th = 0 
v = True
 
ax = vec(cos(th), sin(th), 0)
rod = cylinder(pos=pos - (L/2)*ax, axis=L*ax, radius=0.08, color=color.red)
b1 = sphere(pos=pos - (L/2)*ax, radius=0.22, color=color.white)
b2 = sphere(pos=pos + (L/2)*ax, radius=0.22, color=color.white)
 
com = sphere(pos=(b1.pos * m1 + b2.pos * m2) / (m1 + m2), radius=0.10, color=color.yellow, opacity=0.6)
b = attach_trail(com, color=color.yellow, radius=0.035, retain=500)
t_b1 = attach_trail(b1, color=color.yellow, radius=0.035, retain=500)
t_b2 = attach_trail(b2, color=color.yellow, radius=0.035, retain=500)

r1 = m2 * L / (m1 + m2)
r2 = m1 * L / (m1 + m2)
 
scene.append_to_caption("speed=12 angle=50 w=4 L=3\nyellow = COM path\n")

scene.append_to_caption("\n\nBall 1 mass: ")
m1_slider = slider(min=0.05, max=1.0, value=0.3, step=0.05, bind=update_m1)
m1_text = wtext(text=" 0.30 kg")

scene.append_to_caption("\n\nBall 2 mass: ")
m2_slider = slider(min=0.05, max=1.0, value=0.3, step=0.05, bind=update_m2)
m2_text = wtext(text=" 0.30 kg")

scene.append_to_caption("\n\n Starting speed ")
speed_slider = slider(min=1.0, max=20.0, value=10, step=1, bind=update_speed)
speed_text = wtext(text=" 10 m/s")

scene.append_to_caption("\n\n Starting angle ")
angle_slider = slider(min=1.0, max=90.0, value=45, step=1, bind=update_angle)
angle_text = wtext(text=" 45 degrees")

scene.append_to_caption("\n\n Starting axis of orientation ")
th_slider = slider(min=0.0, max=180.0, value=0, step=1, bind=update_th)
th_text = wtext(text=" 0 degrees")


def update_m1(s):
    global m1
    m1 = s.value
    m1_text.text = " {:.2f} kg".format(s.value)

def update_m2(s):
    global m2
    m2 = s.value
    m2_text.text = " {:.2f} kg".format(s.value)
    
def update_speed(s):
    global speed
    speed = s.value
    speed_text.text = " {:.2f} m/s".format(s.value)
    
def update_angle(s):
    global angle
    angle = s.value
    angle_text.text = " {:.2f} degrees".format(s.value)
    
def update_th(s):
    global th
    th = s.value * pi / 180
    th_text.text = " {:.2f} degrees".format(s.value)



running = False
run_btn = button(text = "Run", pos = scene.title_anchor, bind = run)

def run():
    global running, run_btn
    running = not running
    if running: 
        run_btn.text = "Pause"
    else:
        run_btn.text = "Run"

reset_btn = button(bind=reset_action, text="Reset Simulation", pos=scene.title_anchor)

def reset_action(btn):
    global vel, pos, th, t, v, b, t_b1, t_b2, running, run_btn, angle, rad
    t = 0

    rad = angle * pi / 180
    vel = speed * vec(cos(rad), sin(rad), 0)
    pos = vec(0, 0.01, 0)
    v = True

    ax = vec(cos(th), sin(th), 0)
    r1 = m2 * L / (m1 + m2)
    r2 = m1 * L / (m1 + m2)
    b1.pos = pos - r1 * ax
    b1.radius = m1 * 0.8
    b2.pos = pos + r2 * ax
    b2.radius = m2 * 0.8
    rod.pos = b1.pos
    rod.axis = b2.pos - b1.pos
    com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
    b.stop()
    b.clear()
    b = attach_trail(com, color=color.yellow, radius=0.035, retain=500)
    t_b1.stop()
    t_b1.clear()
    t_b1 = attach_trail(b1, color=color.yellow, radius=0.035, retain=500)
    t_b2.stop()
    t_b2.clear()
    t_b2 = attach_trail(b2, color=color.yellow, radius=0.035, retain=500)
    
    running = False
    run_btn.text = "Run"
    
while True:
    rate(1/dt)

    if (not v) or (not running):
        continue

    vel += vec(0, g, 0) * dt
    pos += vel * dt
    th += w * dt

    ax = vec(cos(th), sin(th), 0)
    r1 = m2 * L / (m1 + m2)
    r2 = m1 * L / (m1 + m2)
    b1.pos = pos - r1 * ax
    b2.pos = pos + r2 * ax
    rod.pos = b1.pos
    rod.axis = b2.pos - b1.pos
    com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)

    t += dt

    if pos.y <= 0:
        v = False
        
#def down():
#    global drag
#    print("its not dragging time!")
#    if (mag(velArrow.pos + velArrow.axis - scene.mouse.pos) < slop and launched == False):
#        drag = True
#        print("its dragging time!")
#        
#def move():
#    if drag:
#        velArrow.axis = scene.mouse.pos
#        rodVel = velArrow.axis
#        print(rodVel.x)
#        print(rodVel.y)
#        print("its moving time!")
#        
#def up():
#    global drag
#    drag = False
