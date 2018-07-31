from turtle import*
shape("circle")
color("blue")
speed(-1)


for i in range(40):
    for j in range(4):
        forward(i*5)
        left(90)
    left(12)
mainloop()