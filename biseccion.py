import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 3 * np.sin(0.5 * x) - 0.5 * x + 2


def biseccion(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El intervalo [a,b] no tiene cambio de signo.")
        return None, []

    iter_count = 0
    c_old = a
    puntos = []

    print(f"{'Iter':>4} | {'a':>10} | {'b':>10} | {'c':>10} | {'f(c)':>12} | {'Error':>12}")
    print("-"*70)

    while iter_count < max_iter:
        c = (a + b) / 2
        fc = f(c)
        error = abs(c - c_old)
        puntos.append(c)
        print(f"{iter_count:4d} | {a:10.6f} | {b:10.6f} | {c:10.6f} | {fc:12.6f} | {error:12.6f}")

        if fc == 0 or error < tol:
            return c, puntos

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        c_old = c
        iter_count += 1

    print("Se alcanzó el máximo número de iteraciones.")
    return c, puntos
a = 5.7
b = 5.8
raiz, puntos = biseccion(a, b)

print(f"\nRaíz aproximada: {raiz:.6f}")
x = np.linspace(a-1, b+1, 400)
y = f(x)

plt.figure(figsize=(10,6))
plt.plot(x, y, label="f(x)")
plt.axhline(0, color='black', linewidth=0.8)
for i, c in enumerate(puntos):
    plt.plot(c, f(c), 'ro')
    plt.text(c, f(c)+0.2, f"c{i}", fontsize=8, ha='center')

plt.title("Método de Bisección")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
