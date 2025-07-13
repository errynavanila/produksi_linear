import streamlit as st
from scipy.optimize import linprog

st.set_page_config(page_title="Optimasi Produksi Meja dan Kursi", layout="centered")

st.title("📊 Aplikasi Optimasi Produksi Meja dan Kursi")

st.markdown("""
Masukkan data untuk menghitung jumlah meja dan kursi yang harus diproduksi untuk memaksimalkan keuntungan.
""")

# Input dari user
col1, col2 = st.columns(2)

with col1:
    profit_meja = st.number_input("Keuntungan per Meja (Rp)", value=500000)
    kayu_meja = st.number_input("Kebutuhan Kayu per Meja", value=3)
    waktu_meja = st.number_input("Waktu Kerja per Meja (jam)", value=4)

with col2:
    profit_kursi = st.number_input("Keuntungan per Kursi (Rp)", value=300000)
    kayu_kursi = st.number_input("Kebutuhan Kayu per Kursi", value=2)
    waktu_kursi = st.number_input("Waktu Kerja per Kursi (jam)", value=2)

st.markdown("### Batasan Sumber Daya")
total_kayu = st.number_input("Total Kayu Tersedia", value=120)
total_waktu = st.number_input("Total Jam Kerja Tersedia", value=160)

if st.button("Hitung Optimasi"):
    # Fungsi objektif (max → min)
    c = [-profit_meja, -profit_kursi]

    # Matriks kendala
    A = [
        [kayu_meja, kayu_kursi],
        [waktu_meja, waktu_kursi]
    ]
    b = [total_kayu, total_waktu]

    result = linprog(c, A_ub=A, b_ub=b, method="highs")

    if result.success:
        x, y = result.x
        total_profit = -result.fun

        st.success("✅ Solusi optimal ditemukan!")
        st.write(f"Jumlah Meja yang diproduksi: **{x:.2f}**")
        st.write(f"Jumlah Kursi yang diproduksi: **{y:.2f}**")
        st.write(f"Total Keuntungan Maksimum: **Rp {total_profit:,.2f}**")
    else:
        st.error("❌ Gagal menemukan solusi.")
