import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Judul Aplikasi
st.title("Optimasi Produksi Meja dan Kursi - Linear Programming")

st.markdown("### Fungsi Objektif:")
st.latex(r"Z = 500{,}000x + 300{,}000y")
st.markdown("### Kendala:")
st.latex(r"3x + 2y \leq 120 \quad \text{(Kayu)}")
st.latex(r"4x + 2y \leq 160 \quad \text{(Waktu kerja)}")
st.latex(r"x \geq 0, y \geq 0")

# Definisi koefisien
c = [-500000, -300000]  # Maks Z → Min -Z
A = [
    [3, 2],
    [4, 2]
]
b = [120, 160]

# Optimasi
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Menampilkan hasil
if result.success:
    x_opt, y_opt = result.x
    z_opt = -result.fun
    st.success("Solusi optimal ditemukan:")
    st.write(f"Jumlah meja (x): {x_opt:.0f}")
    st.write(f"Jumlah kursi (y): {y_opt:.0f}")
    st.write(f"Total keuntungan maksimum: Rp {z_opt:,.0f}")
else:
    st.error("Gagal menemukan solusi.")

# Visualisasi grafik
st.markdown("### Visualisasi Grafik")

x_vals = np.linspace(0, 50, 400)
y1 = (120 - 3 * x_vals) / 2
y2 = (160 - 4 * x_vals) / 2

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label=r'$3x + 2y \leq 120$', color='blue')
plt.plot(x_vals, y2, label=r'$4x + 2y \leq 160$', color='green')

plt.fill_between(x_vals, 0, np.minimum(y1, y2), where=(y1 > 0) & (y2 > 0), color='skyblue', alpha=0.3)

# Titik optimal
if result.success:
    plt.plot(x_opt, y_opt, 'ro', label='Solusi Optimal')
    plt.text(x_opt + 1, y_opt, f'({x_opt:.0f}, {y_opt:.0f})', color='red')

plt.xlim(0, 50)
plt.ylim(0, 80)
plt.xlabel('Meja (x)')
plt.ylabel('Kursi (y)')
plt.title('Grafik Linear Programming - Produksi Meja dan Kursi')
plt.legend()
plt.grid(True)

st.pyplot(plt)
