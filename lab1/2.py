import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.exp(x ** 2 / 2)


def f2(x):
    return np.sin(3 * x / 5) ** 3


def f3(x):
    return np.cos(x / (x + 1)) ** 2


def f4(x):
    return np.log(x + np.sqrt(4 + x ** 2))


def f5(x):
    return (x * np.arctan(2 * x)) / (x ** 2 + 4)


def df1(x):
    return x * np.exp(x ** 2 / 2)


def df2(x):
    return (3 / 5) * np.sin(3 * x / 5) ** 2 * np.cos(3 * x / 5) * 3


def df3(x):
    return -2 * np.cos(x / (x + 1)) * np.sin(x / (x + 1)) / ((x + 1) ** 2)


def df4(x):
    return 1 / np.sqrt(4 + x ** 2)


def df5(x):
    return (2 * x ** 2 + np.arctan(2 * x) - 8 * x) / (x ** 2 + 4) ** 2


functions = [f1, f2, f3, f4, f5]
derivatives = [df1, df2, df3, df4, df5]

intervals = [(0, 1), (2, 15), (-5, 5)]

steps = [0.01, 0.005]

for i, (func, dfunc) in enumerate(zip(functions, derivatives), start=1):
    for interval in intervals:
        for h in steps:
            x = np.arange(interval[0], interval[1] + h, h)

            y = func(x)
            dy_numeric = np.diff(y) / h
            x_numeric = x[:-1]

            dy_analytic = dfunc(x)

            plt.figure(figsize=(10, 6))
            plt.plot(x_numeric, dy_numeric, label="Численная производная", linestyle="--")
            plt.plot(x, dy_analytic, label="Аналитическая производная")
            plt.title(f"Функция {i}, Интервал {interval}, h={h}")
            plt.xlabel("x")
            plt.ylabel("y'")
            plt.legend()
            plt.grid()
            plt.show()
