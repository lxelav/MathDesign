import turtle
import random
from mathDesign.task3_fractals import koch_curve

def draw_snowflake(t, num_rays, length, depth, angle_shift):
    t.penup()
    t.goto(-100, 0)
    t.setheading(angle_shift)
    t.pendown()

    for _ in range(num_rays):
        koch_curve(t, length, depth)
        t.right(360 / num_rays)



screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Снежинка Коха")

t = turtle.Turtle()
t.speed(0)

num_rays = random.randint(6, 12)  #Лучи(минимум 6 чтобы норм выглядело)
length = 100  #Длина стороны
depth = random.randint(1, 3) #Глубина рекурсии
color = random.choice(["blue", "cyan", "lightblue", "white", "purple"])
angle_shift = random.randint(0, 360)  #Угол

t.color(color)

draw_snowflake(t, 12, length, depth, angle_shift)

t.hideturtle()
screen.mainloop()
