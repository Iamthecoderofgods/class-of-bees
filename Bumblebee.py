#BUMBLEBEE
import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "The Bumblebee game"
bee = Actor("bee")
flower = Actor("flower")
flower.pos=200,300
bee.pos=100,400
#from random import randint
#WIDTH,HEIGHT
#score,game
score = 0
#variable to declare actors(bee, flower)
def draw():
    

#   screen.blit(nameofimage, position)
    screen.blit("backround",(0,0))
    bee.draw()
    flower.draw()


#display score
    screen.draw.text("score:"+str(score),(450,550))

#if game_over:
        
def place_flower():
    x= random.randint(0,WIDTH-50)
    y = random.randint(0,HEIGHT-50)
    flower.pos= x,y

#def time_up():
def update():
    global score
    if keyboard.right:
        bee.x+=10
        if bee.x>WIDTH:
            bee.x=WIDTH-50
    if keyboard.left:
        bee.x-=10
        if bee.x<0:
            bee.x=0
    if keyboard.down:
        bee.y+=10
        if bee.y>HEIGHT:
            bee.y=HEIGHT-50
    if keyboard.up:
        bee.y-=10
        if bee.y<0:
            bee.y=0
    if bee.colliderect(flower):
        place_flower()
        score+=1
    

pgzrun.go()