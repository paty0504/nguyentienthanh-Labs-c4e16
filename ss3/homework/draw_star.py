from turtle import *
shape('turtle')
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
# draw_star(100, 50, 100)
    return [x,y,length]
mainloop()
speed(-1)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
