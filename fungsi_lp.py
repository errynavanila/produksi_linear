import streamlit as st
from scipy.optimize import linprog
import numpy as np

st.set_page_config(page_title="Optimasi Produksi", layout="centered")

st.title("📦 Aplikasi Optimasi Produksi (Linear Programming)")

st.markdown("""
Masukkan koefisien untuk fungsi objektif dan kendala.  
Contoh: Maksimalkan Z = 40x + 30y  
Dengan kendala:  
- 2x + y ≤ 100  
- x + y ≤ 80
""")

st.subheader("Fungsi Objektif")
c1 = st.number_input("Koefisien x", value=40.0)
c2 = st.number_input("Koefisien y", value=30.0)

st.subheader("Kendala")
A = []
b = []

col1, col2, col3 = st.columns(3)
with col1:
    a1 = st.number_input("Kendala 1 - x", value=2.0)
with col2:
    a2 = st.number_input("Kendala 1 - y", value=1.0)
with col3:
    b1 = st.number_input("Batas Kendala 1", value=100.0)

col4, col5, col6 = st.columns(3)
with col4:
    a3 = st.number_input("Kendala 2 - x", value=1.0)
with col5:
    a4 = st.number_input("Kendala 2 - y", value=1.0)
with col6:
    b2 = st.number_input("Batas Kendala 2", value=80.0)

if st.button("🔍 Hitung Solusi Optimal"):
    # Format LP untuk linprog (minimisasi)
    c = [-c1, -c2]  # Negatif karena linprog = minimisasi
    A_ub = [[a1, a2], [a3, a4]]
    b_ub = [b1, b2]

    result = linprog(c, A_ub=A_ub, b_ub=b_ub, method="highs")

    if result.success:
        st.success("✅ Solusi optimal ditemukan!")
        st.write(f"Nilai x = **{result.x[0]:.2f}**")
        st.write(f"Nilai y = **{result.x[1]:.2f}**")
        st.write(f"Nilai maksimum Z = **{-result.fun:.2f}**")
    else:
        st.error("❌ Gagal menemukan solusi.")
        st.text(result.message)
