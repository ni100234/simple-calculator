
import turtle   
pen = turtle.Turtle()
color=['red','green','orange','purple','yellow','blue']
w=turtle.Screen()
w.title('pattern')
w.bgcolor('black')
pen.pensize('1')
turtle.speed(30)

for i in range(150):
    pen.pencolor(color[i%6])
    pen.width(i/100+1)
    pen.forward(i)
    pen.right(59)
turtle.done()