import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 500

score = 0
gameover = False


mario = Actor("mario3.png")
luigi = Actor("luigi3.png")

mario.pos = 100,100
luigi.pos = 200,200

def draw():
    screen.blit("mario_background.jpeg",(0,0))
    luigi.draw()
    mario.draw()
    screen.draw.text(str(score),(10,10),fontsize = 40)

    if gameover:
        screen.fill("green")
        screen.draw.text("The time is up",(10,10),fontsize = 40,color = "red")

def time_up():
    global gameover
    gameover = True


def update():
    global score
    
    if keyboard.left:
        mario.x = mario.x - 2
    
    if keyboard.right:
        mario.x = mario.x + 2

    if keyboard.up:
        mario.y = mario.y - 2

    if keyboard.down:
        mario.y = mario.y + 2

    luigi_collected = mario.colliderect(luigi)

    if luigi_collected:
        move_luigi()
        score = score + 10
        print(score)


def move_luigi():
    luigi.x = random.randint(50,500)
    luigi.y = random.randint(50,450)
    

clock.schedule(time_up,60)


pgzrun.go()