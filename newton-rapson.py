import math
import matplotlib.pyplot as plt
import numpy as np

# --- Definir la función y su derivada ---
def f(x):
    return 3 * np.sin(0.5*x) - 0.5*x + 2

def df(x):
    return 1.5 * np.cos(0.5*x) - 0.5

# --- Método de Newton-Raphson ---
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    puntos = [x]  # Para graficar los puntos
    print(f"{'Iter':>4} | {'x_n':>10} | {'f(x_n)':>12} | {'Error':>12}")
    print("-"*50)
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:
            print("Derivada cercana a cero. Método falló.")
            break
        
        x_new = x - fx/dfx
        error = abs(x_new - x)
        puntos.append(x_new)
        print(f"{i:4d} | {x:10.6f} | {fx:12.6f} | {error:12.6f}")
        
        if error < tol:
            return x_new, puntos
        
        x = x_new
    
    print("Se alcanzó el máximo número de iteraciones.")
    return x, puntos

# --- Uso del método ---
x0 = 5.75  # Valor inicial
raiz, puntos = newton_raphson(x0)
print(f"\nRaíz aproximada: {raiz:.6f}")

# --- Gráfica ---
x = np.linspace(x0-0.1, x0+0.1, 400)
y = f(x)

plt.figure(figsize=(10,6))
plt.plot(x, y, label="f(x)")
plt.axhline(0, color='black', linewidth=0.8)  # eje x

# Graficar puntos sucesivos
for i, xi in enumerate(puntos):
    plt.plot(xi, f(xi), 'ro')
    desplazamiento = 0.05 + 0.05*(i%5)  # evitar solapamiento
    plt.text(xi, f(xi)+desplazamiento, f"x{i}", fontsize=8, ha='center')
    plt.plot([xi, xi], [0, f(xi)], 'r--', alpha=0.5)

plt.title("Método de Newton-Raphson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

# --- Guardar la figura ---
plt.savefig("imgs/Newton-Raphson.png", dpi=300)
plt.show()
