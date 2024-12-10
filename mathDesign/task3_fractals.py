import turtle

#Кривая Коха
def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

#Снежинка Коха из трех кривых
def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

#треугольник Серпинского
def sierpinski_triangle(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        length /= 2
        sierpinski_triangle(t, length, depth - 1)
        t.forward(length)
        sierpinski_triangle(t, length, depth - 1)
        t.backward(length)
        t.left(60)
        t.forward(length)
        t.right(60)
        sierpinski_triangle(t, length, depth - 1)
        t.left(60)
        t.backward(length)
        t.right(60)

def sierpinski_carpet(t, x, y, size, depth):
    t.color("blue")
    if depth == 0:
        t.penup()
        t.goto(x - size / 2, y - size / 2)
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    else:
        new_size = size / 3
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Пропускаем центральный квадрат
                if dx == 0 and dy == 0:
                    continue
                # Рекурсивно рисуем остальные квадраты
                sierpinski_carpet(t, x + dx * new_size, y + dy * new_size, new_size, depth - 1)

#фрактальное дерево(веточка)
def fractal_tree(t, length, angle, depth):
    if depth == 0:
        return

    t.forward(length)
    t.left(angle)
    fractal_tree(t, length * 0.7, angle, depth - 1)
    t.right(2 * angle)
    fractal_tree(t, length * 0.7, angle, depth - 1)
    t.left(angle)
    t.backward(length)

def option_koch_curve(t, depth):
    koch_curve(t, 400, depth)

def option_sierpinski_triangle(t, depth):
    sierpinski_triangle(t, 200, depth)

def option_fractal_tree(t, depth):
    angle = int(input("Введите угол разветвления (например, 30): "))
    fractal_tree(t, 100, angle, depth)

def option_sierpinski_carpet(t, depth):
    sierpinski_carpet(t, 0, 0, 300, depth)


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Задание 3 - Фракталы")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    choice = int(input("Выберите фрактал (1: Кривая Коха, 2: Треугольник Серпинского, 3: Дерево, 4: Ковер Серпинского): "))
    depth = int(input("Введите глубину рекурсии: "))

    fractals_dict = {
        1: option_koch_curve,
        2: option_sierpinski_triangle,
        3: option_fractal_tree,
        4: option_sierpinski_carpet,
    }

    if choice in fractals_dict:
        fractals_dict[choice](t, depth)
    else:
        print("Неверный выбор!")

    screen.mainloop()


if __name__ == "__main__":
    main()