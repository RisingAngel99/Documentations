from turtle import *

bgcolor("black")
color("red")
title("StudyMuch")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill

penup()
goto(0, -50)
pendown()
color("red")
write("Ich wuv dich ", align="center",
      font=("Brush Script TM", 45, "normal"))
hideturtle()
done()