import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")  
screen.title("Basketball Court")

court_turtle = turtle.Turtle()
court_turtle.speed(5)


def draw_rectangle(x, y, width, height, color):
    court_turtle.penup()
    court_turtle.goto(x, y)
    court_turtle.pendown()
    court_turtle.begin_fill()
    court_turtle.fillcolor(color)
    for _ in range(2):
        court_turtle.forward(width)
        court_turtle.left(90)
        court_turtle.forward(height)
        court_turtle.left(90)
    court_turtle.end_fill()

def draw_circle(x, y, radius, color):
    court_turtle.penup()
    court_turtle.goto(x, y - radius)
    court_turtle.pendown()
    court_turtle.begin_fill()
    court_turtle.fillcolor(color)
    court_turtle.circle(radius)
    court_turtle.end_fill()

#player symbol
def draw_player(x, y, symbol, color):
    court_turtle.penup()
    court_turtle.goto(x, y)
    court_turtle.pendown()
    court_turtle.color(color)
    court_turtle.write(symbol, font=("Arial", 12, "normal"))

#random symbols in various colors on the outer black background
def draw_random_symbols(num_symbols):
    symbols = "!@#%^&*"
    for _ in range(num_symbols):
        x = random.uniform(-375, -280)  
        y = random.uniform(-300, 300)
        color = random.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink"])
        symbol = random.choice(symbols)
        size = random.randint(10, 30)
        
        court_turtle.penup()
        court_turtle.goto(x, y)
        court_turtle.pendown()
        court_turtle.color(color)
        court_turtle.write(symbol, font=("Arial", size, "normal"))
        
    for _ in range(num_symbols):
        x = random.uniform(375, 280)  
        y = random.uniform(-300, 300)
        color = random.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink"])
        symbol = random.choice(symbols)
        size = random.randint(10, 30)
        
        court_turtle.penup()
        court_turtle.goto(x, y)
        court_turtle.pendown()
        court_turtle.color(color)
        court_turtle.write(symbol, font=("Arial", size, "normal"))
        
    for _ in range(num_symbols):
        x = random.uniform(-290, 280)  
        y = random.uniform(155, 300)
        color = random.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink"])
        symbol = random.choice(symbols)
        size = random.randint(10, 30)
        
        court_turtle.penup()
        court_turtle.goto(x, y)
        court_turtle.pendown()
        court_turtle.color(color)
        court_turtle.write(symbol, font=("Arial", size, "normal"))
        
    for _ in range(num_symbols):
        x = random.uniform(-290, 280)  
        y = random.uniform(-300, -200)
        color = random.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink"])
        symbol = random.choice(symbols)
        size = random.randint(10, 30)
        
        court_turtle.penup()
        court_turtle.goto(x, y)
        court_turtle.pendown()
        court_turtle.color(color)
        court_turtle.write(symbol, font=("Arial", size, "normal"))

#basketball court elements
draw_rectangle(-250, -150, 500, 300, "#FFFFFF")  
draw_rectangle(-240, -140, 480, 280, "#F0D9B5")  
draw_circle(0, 0, 50, "#FFA500")                 
draw_rectangle(-5, -150, 10, 300, "#FFFFFF")      

#basketball hoop and backboard
draw_rectangle(-240, -50, 20, 100, "#FFFFFF")     
draw_rectangle(220, -50, 20, 100, "#FFFFFF")      
draw_circle(-220, 0, 15, "#FFA500")             
draw_circle(-220, 0, 10, "#FFFFFF")             
draw_circle(220, 0, 15, "#FFA500")              
draw_circle(220, 0, 10, "#FFFFFF") 

#players
draw_player(-120, -70, "+", "blue")  
draw_player(-130, 40, "+", "blue")  
draw_player(-180, -10, "+", "blue")  
draw_player(-90, -50, "+", "blue")
draw_player(-165, -65, "+", "blue")

draw_player(100, -35, "$", "green")    
draw_player(150, 60, "$", "green")    
draw_player(80, -30, "$", "green")  
draw_player(200, -55, "$", "green") 
draw_player(50, -90, "$", "green")   


draw_random_symbols(50)

court_turtle.hideturtle()

turtle.mainloop()
