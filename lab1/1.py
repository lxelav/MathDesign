import numpy as np
import matplotlib.pyplot as plt
import math

steps = [0.01, 0.005, 0.001]

intervals = {
    "e^(-x/2)": [0, np.pi / 2],
    "sin(3x)": [2, 10],
    "cos^2(5x)": [-3, 3],
    "sum(x^(2n)/(2n)!) (cosh(x))": [-3, 3]
}

def f1(x):
    return np.exp(-x / 2)

def f2(x):
    return np.sin(3 * x)

def f3(x):
    return np.cos(5 * x) ** 2

def f4(x):
    # Вычисление частичной суммы ряда Тейлора для cosh(x)
    terms = [x ** (2 * n) / math.factorial(2 * n) for n in range(10)]
    return np.sum(terms, axis=0)


functions = {
    "e^(-x/2)": f1,
    "sin(3x)": f2,
    "cos^2(5x)": f3,
    "sum(x^(2n)/(2n)!) (cosh(x))": f4
}

for step in steps:
    print(f"Построение для шага h = {step}")

    plt.figure(figsize=(14, 8))
    for name, func in functions.items():
        a, b = intervals[name]
        x_continuous = np.linspace(a, b, 1000)  # Для построения непрерывного графика
        y_continuous = func(x_continuous)  # Значения функции для непрерывного графика

        x_discrete = np.arange(a, b + step, step)
        y_discrete = func(x_discrete)  # Значения функции для сеточных точек

        plt.plot(
            x_continuous, y_continuous,
            label=f"{name} (непрерывная)", linestyle='-', alpha=1.0, linewidth=2.5, color=np.random.rand(3, )
        )

        plt.scatter(
            x_discrete, y_discrete,
            label=f"{name} (сеточная, h={step})", s=50, marker='o', alpha=0.9, edgecolor="black", color="red"
        )

        print(f"\nФункция: {name}")
        print(f"x (первые 5 точек): {x_discrete[:5]}")
        print(f"y (первые 5 значений): {y_discrete[:5]}")

    plt.title(f"Графики функций при шаге h = {step}", fontsize=16)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
