Web VPython 3.2

scene.camera.pos = vec(15, 5, 20)

launched = False
drag = False
slop = 5

button(text = "launch", pos = scene.title_anchor, bind = launch)

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

def launch():
    global launched
    launched = True
    
def down():
    global drag
    print("its not dragging time!")
    if (mag(baton.pos - scene.mouse.pos) < slop and launched == False):
        drag = True
        print("its dragging time!")
        
def move():
    if drag:
        arrow(pos = baton.pos, axis = scene.mouse.pos)
        print("its moving time!")
        
def up():
    global drag
    drag = False

while rodPos.y >= 0:
    rate(1 / dt)
    
    scene.bind("mousedown", down)
    scene.bind("mousemove", move)
    
    if launched:
        rodVel += rodAcc * dt
        rodPos += rodVel * dt
    
        baton.pos = rodPos
        baton.axis = len * norm(rodVel)
    
        t += dt
