import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Fungsi objektif (maks Z = 500000x + 300000y) → min -Z
c = [-500000, -300000]

# Kendala: 3x + 2y <= 120, 4x + 2y <= 160
A = [
    [3, 2],
    [4, 2]
]
b = [120, 160]

# Selesaikan LP
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Plot grafik
x_vals = np.linspace(0, 50, 400)
y1 = (120 - 3 * x_vals) / 2
y2 = (160 - 4 * x_vals) / 2

plt.figure(figsize=(8,6))
plt.plot(x_vals, y1, label=r'$3x + 2y \leq 120$', color='blue')
plt.plot(x_vals, y2, label=r'$4x + 2y \leq 160$', color='green')

# Arsiran daerah layak
plt.fill_between(x_vals, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color='skyblue', alpha=0.3)

# Titik solusi optimal
if res.success:
    x_opt, y_opt = res.x
    plt.plot(x_opt, y_opt, 'ro', label='Solusi optimal')
    plt.text(x_opt + 0.5, y_opt, f'({x_opt:.0f}, {y_opt:.0f})', color='red')

# Label dan tampilan
plt.xlim(0, 50)
plt.ylim(0, 80)
plt.xlabel('Meja (x)')
plt.ylabel('Kursi (y)')
plt.title('Grafik Linear Programming: Produksi Meja & Kursi')
plt.grid(True)
plt.legend()
plt.show()
