import streamlit as st
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Optimasi Produksi Meja dan Kursi (Linear Programming)")

# Fungsi Optimasi
c = [-40, -30]  # Koefisien fungsi tujuan (dinegatifkan karena linprog = minimisasi)
A = [[2, 1], [1, 1]]  # Koefisien kendala (mesin & tenaga kerja)
b = [100, 80]  # Sisi kanan kendala

# Menyelesaikan LP
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Hasil
if result.success:
    x_opt, y_opt = result.x
    z_max = -result.fun
    st.success("✅ Solusi Optimal Ditemukan:")
    st.write(f"Jumlah Meja (x): **{x_opt:.2f} unit**")
    st.write(f"Jumlah Kursi (y): **{y_opt:.2f} unit**")
    st.write(f"Keuntungan Maksimum (Z): **Rp{z_max * 1000:,.2f}**")
else:
    st.error("❌ Gagal menemukan solusi.")
    st.write(result.message)

# Visualisasi Grafik
st.subheader("Visualisasi Kendala dan Area Feasible")

fig, ax = plt.subplots()

# Garis kendala 1: 2x + y ≤ 100
x = np.linspace(0, 60, 400)
y1 = 100 - 2 * x

# Garis kendala 2: x + y ≤ 80
y2 = 80 - x

# Area feasible (yang memenuhi semua kendala)
y3 = np.minimum(y1, y2)
y3 = np.maximum(y3, 0)

ax.plot(x, y1, label='2x + y ≤ 100', color='blue')
ax.plot(x, y2, label='x + y ≤ 80', color='green')
ax.fill_between(x, 0, y3, where=(y3 >= 0), color='orange', alpha=0.3, label='Area Feasible')

# Titik optimal
if result.success:
    ax.plot(x_opt, y_opt, 'ro', label='Solusi Optimal')
    ax.annotate(f'({x_opt:.2f}, {y_opt:.2f})', (x_opt + 1, y_opt - 1), color='red')

ax.set_xlim(0, 60)
ax.set_ylim(0, 80)
ax.set_xlabel('Jumlah Meja (x)')
ax.set_ylabel('Jumlah Kursi (y)')
ax.set_title('Grafik Kendala dan Area Solusi')
ax.legend()
ax.grid(True)

st.pyplot(fig)
