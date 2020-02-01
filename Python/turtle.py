import turtle
import time
turtle.pensize(4)
turtle.speed(2)

melinda = turtle.Turtle()
melinda.color("red")
melinda.speed(2)
melinda.forward(200)
melinda.left(120)
melinda.forward(200)
melinda.left(120)
melinda.forward(200)
melinda.reset()
time.sleep(1)

melinda.color("red")
melinda.speed(2)
melinda.circle(100)
time.sleep(1)

melinda.reset()
melinda.speed(2)
melinda.color("red")
for side in [1, 2, 3, 4]:
    melinda.forward(200)
    melinda.right(90)
time.sleep(1)

melinda.reset()
melinda.speed(2)
melinda.color("red")
melinda.left(30)
melinda.forward(200)
melinda.right(60)
melinda.forward(200)
melinda.right(120)
melinda.forward(200)
melinda.right(60)
melinda.forward(200)
time.sleep(1)

melinda.reset()
melinda.speed(2)
melinda.color("red")
for side in [1, 2, 3, 4, 5]:
    melinda.forward(200)
    melinda.right(144)
time.sleep(1)

melinda.reset()
melinda.speed(2)
melinda.color("red")
for side in [1, 2, 3, 4, 5, 6]:
    melinda.forward(200)
    melinda.right(60)
time.sleep(1)

#turtle.penup()
turtle.mainloop()
