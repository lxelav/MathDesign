import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# Определяем систему дифференциальных уравнений
def ode_system(x, y):
    y1, y2 = y
    dy1dx = y2
    dy2dx = x**2 * y2 + (2 / x**2) * y1 + 1 + (4 / x**2)
    return np.vstack((dy1dx, dy2dx))

# Определяем граничные условия
def boundary_conditions(ya, yb):
    bc1 = 2 * ya[0] - ya[1] - 6  # Граничное условие в точке x=0.5
    bc2 = yb[0] + 3 * yb[1] + 1  # Граничное условие в точке x=1
    return np.array([bc1, bc2])


x = np.linspace(0.5, 1, 100)

# Инициализируем начальные приближения для решения задачи
y_init = np.zeros((2, x.size))

# Решаем задачу краевых значений
solution = solve_bvp(ode_system, boundary_conditions, x, y_init)

if solution.status != 0:
    print("Численное решение не удалось получить")
else:
    print("Численное решение получено успешно.")

# Извлекаем результаты решения
x_sol = solution.x
y_sol = solution.y[0]
y_prime_sol = solution.y[1]

# Вычисляем вторую производную y''(x) с помощью системы дифференциальных уравнений
y_double_prime_sol = ode_system(x_sol, solution.y)[1]

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x_sol, y_sol, label='y(x)')
plt.title('График функции y(x)')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.legend()

# График первой производной y'(x)
plt.subplot(3, 1, 2)
plt.plot(x_sol, y_prime_sol, label="y'(x)", color='orange')
plt.title("График первой производной y'(x)")
plt.xlabel('x')
plt.ylabel("y'(x)")
plt.grid(True)
plt.legend()

# График второй производной y''(x)
plt.subplot(3, 1, 3)
plt.plot(x_sol, y_double_prime_sol, label="y''(x)", color='green')
plt.title("График второй производной y''(x)")
plt.xlabel('x')
plt.ylabel("y''(x)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Таблица значений функции и ее производных в выбранных точках
x_table = np.linspace(0.5, 1, 10)
y_table = solution.sol(x_table)[0]
y_prime_table = solution.sol(x_table)[1]
y_double_prime_table = ode_system(x_table, solution.sol(x_table))[1]

for xi, yi, ypi, ydpi in zip(x_table, y_table, y_prime_table, y_double_prime_table):
    print(f"{xi:.3f}    {yi:.6f}    {ypi:.6f}    {ydpi:.6f}")
