import turtle
turtle.bgcolor('lightpink')
turtle.pensize(12)
turtle.speed(0.2)
color = ['red','yellow','blue','orange']


for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(50)
        turtle.left(10)

turtle.mainloop()
