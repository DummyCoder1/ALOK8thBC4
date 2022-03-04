import turtle
w = int(input('Enter the width of Rectangle'))
h = int(input('Enter the heigth of Rectangle'))
for variable in range(0, 2):
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
