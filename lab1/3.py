import numpy as np
import matplotlib.pyplot as plt

h = 0.025

x_values = np.arange(0, 10 + h, h)

# Задача (a)
def f_a(y):
    return 0.5 * y

def euler_a(h, x_values, y0):
    y = np.zeros(len(x_values))
    y[0] = y0
    for i in range(1, len(x_values)):
        y[i] = y[i-1] + h * f_a(y[i-1])
    return y

# Задача (b)
def f_b(x, y):
    return 2*x + 3*y

def euler_b(h, x_values, y0):
    y = np.zeros(len(x_values))
    y[0] = y0
    for i in range(1, len(x_values)):
        y[i] = y[i-1] + h * f_b(x_values[i-1], y[i-1])
    return y

# Задача (c)
def f_c1(x2):
    return x2

def f_c2(x1):
    return -x1

def euler_c(h, x_values, x1_0, x2_0):
    x1 = np.zeros(len(x_values))
    x2 = np.zeros(len(x_values))
    x1[0] = x1_0
    x2[0] = x2_0
    for i in range(1, len(x_values)):
        x1[i] = x1[i-1] + h * f_c1(x2[i-1])
        x2[i] = x2[i-1] + h * f_c2(x1[i-1])
    return x1, x2

# Задача (d)
def f_d1(x1):
    return 4 * x1

def f_d2(x1):
    return x1

def euler_d(h, x_values, x1_0, x2_0):
    x1 = np.zeros(len(x_values))
    x2 = np.zeros(len(x_values))
    x1[0] = x1_0
    x2[0] = x2_0
    for i in range(1, len(x_values)):
        x1[i] = x1[i-1] + h * f_d1(x1[i-1])
        x2[i] = x2[i-1] + h * f_d2(x1[i-1])
    return x1, x2


y_a = euler_a(h, x_values, 1)  # Задача (a)
y_b = euler_b(h, x_values, -2) # Задача (b)
x1_c, x2_c = euler_c(h, x_values, 1, 0)  # Задача (c)
x1_d, x2_d = euler_d(h, x_values, 1, 1)  # Задача (d)



plt.figure(figsize=(10, 8))

# Задача (a)
plt.subplot(2, 2, 1)
plt.plot(x_values, y_a, label="Приближенное решение")
plt.title("Задача (a): y' = 1/2 y, y(0) = 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Задача (b)
plt.subplot(2, 2, 2)
plt.plot(x_values, y_b, label="Приближенное решение", color="r")
plt.title("Задача (b): y' = 2x + 3y, y(0) = -2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Задача (c)
plt.subplot(2, 2, 3)
plt.plot(x_values, x1_c, label="x1", color="g")
plt.plot(x_values, x2_c, label="x2", color="b")
plt.title("Задача (c): x1' = x2, x2' = -x1")
plt.xlabel("x")
plt.ylabel("x1, x2")
plt.grid(True)

# Задача (d)
plt.subplot(2, 2, 4)
plt.plot(x_values, x1_d, label="x1", color="m")
plt.plot(x_values, x2_d, label="x2", color="c")
plt.title("Задача (d): x1' = 4x1, x2' = x1")
plt.xlabel("x")
plt.ylabel("x1, x2")
plt.grid(True)

plt.tight_layout()
plt.show()
