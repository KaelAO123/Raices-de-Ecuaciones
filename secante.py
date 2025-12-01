import math
import matplotlib.pyplot as plt
import numpy as np

# --- Definir la función ---
def f(x):
    return 3 * np.sin(0.5*x) - 0.5*x + 2

# --- Método de la Secante ---
def secante(x0, x1, tol=1e-6, max_iter=100):
    puntos = [x0, x1]  # Guardar puntos sucesivos para graficar
    print(f"{'Iter':>4} | {'x_n':>10} | {'x_n-1':>10} | {'f(x_n)':>12} | {'Error':>12}")
    print("-"*70)
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-12:
            print("División por cero aproximada. Método falló.")
            break
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)
        puntos.append(x2)
        
        print(f"{i:4d} | {x1:10.6f} | {x0:10.6f} | {fx1:12.6f} | {error:12.6f}")
        
        if error < tol:
            return x2, puntos
        
        x0, x1 = x1, x2
    
    print("Se alcanzó el máximo número de iteraciones.")
    return x2, puntos

# --- Uso del método ---
x0 = 5.7   # Primer valor inicial
x1 = 5.8   # Segundo valor inicial
raiz, puntos = secante(x0, x1)
print(f"\nRaíz aproximada: {raiz:.6f}")

# --- Gráfica ---
x = np.linspace(x0-0.05, x1+0.05, 400)
y = f(x)

plt.figure(figsize=(10,6))
plt.plot(x, y, label="f(x)")
plt.axhline(0, color='black', linewidth=0.8)  # eje x

# Graficar los puntos sucesivos de la secante
for i, xi in enumerate(puntos):
    plt.plot(xi, f(xi), 'ro')
    desplazamiento = 0.05 + 0.05*(i%5)  # evitar solapamiento
    plt.text(xi, f(xi)+desplazamiento, f"x{i}", fontsize=8, ha='center')
    # Línea vertical hasta el eje x
    plt.plot([xi, xi], [0, f(xi)], 'r--', alpha=0.5)

plt.title("Método de la Secante")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
