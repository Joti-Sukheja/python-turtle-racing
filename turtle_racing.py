import turtle
import time
import random

print("-----Welcome to turtle racing----")
WIDTH, HEIGHT = 400,400
COLORS = ["red","yellow","green","blue","orange","purple","brown","cyan","black","grey"]

def input_racers():
 while True:
    racers = input("Enter the number of turtles (2 - 10) ")
    if racers.isdigit():
        racers  = int(racers)
        if 2 <= racers <= 10:
            break
        else:
            print("Please enter the number between (2 - 10). ") 
    else:
        print("Please enter a number.")        
 return racers

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing")
    
        
def race(colors):
    Turtles = create_turtle(colors)
    while True:
        for racer in Turtles:
            dis = random.randrange(1, 20)
            racer.forward(dis)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 20:
                return colors[Turtles.index(racer)]
            
def create_turtle(colors):
    Turtles = []
    spacing  = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
      racer = turtle.Turtle()
      racer.color(color)
      racer.shape("turtle")
      racer.left(90)
      racer.penup()
      racer.setpos(-WIDTH//2 + (i+1)* spacing,-HEIGHT//2 +20)
      racer.pendown()
      Turtles.append(racer)
    return Turtles  


racers = input_racers()  
init_screen()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("winner is", winner)
time.sleep(5)
