Web VPython 3.2

scene.camera.pos = vec(10, 5, 15)

t = 0
dt = 0.01
g = -9.81
m = 0.1
initPos = vec(0, 0, 0)
rodPos = initPos
Ball1Pos = initPos - vec(sqrt(2)/2,sqrt(2)/2,0)
Ball2Pos = initPos + vec(sqrt(2)/2,sqrt(2)/2,0)
initVel = vec(10, 10, 0)
rodVel = initVel
rodAcc = vec(0, g, 0)
len = 3;
baton = cylinder(pos = rodPos, axis = len * norm(rodVel), color=color.red, radius = .5)
ball1 = sphere(pos= Ball1Pos, radius = 0.5, color=color.red)
ball2 = sphere(pos= Ball2Pos, radius = 0.5, color=color.red)

while rodPos.y >= 0:
    rate(1 / dt)
    
    rodVel += rodAcc * dt
    rodPos += rodVel * dt
    Ball1Pos += rodVel * dt
    Ball2Pos += rodVel * dt
    
    baton.pos = rodPos
    baton.axis = len * norm(rodVel)
    ball1.pos = Ball1Pos
    ball2.pos = Ball2Pos
    
    t += dt
    