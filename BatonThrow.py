Web VPython 3.2
 
# rod projectile sim
# shows baton flying with COM trail, spins independently
 
scene.background = vec(0.53, 0.81, 0.98)
scene.camera.pos = vec(8, 5, 20)
scene.camera.axis = vec(0, 0, -20)

grass = box(
    pos=vec(10, -0.08, 0),
    size=vec(200, 0.16, 60),
    texture=textures.wood,     
    color=vec(0.22, 0.62, 0.18),   
    opacity=1.0
)
 
dirt = box(
    pos=vec(10, -5, 0),
    size=vec(200, 9, 60),
    color=vec(0.38, 0.24, 0.10),
    opacity=1.0
)

g = -9.81; dt = 0.005; t = 0
speed = 12; angle = 45; L = 3; w = 4; I = 0
m1 = 0.3; m2 = 0.3
 
rad = angle * pi / 180
vel = speed * vec(cos(rad), sin(rad), 0)
th = 0 
v = True
 
ax = vec(cos(th), sin(th), 0)
rod = cylinder(pos=-(L/2)*ax, axis=L*ax, radius=0.08, color=color.red)
b1 = sphere(pos=-(L/2)*ax, radius=.5*sqrt(m1), color=color.white)
b2 = sphere(pos=(L/2)*ax, radius=.5*sqrt(m2), color=color.white)
com = sphere(pos=(b1.pos * m1 + b2.pos * m2) / (m1 + m2), radius=0.10, color=color.yellow, opacity=0.6)
pos = vec(0, max(mag(b1.pos - com.pos), mag(b2.pos - com.pos)), 0)
b1.pos += pos
b2.pos += pos
com.pos += pos
rod.pos += pos
b = attach_trail(com, color=color.yellow, radius=0.035, retain=500)
t_b1 = attach_trail(b1, color=color.red, radius=0.035, retain=500)
t_b2 = attach_trail(b2, color=color.red, radius=0.035, retain=500)
b.stop()
t_b1.stop()
t_b2.stop()

r1 = m2 * L / (m1 + m2)
r2 = m1 * L / (m1 + m2)

g1 = graph(xtitle = "time (s)", ytitle = "speed (m/s)", ymax = 0, xmin = 0, ymin = 0)
gc1 = gcurve(color = color.yellow, label = "COM speed")
gc2 = gcurve(color = color.black, label = "Mass 2 speed")
gc3 = gcurve(color = color.red, label = "Mass 1 speed")
gd1 = gdots(color = color.black, radius = 1)

g2 = graph(xtitle = "time (s)", ytitle = "Kinetic Energy (J)", ymax = 0, xmin = 0, ymin = 0)
gc_kr = gcurve(color = color.yellow, label = "K rot")
gc_kt = gcurve(color = color.black, label = "K trans")
gc_ktot = gcurve(color = color.red, label = "K total")
gc_ktot_split = gcurve(color = color.red)
gd2 = gdots(color = color.black, radius = 1)

started = False

# New split code variables
split_both = False
v1 = vec(0,0,0)
v2 = vec(0,0,0)
stop1 = False
stop2 = False

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

scene.append_to_caption("\n\n Starting angular speed ")
w_slider = slider(min=1.0, max=20.0, value=3, step=.5, bind=update_angular_speed)
w_text = wtext(text=" 3.0 rad/s")

scene.append_to_caption("\n\n Starting axis of orientation ")
th_slider = slider(min=0.0, max=180.0, value=0, step=1, bind=update_th)
th_text = wtext(text=" 0 degrees")

scene.append_to_caption("\n\n Rod Length ")
L_slider = slider(min=0.0, max=10.0, value=3.0, step=1, bind=update_length)
L_text = wtext(text=" 3 m")

scene.append_to_caption("\n\n Starting impulse ")
I_slider = slider(min=0.0, max=20.0, value=0, step=1, bind=update_impulse)
I_text = wtext(text=" 0 N*s")

all_sliders = [m1_slider, m2_slider, speed_slider, angle_slider, w_slider, th_slider, L_slider, I_slider]

def disable_sliders():
    for s in all_sliders:
        s.disabled = True

def enable_sliders():
    for s in all_sliders:
        s.disabled = False

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
    speed_text.text = " {:d} m/s".format(s.value)
    
def update_angle(s):
    global angle
    angle = s.value
    angle_text.text = " {:d} degrees".format(s.value)
    
def update_angular_speed(s):
    global w
    w = s.value
    w_text.text = " {:.1f} rad/s".format(s.value)
    
def update_th(s):
    global th
    th = s.value * pi / 180
    th_text.text = " {:d} degrees".format(s.value)
    
def update_length(s):
    global L
    L = s.value
    L_text.text = " {:d} m".format(s.value)
    

def update_impulse(s):
    global I
    I = s.value
    I_text.text = " {:.2f} N*s".format(s.value)

running = False
run_btn = button(text = "Run", pos = scene.title_anchor, bind = run)

def run(btn):
    global running, run_btn, started, b, t_b1, t_b2
    running = not running
    if not started:
        b.start()
        t_b1.start()
        t_b2.start()
        started = True
    if running: 
        run_btn.text = "Pause"
        disable_sliders()
    else:
        run_btn.text = "Run"

reset_btn = button(bind=reset_action, text="Reset Simulation", pos=scene.title_anchor)
split_btn = button(bind=split_rod, text="Split Rod", pos=scene.title_anchor)

scene.bind('click', split_rod)

def clear(graph):
    graph.clear()

def reset_action(btn):
    global vel, g2, pos, th, L, t, v, b, t_b1, t_b2, running, run_btn, split_btn, angle, rad, th_slider, split_both, v1, v2, stop1, stop2, started
    t = 0

    rad = angle * pi / 180
    vel = speed * vec(cos(rad), sin(rad), 0)
    th = th_slider.value * pi / 180    
    v = True

    ax = vec(cos(th), sin(th), 0)
    rod.pos = -(L/2)*ax
    rod.axis = L * ax
    b1.pos = -(L/2)*ax
    b2.pos = (L/2)*ax
    com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
    pos = vec(0, max(mag(b1.pos - com.pos), mag(b2.pos - com.pos)), 0)
    b1.pos += pos
    b2.pos += pos
    com.pos += pos
    rod.pos += pos  
    b.stop()
    b.clear()
    b = attach_trail(com, color=color.yellow, radius=0.035, retain=500)
    b.stop()
    t_b1.stop()
    t_b1.clear()
    t_b1 = attach_trail(b1, color=color.red, radius=0.035, retain=500)
    t_b1.stop()
    t_b2.stop()
    t_b2.clear()
    t_b2 = attach_trail(b2, color=color.red, radius=0.035, retain=500)
    t_b2.stop()
    
    running = False
    run_btn.text = "Run"
    
    split_both = False
    v1 = vec(0,0,0)
    v2 = vec(0,0,0)
    rod.visible = True
    com.visible = True
    split_btn.disabled = False
    split_btn.text = "Split Rod"
    stop1 = False
    stop2 = False
    
    started = False
    enable_sliders()
    
    #reset graphs
    gd2.data = []
    gc_kr.data = []
    gc_kt.data = []
    gc_ktot.data = []
    gc_ktot_split.data = []
    g2.ymax = None
    clear(g2)
    
    gd1.data = []
    gc1.data = []
    gc2.data = []
    gc3.data = []
    g1.ymax = None
    g1.select()
    clear(g1)
    
def split_rod(btn):
    global rod, b1, b2, t_b1, t_b2, t, v, v1, v2, split_both, started
    
    if not v or not started or split_both:
        return
    
    
    #Calculations
    tang = vec(-sin(th), cos(th), 0)
    r1 = m2 * L / (m1 + m2) 
    r2 = m1 * L / (m1 + m2)
    
    v1 = vel + (-w * r1) * tang - (I / m1) * ax
    v2 = vel + (w * r2) * tang + (I / m2) * ax
    
    #Rod trail
    rod.visible = False
    b.stop(); b.clear()
    com.visible = False
    
    #New ball trails
    t_b1.stop(); t_b1.clear()
    t_b2.stop(); t_b2.clear()
    t_b1 = attach_trail(b1, color=color.cyan,   radius=0.04, retain=500)
    t_b2 = attach_trail(b2, color=color.magenta, radius=0.04, retain=500)
    
    #Variable update
    split_both = True
    split_btn.disabled = True
    split_btn.text = "Rod split"
    
    #split graph indicator
    g1.select()
    i = 0
    while i < 2000:
        gd1.plot(t, i)
        i += 1
        
    g2.select()
    i = 0
    while i < 2000:
        gd2.plot(t, i)
        i += 2

    
while True:
    rate(1/dt)
    
    if not started:
        ax = vec(cos(th), sin(th), 0)
        r1 = m2 * L / (m1 + m2)
        r2 = m1 * L / (m1 + m2)
        b1.pos = pos - r1 * ax
        b2.pos = pos + r2 * ax
        b1.radius = .5 * sqrt(m1)
        b2.radius = .5 * sqrt(m2)
        rod.pos  = b1.pos
        rod.axis = b2.pos - b1.pos
        com.pos  = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
        pos = vec(0, max(mag(b1.pos - com.pos), mag(b2.pos - com.pos)), 0)
        continue

    if (not v) or (not running):
        continue

    if split_both:
        if not stop1:
            v1 += vec(0, g, 0) * dt
            b1.pos += v1 * dt
            g1.select()
            gc3.plot(t, mag(v1))
            g1.ymax = max(mag(v1), g1.ymax)
            if b1.pos.y <= 0:
                stop1 = True
        if not stop2:
            v2 += vec(0, g, 0) * dt
            b2.pos += v2 * dt
            g1.select()
            gc2.plot(t, mag(v2))
            g1.ymax = max(mag(v2), g1.ymax)
            if b2.pos.y <= 0:
                stop2 = True
        if not stop1 and not stop2:
            vel = ((b1.pos * m1 + b2.pos * m2) / (m1 + m2) - com.pos) / dt
            com.pos = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
            g1.select()
            gc1.plot(t, mag(vel))
            g2.select()
            K = .5 * (m1 * mag(v1) ** 2 + m2 * mag(v2) ** 2)
            gc_ktot_split.plot(t, K)
            g2.ymax = max(g2.ymax, K + 10)
        t += dt
        if stop1 and stop2:
            v = False
    else:
        vel += vec(0, g, 0) * dt
        pos += vel * dt
        th  += w * dt
        
        ax = vec(cos(th), sin(th), 0)
        b1.pos = pos - r1 * ax
        b2.pos = pos + r2 * ax
        rod.pos  = b1.pos
        rod.axis = b2.pos - b1.pos
        com.pos  = (b1.pos * m1 + b2.pos * m2) / (m1 + m2)
        
        g1.select()
        gc1.plot(t, mag(vel))
        tang = vec(-sin(th), cos(th), 0)
        gc2.plot(t, mag(vel + (w * r2) * tang)) 
        gc3.plot(t, mag(vel + (-w * r1) * tang))
        g1.ymax = max(max(mag(vel + (w * r2) * tang), mag(vel + (-w * r1) * tang)) + 3, g1.ymax)
        
        g2.select()
        kr = .5 * m1 * r1 + m2 * r2 * w * w
        gc_kr.plot(t, kr)
        kt = .5 * (m1 * (mag(vel + (-w * r1) * tang) ** 2) + m2 * (mag(vel + (w * r2) * tang) ** 2))
        gc_ktot.plot(t, kr + kt)
        g2.ymax = max(g2.ymax, kr + kt + 10)
        
        t += dt

        if pos.y <= 0 or b1.pos.y <= 0 or b2.pos.y <= 0:
            v = False
