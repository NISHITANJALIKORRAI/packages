import turtle

#Screen setting
screen=turtle.Screen()
screen.bgcolor("white")


#Create turtle
pen=turtle.Turtle()
pen.speed(3)
pen.width(4)


#Face
pen.penup()
pen.goto(0,-150) #As screen center is (0,0)
pen.pendown()

pen.color("black")
pen.fillcolor("yellow")

pen.begin_fill()
pen.circle(150)
pen.end_fill()


#Left Eye
pen.penup()
pen.goto(-60,50)
pen.pendown()

pen.color("black")
pen.fillcolor("black")

pen.begin_fill()
pen.circle(15)
pen.end_fill()


#Right Eye
pen.penup()
pen.goto(60,50)
pen.pendown()

pen.color("black")
pen.fillcolor("black")

pen.begin_fill()
pen.circle(15)
pen.end_fill()


#Smile
pen.penup()
pen.goto(-70,-30)
pen.setheading(-60)
pen.pendown()

pen.width(5)
pen.circle(80,120)

#Text
pen.penup()
pen.goto(-90,190)
pen.color("blue")

pen.write(
    "Smiley Face",
    font=("Time New Roman",24,"bold")
)

pen.hideturtle()
turtle.done()