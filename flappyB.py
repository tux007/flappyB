from ursina import *

window.title = "Flöppy Game"
app = Ursina()

window.exit_button.enabled = True

bird = Animation('assets/bird_blue', scale=2, collider='box')
#Animation('assets/game_over', scale=20, position=(1, 1))
camera.orthographic = True
camera.fov = 20

def update():
    bird.y = bird.y -0.1
    for pipe in pipes:
        pipe.x = pipe.x - 0.05
    if bird.y < -10:   
        time.sleep(3)
        quit()       
        
    if bird.y > 10:
        time.sleep(3)
        quit()

    if bird.intersects().hit:
        time.sleep(3)
        quit()

def input(key):
    if key == 'space':
        bird.y = bird.y + 2.5

pipes = []

pipe = Entity(model='quad', 
              texture='assets/pipe',
              position=(20,10),
              scale=(3, 15, 1),
              collider='box'
              )

def createPipes():
    newY = random.randint(4, 12)
    newPipe = duplicate(pipe, y=newY)
    newPipe2 = duplicate(pipe, y=newY-24)
    pipes.append(newPipe)
    pipes.append(newPipe2)
    invoke(createPipes, delay=5)

 

createPipes()
Sky()
app.run()