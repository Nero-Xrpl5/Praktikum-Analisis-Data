# =========================
# Analisis Nilai Siswa Interaktif (Lengkap + Efisien)
# =========================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot

# =========================
# BACA DATA
# =========================
data = pd.read_csv('nilai_siswa.csv')
data.columns = data.columns.str.strip().str.lower()

# Pastikan kolom utama ada
kolom_mapel = 'mapel' if 'mapel' in data.columns else 'mata pelajaran'
kolom_nilai = 'nilai'
kolom_nama = 'nama' if 'nama' in data.columns else None

# =========================
# ANALISIS DASAR
# =========================
rata_mapel = data.groupby(kolom_mapel)[kolom_nilai].mean().sort_values(ascending=False)
mapel_tertinggi = rata_mapel.idxmax()
mapel_terendah = rata_mapel.idxmin()

print("=== HASIL ANALISIS DATA ===")
print(f"Mapel dengan rata-rata nilai tertinggi: {mapel_tertinggi} ({rata_mapel.max():.2f})")
print(f"Mapel dengan rata-rata nilai terendah : {mapel_terendah} ({rata_mapel.min():.2f})\n")

# =========================
# BUAT SUBPLOTS (4 Diagram)
# =========================
fig = make_subplots(
    rows=2, cols=2,
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "domain"}, {"type": "xy"}]
    ],
    subplot_titles=(
        "Rata-Rata Nilai per Mapel",
        "Sebaran Nilai per Mapel",
        "Persentase Nilai per Mapel",
        "Tren Nilai (dengan Garis Bantu)"
    )
)

# 1️⃣ Bar Chart
fig.add_trace(
    go.Bar(
        x=rata_mapel.index,
        y=rata_mapel.values,
        marker=dict(color=rata_mapel.values, colorscale="Viridis"),
        text=[f"{v:.1f}" for v in rata_mapel.values],
        textposition="auto",
        name="Rata-rata"
    ),
    row=1, col=1
)

# 2️⃣ Boxplot
fig.add_trace(
    go.Box(
        y=data[kolom_nilai],
        x=data[kolom_mapel],
        boxmean='sd',
        marker_color='teal',
        name="Sebaran Nilai"
    ),
    row=1, col=2
)

# 3️⃣ Pie Chart
fig.add_trace(
    go.Pie(
        labels=rata_mapel.index,
        values=rata_mapel.values,
        pull=[0.05]*len(rata_mapel),
        textinfo="label+percent",
        name="Persentase Nilai"
    ),
    row=2, col=1
)

# 4️⃣ Line Chart (Tren Nilai)
if kolom_nama:
    for nama in data[kolom_nama].unique():
        subset = data[data[kolom_nama] == nama]
        fig.add_trace(
            go.Scatter(
                x=subset[kolom_mapel],
                y=subset[kolom_nilai],
                mode="lines+markers",
                line=dict(width=2, color="darkgreen"),
                marker=dict(size=8, symbol="circle", line=dict(width=1, color="black")),
                name=nama,
                visible=(nama == data[kolom_nama].unique()[0])  # hanya siswa pertama aktif default
            ),
            row=2, col=2
        )

# =========================
# DROPDOWN MENU
# =========================
unique_mapel = sorted(data[kolom_mapel].unique())
unique_siswa = sorted(data[kolom_nama].unique()) if kolom_nama else []

# Dropdown Mapel
mapel_buttons = [
    dict(
        label=m,
        method="update",
        args=[
            {"visible": [True, True, True] + [True] * len(unique_siswa)},
            {"title": f"Analisis Nilai Siswa - Mapel: {m}"}
        ]
    )
    for m in unique_mapel
]

# Dropdown Siswa
siswa_buttons = []
if kolom_nama:
    for s in unique_siswa:
        visible = [True, True, True] + [nama == s for nama in unique_siswa]
        siswa_buttons.append(
            dict(
                label=s,
                method="update",
                args=[
                    {"visible": visible},
                    {"title": f"Analisis Nilai Siswa - Nama: {s}"}
                ]
            )
        )

# =========================
# TATA LETAK
# =========================
fig.update_layout(
    title="Analisis Nilai Siswa Interaktif (Mapel & Siswa)",
    template="plotly_white",
    height=850,
    showlegend=False,
    font=dict(size=11),
    margin=dict(l=60, r=20, t=80, b=60),
    updatemenus=[
        dict(
            buttons=mapel_buttons,
            direction="down",
            x=1.05, xanchor="left", y=1, yanchor="top",
            bgcolor="white", bordercolor="gray", borderwidth=1,
            showactive=True
        ),
        dict(
            buttons=siswa_buttons,
            direction="down",
            x=1.05, xanchor="left", y=0.85, yanchor="top",
            bgcolor="white", bordercolor="gray", borderwidth=1,
            showactive=True
        )
    ],
    annotations=[
        dict(
            text="Klik kanan grafik > Save as PNG untuk menyimpan gambar.",
            xref="paper", yref="paper",
            x=0.5, y=-0.08, showarrow=False, font=dict(size=10, color="gray")
        )
    ]
)

# Garis bantu & grid
fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor="lightgray")
fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor="lightgray")

# =========================
# SIMPAN OTOMATIS
# =========================
plot(fig, filename='analisis_nilai_siswa.html', auto_open=True)
try:
    fig.write_image("analisis_nilai_siswa.png")
except Exception:
    print("⚠️ Gagal simpan PNG — pastikan 'kaleido' sudah diinstal (pip install kaleido)")

# =========================
# ANALISIS & PERTANYAAN
# =========================
print("\n=== ANALISIS DAN PERTANYAAN ===")
print("1. Mapel mana yang memiliki rata-rata nilai tertinggi?")
print(f"   Jawaban: {mapel_tertinggi} ({rata_mapel.max():.2f})")
print()
print("2. Mapel mana yang memiliki rata-rata nilai terendah?")
print(f"   Jawaban: {mapel_terendah} ({rata_mapel.min():.2f})")
print()
print("3. Bagaimana visualisasi membantu dalam memahami data?")
print("   Jawaban: Visualisasi membantu kita memahami data lebih cepat dan mudah.")
print("   Garis bantu, warna, serta dropdown interaktif mempermudah membandingkan antar siswa dan mata pelajaran.")
print("   Diagram batang dan pie chart memperlihatkan perbandingan, boxplot menunjukkan variasi,")
print("   dan grafik garis memperjelas perkembangan nilai setiap siswa.")
print()
print("4. File laporan otomatis disimpan sebagai:")
print("   - analisis_nilai_siswa.html (interaktif)")
print("   - analisis_nilai_siswa.png (gambar statis)")
print("   Silakan buka file HTML untuk eksplorasi lebih lanjut.")