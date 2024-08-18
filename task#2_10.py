import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Межі інтегрування
a, b = 0, 2

# Визначення функції для інтегрування
def f(x):
    return x ** 2

def monte_carlo_integration(a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Кількість точок під кривою
    under_curve = np.sum(y_random < f(x_random))

    # Площа під кривою
    area_under_curve = (b - a) * f(b) * under_curve / num_samples

    return area_under_curve

# Обчислення інтеграла за допомогою функції quad
result_quad, _ = spi.quad(f, a, b)

# Обчислення інтеграла методом Монте-Карло
result_monte_carlo = monte_carlo_integration(a, b, 100000)

print(f"Площа обчислена методом Монте-Карло: {result_monte_carlo}")
print(f"Площа обчислена функцією quad: {result_quad}")



import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

def visualize_results(x_random, y_random):
    a, b = 0, 2
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)
    ax.scatter(x_random, y_random, color="red", s=1)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) від {a} до {b}")

    plt.grid()
    plt.show()

# Генерація випадкових точок для прикладу
x_random = np.random.uniform(0, 2, 1000)
y_random = np.random.uniform(0, 4, 1000)  # верхня межа y визначена як f(2) = 4

visualize_results(x_random, y_random)
