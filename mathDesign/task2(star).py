import turtle
import random

def draw_star(t, rays, length, fill_colors):
    angle = 360 / rays  #Считает угол между лучами 360 на количество лучей
    for i in range(rays):
        t.color(random.choice(fill_colors))

        #{begin_fill; end_fill} - обозначает область для закраски
        t.begin_fill()

        t.forward(length)
        t.right(180 - angle) #Это поворот для след.луча
        t.forward(length)

        t.end_fill()

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Задание 2 - Звезда")

t = turtle.Turtle()
t.speed(3)
t.width(2)

# Случайные параметры
rays = random.randint(5, 12)  #Лучи
length = random.randint(50, 150)  #Их длина
fill_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

print(f"Количество лучей: {rays}")
print(f"Длина лучей: {length}")

draw_star(t, rays, length, fill_colors)

turtle.done()

