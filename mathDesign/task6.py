import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

COLORS = ["red", "green", "blue", "yellow"]
NUM_COLORS = len(COLORS)

def draw_triangle(x, y, size, color, shape_type):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)


    if shape_type == "right":
        # Прямоугольный
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(135)
        t.forward(size * math.sqrt(2))
        t.left(135)
    elif shape_type == "acute":
        # Остроугольный
        for _ in range(3):
            t.forward(size)
            t.left(60)


def draw_square(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(size)
        t.left(90)


def draw_hexagon(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(6):
        t.forward(size)
        t.left(60)


def generate_tiling(shape_type):
    size = 50
    x_offset = 1.5 * size
    y_offset = math.sqrt(3) * size
    for row in range(-250, 250, int(y_offset)):
        for col in range(-350, 350, int(x_offset)):
            color = random.choice(COLORS)
            if shape_type == "triangle":
                shape_type_specific = random.choice(["right", "acute"])
                draw_triangle(col, row, size, color, shape_type_specific)
            elif shape_type == "square":
                draw_square(col, row, size, color)
            elif shape_type == "hexagon":
                draw_hexagon(col, row, size, color)


print("Выберите фигуру для замощения плоскости:")
print("1. Треугольники")
print("2. Квадраты")
print("3. Шестиугольники")
choice = input("Введите номер фигуры (1-3): ")

if choice == "1":
    shape_type = "triangle"
elif choice == "2":
    shape_type = "square"
elif choice == "3":
    shape_type = "hexagon"
else:
    print("Неверный выбор. Выбрана фигура по умолчанию: Треугольники.")
    shape_type = "triangle"

generate_tiling(shape_type)
turtle.done()
