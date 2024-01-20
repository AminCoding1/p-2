import turtle
turtle.bgcolor("black")
t = turtle.Turtle()                             
screen = turtle.Screen()
h = screen.window_height()
w = screen.window_width()
def container():
    for count, y in enumerate(range(y1, y2, -1)):
        length = (-5 / 6) * (y + (h / 32))              
        t.penup()
        x = -length
        t.sety(y)
        t.goto(x, y)
        t.pendown()
        t.forward(length * 2)
        t.color([color1[i] + col_change * (count) for i, col_change in enumerate(color_change)]) 
def stem():
    for count, y in enumerate(range(y1, y2, -1)):
        length = (-5 / 6) * (h // 32)                   
        t.penup()
        x = length
        t.sety(y)
        t.goto(x, y)
        t.pendown()
        t.forward(-length * 2)
        t.color([color1[i] + col_change * (count) for i, col_change in enumerate(color_change)]) 
def base():
    for count, y in enumerate(range(y1, y2, -1)):                      
        t.penup()
        x = -w / 5
        t.sety(y)
        t.goto(x, y)
        t.pendown()
        t.forward(-x * 2)
        t.color([color1[i] + col_change * (count) for i, col_change in enumerate(color_change)]) 
                                                
color1 = (.7, 0, .7)                                    
color2 = (1, 1 ,0)                                  
t.color(color1)
color_change = [(col - color1[i]) / (3 * h // 16) for i, col in enumerate(color2)]
y1 = h//2 - h//16                                     
y2 = h//4
container()                                            
color1 = (0, 1, 0)                                       
color2 = (0, 0, 0)                                     
t.color(color1)
color_change = [(col - color1[i]) / (h // 4) for i, col in enumerate(color2)]
y1 = h // 4                                           
y2 = 0
container()                                           
color1 = (1, 1, 0)                                      
color2 = (0, 0, 0)                                      
t.color(color1)
color_change = [(col - color1[i]) / (13 * h // 32) for i, col in enumerate(color2)]
y1 = 0                                              
y2 = -13 * h // 32
stem()                                                  
color1 = (0, 0, 0)                                      
color2 = (0, 0, 0)                                      
t.color(color1)
color_change = [(col - color1[i]) / (h // 32) for i, col in enumerate(color2)]
y1 = -13 * h // 32                                     
y2 = -14 * h // 32
base()                                                 
t.hideturtle()
screen.exitonclick()