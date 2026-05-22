Web VPython 3.2

scene.camera.pos = vec(10, 5, 15)

t = 0
dt = 0.01
g = -9.81
m = 0.1
initPos = vec(0, 0, 0)
rodPos = initPos
initVel = vec(10, 10, 0)
rodVel = initVel
rodAcc = vec(0, g, 0)
len = 3;
baton = cylinder(pos = rodPos, axis = len * norm(rodVel), color=color.red, radius = .5)

while rodPos.y >= 0:
    rate(1 / dt)
    
    rodVel += rodAcc * dt
    rodPos += rodVel * dt
    
    baton.pos = rodPos
    baton.axis = len * norm(rodVel)
    
    t += dt
