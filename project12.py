import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(700,700)
polygon = turtle.Turtle()
num_sides = 4
side_lenth = 300
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_lenth)
    polygon.right(angle)
turtle.done()