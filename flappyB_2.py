from ursina import *

window.title = "Flöppy Game"
app = Ursina()

window.exit_button.enabled = True

bird = Animation('assets/bird_blue', scale=2, collider='box')
camera.orthographic = True
camera.fov = 20

game_over_popup = Entity(
    model='quad',
    texture='white_cube',
    scale=(5, 3, 1),
    position=(0, 0, 0),
    enabled=False  # Initially disabled
)

game_over_text = Text(
    parent=game_over_popup,
    text='Game Over',
    scale=2,
    position=(0, 0.5),
    color=color.black
)

restart_button = Button(
    parent=game_over_popup,
    text='Restart',
    scale=(1.5, 0.5),
    position=(0, -0.5),
    on_click=lambda: restart_game()
)

def restart_game():
    # Reset the game state here
    bird.y = 0  # Reset bird position
    for pipe in pipes:
        pipe.disable()  # Disable existing pipes
    pipes.clear()  # Clear the pipe list
    createPipes()  # Create new pipes
    game_over_popup.enabled = False  # Hide the game over popup

def update():
    bird.y = bird.y - 0.1
    for pipe in pipes:
        pipe.x = pipe.x - 0.05

    if bird.y < -10 or bird.y > 10 or bird.intersects().hit:
        game_over_popup.enabled = True  # Show the game over popup
        invoke(lambda: time.sleep(3), delay=0)  # Delay before quitting

def input(key):
    if key == 'space':
        bird.y = bird.y + 2.5

pipes = []

pipe = Entity(model='quad', 
              texture='assets/pipe',
              position=(20, 10),
              scale=(3, 15, 1),
              collider='box'
              )

def createPipes():
    newY = random.randint(4, 12)
    newPipe = duplicate(pipe, y=newY)
    newPipe2 = duplicate(pipe, y=newY - 24)
    pipes.append(newPipe)
    pipes.append(newPipe2)
    invoke(createPipes, delay=5)

createPipes()
Sky()
app.run()