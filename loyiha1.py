import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)

def daraxt(uzunlik):
    if uzunlik < 10:
        t.color("green")
        t.dot(10)
        t.color("brown")
        return

    t.forward(uzunlik)

    t.right(30)
    daraxt(uzunlik * 0.7)

    t.left(60)
    daraxt(uzunlik * 0.7)

    t.right(30)
    t.backward(uzunlik)

t.color("brown")
daraxt(100)

t.hideturtle()
turtle.done()