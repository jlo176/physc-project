Web VPython 3.2
 
# rod projectile sim
# shows baton flying with COM trail, spins independently
 
scene.background = color.black
scene.camera.pos = vec(8, 5, 20)
scene.camera.axis = vec(0, 0, -20)
g = -9.81; dt = 0.005; t = 0
speed = 12; angle = 50; L = 3; w = 4
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
 
scene.append_to_caption("speed=12 angle=50 w=4 L=3\nyellow = COM path\n")

scene.append_to_caption("\n\nBall 1 mass: ")
m1_slider = slider(min=0.05, max=1.0, value=0.3, step=0.05, bind=update_m1)
m1_text = wtext(text=" 0.30 kg")

scene.append_to_caption("\n\nBall 2 mass: ")
m2_slider = slider(min=0.05, max=1.0, value=0.3, step=0.05, bind=update_m2)
m2_text = wtext(text=" 0.30 kg")

def update_m1(s):
    global m1
    m1 = s.value
    m1_text.text = " {:.2f} kg".format(s.value)

def update_m2(s):
    global m2
    m2 = s.value
    m2_text.text = " {:.2f} kg".format(s.value)

launched = False
launch_btn = button(text = "launch", pos = scene.title_anchor, bind = launch)

def launch():
    global launched
    launched = True

reset_btn = button(bind=reset_action, text="Reset Simulation", pos=scene.title_anchor)

def reset_action(btn):
    global vel, pos, th, t, v, b, launched
    t = 0

    rad = angle * pi / 180
    vel = speed * vec(cos(rad), sin(rad), 0)
    pos = vec(0, 0.01, 0)
    th = 0
    v = True

    ax = vec(cos(th), sin(th), 0)
    rod.pos = pos - (L/2)*ax
    rod.axis = L*ax
    b1.pos = pos - (L/2)*ax
    b1.radius = m1 * 0.8
    b2.pos = pos + (L/2)*ax
    b2.radius = m2 * 0.8
    com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
    b.stop()
    b.clear()
    b = attach_trail(com, color=color.yellow, radius=0.035, retain=500)
    
    launched = False
    
while True:
    rate(1/dt)

    if (not v) or (not launched):
        continue

    vel += vec(0, g, 0) * dt
    pos += vel * dt
    th += w * dt

    ax = vec(cos(th), sin(th), 0)
    rod.pos = pos - (L/2)*ax
    rod.axis = L*ax
    b1.pos = pos - (L/2)*ax
    b2.pos = pos + (L/2)*ax
    com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)

    t += dt

    if pos.y <= 0:
        v = False
        

    if pos.y <= 0:
        v = False
