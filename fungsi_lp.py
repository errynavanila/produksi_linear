import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Fungsi tujuan: Maks Z = 40x + 30y → Min Z = -40x -30y
c = [-40, -30]

# Kendala:
A = [
    [2, 1],   # 2x + y ≤ 100 (Mesin)
    [1, 1]    # x + y ≤ 80 (Tenaga kerja)
]
b = [100, 80]

# Batasan non-negatif
x_bounds = (0, None)
y_bounds = (0, None)

# Solusi
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Tampilkan hasil
if result.success:
    x_opt, y_opt = result.x
    z_max = -result.fun
    print("Solusi optimal ditemukan!")
    print(f"x (Meja) = {x_opt:.2f}")
    print(f"y (Kursi) = {y_opt:.2f}")
    print(f"Keuntungan Maksimum = Rp{z_max * 1000:.0f}")
else:
    print("Gagal menemukan solusi.")
    exit()

# Visualisasi grafik
x = np.linspace(0, 100, 400)
y1 = (100 - 2*x)         # dari 2x + y ≤ 100
y2 = (80 - x)            # dari x + y ≤ 80

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="2x + y ≤ 100 (Mesin)", color='blue')
plt.plot(x, y2, label="x + y ≤ 80 (Tenaga kerja)", color='green')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.fill_between(x, 0, np.minimum(y1, y2), where=(np.minimum(y1, y2) >= 0), alpha=0.3, color='orange')

# Titik solusi optimal
plt.plot(x_opt, y_opt, 'ro', label='Solusi Optimal')
plt.text(x_opt + 1, y_opt, f'({x_opt:.0f}, {y_opt:.0f})', color='red')

# Label dan legend
plt.title("Wilayah Feasible dan Solusi Optimal")
plt.xlabel("Jumlah Meja (x)")
plt.ylabel("Jumlah Kursi (y)")
plt.xlim(0, max(x))
plt.ylim(0, max(np.max(y1), np.max(y2)))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
