Web VPython 3.2
 
# rod projectile sim - prototype v1
# shows baton flying with COM trail, spins independently
 
scene.background = color.black
scene.camera.pos = vec(8, 5, 20)
scene.camera.axis = vec(-8, -3, -20)
 
g = -9.81; dt = 0.005; t = 0
speed = 12; angle = 50; L = 3; w = 4  # w = angular velocity
 
rad = angle * pi / 180
vel = speed * vec(cos(rad), sin(rad), 0)
pos = vec(0, 0.01, 0)
th = 0  # rotation angle
 

# baton pieces
ax = vec(cos(th), sin(th), 0)
rod = cylinder(pos=pos - (L/2)*ax, axis=L*ax, radius=0.08, color=color.orange)
b1 = sphere(pos=pos - (L/2)*ax, radius=0.22, color=color.white)
b2 = sphere(pos=pos + (L/2)*ax, radius=0.22, color=color.white)
 
# COM dot + trail
com = sphere(pos=pos, radius=0.10, color=color.yellow, opacity=0.6)
attach_trail(com, color=color.yellow, radius=0.035, retain=500)
 
scene.append_to_caption("speed=12 angle=50 w=4 L=3\nyellow = COM path\n")
 
while True:
    rate(1/dt)
 
    vel += vec(0, g, 0) * dt
    pos += vel * dt
    th += w * dt
 
    ax = vec(cos(th), sin(th), 0)
    rod.pos = pos - (L/2)*ax
    rod.axis = L*ax
    b1.pos = pos - (L/2)*ax
    b2.pos = pos + (L/2)*ax
    com.pos = pos
 
    t += dt
 
    if pos.y <= 0:
        break
 
scene.append_to_caption("landed at x={:.2f} after {:.2f}s".format(pos.x, t))
