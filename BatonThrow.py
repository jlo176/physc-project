Web VPython 3.2

t = 0.00
dt = 0.01
m = 0.0088
g = -9.81
vy = 0
y_init = 5
yy = y_init
ball = cylinder(pos=vector(0, y_init, 0), radius = 0.5, color=color.red)
x_init = 0
xx = x_init
vx = 5

scene.camera.pos = vector(0, y_init/2, 10)

while yy > 0:
    rate(1/dt)
    fy = m*g 
    ay = fy / m
    vy = vy + ay*dt
    yy = yy + vy*dt
    xx = xx + vx*dt

    ball.pos = vector(xx, yy, 0)

    t = t + dt


    
    
