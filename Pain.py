from turtle import *
import time
velocidad = int(input('Velocidad: '))
title("Pain")
setup(1080, 1080, 0, 0)
screensize(2040, 2040)
speed(velocidad)

for a in range(50):
    forward(100)
    right(90)
    
    for b in range(1):
        forward(100)
        right(80)

        for c in range(3,11):

            for d in range(10,200,5):

                for e in range(c):
                    forward(100)
                    right(360/c)
                right(10)


    
    if a == 12:
        hideturtle()
hideturtle()
time.sleep(60*5)
