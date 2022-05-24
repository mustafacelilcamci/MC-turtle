import turtle

m = turtle.Turtle()

turtle.Screen().bgcolor("white")
m.fillcolor("purple")



#M harfi
m.penup()
m.goto(-350,175)
m.pendown()

m.begin_fill()
m.speed(5)
m.right(90)
m.forward(200)
m.backward(200)
m.right(-90)
m.forward(65)
m.right(60)
m.forward(145)
m.right(240)
m.forward(145)
m.right(60)
m.forward(65)
m.right(90)
m.forward(200)
m.left(-90)
m.forward(45)
m.right(90)
m.forward(150)
m.left(150)
m.forward(170)
m.right(60)
m.forward(10)
m.right(56)
m.forward(170)
m.right(214)
m.forward(145)
m.left(-90)
m.forward(40)
m.end_fill()


#C harfi
m.penup()
m.goto(160, 175)
m.pendown()

m.begin_fill()
m.right(0)
m.forward(120)
m.right(-60)
m.forward(90)
m.right(-30)
m.forward(90)
m.left(35)
m.forward(90)
m.right(-55)
m.forward(120)
m.right(-90)
m.forward(40)
m.right(-90)
m.forward(100)
m.right(57)
m.forward(55)
m.right(33)
m.forward(75)
m.right(30)
m.forward(50)
m.right(60)
m.forward(100)
m.left(89)
m.forward(35)
m.end_fill()




m.hideturtle()
turtle.mainloop()