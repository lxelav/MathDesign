import turtle


def draw_spiral(angle, step=1, length=1000):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Задание 1 - Спираль")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    current_length = 0
    while current_length < length:
        t.forward(step)
        t.right(angle)
        current_length += step
        step += 0.2  # Увеличение шага для более явной структуры

    turtle.done()


print("Выберите угол для спирали:")
print("1: 30 градусов")
print("2: 45 градусов")
print("3: 60 градусов")

choice = int(input("Введите номер угла (1/2/3): "))
angles = {1: 30, 2: 45, 3: 60}
angle = angles.get(choice, 30)

draw_spiral(angle)
