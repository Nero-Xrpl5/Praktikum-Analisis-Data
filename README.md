# 📊 Analisis Nilai Siswa Interaktif

Project ini dibuat oleh **Dinero Sulung S. (Absen 09)**  
**SMK Telkom Malang**  

---

## 🧠 Deskripsi Proyek

Proyek ini merupakan analisis data nilai siswa yang divisualisasikan secara **interaktif** menggunakan **Plotly (Python)**.  
Tujuannya adalah untuk membantu memahami data nilai siswa dengan lebih cepat, mudah, dan menarik secara visual.

Melalui visualisasi ini, pengguna dapat melihat:
- Rata-rata nilai tiap mata pelajaran
- Sebaran nilai siswa di setiap mapel
- Persentase rata-rata nilai antar mapel
- Tren perkembangan nilai siswa dari waktu ke waktu  

Proyek ini sangat cocok untuk digunakan dalam **praktikum analisis data** maupun **projek pembelajaran informatika/data science di SMK**.

---

## ⚙️ Fitur Utama

✅ **4 Diagram Analisis Utama (terbuka bersamaan)**
1. **Bar Chart** – Menampilkan rata-rata nilai setiap mapel  
2. **Box Plot** – Menunjukkan variasi/sebaran nilai siswa per mapel  
3. **Pie Chart** – Memperlihatkan persentase nilai rata-rata antar mapel  
4. **Line Chart (Tren Nilai)** – Memperlihatkan perkembangan nilai siswa dengan garis bantu di setiap titik

✅ **Fitur Interaktif**
- Dropdown untuk memilih **Mapel**
- Dropdown untuk memilih **Nama Siswa**
- Garis bantu untuk mempermudah pembacaan tren
- Tooltip interaktif untuk setiap titik data

✅ **Analisis Otomatis**
- Menampilkan hasil pertanyaan analisis seperti:
  1. Mapel dengan nilai tertinggi  
  2. Mapel dengan nilai terendah  
  3. Penjelasan bagaimana visualisasi membantu memahami data  

✅ **Output Otomatis**
- Menyimpan hasil analisis dalam dua format:
  - `analisis_nilai_siswa.html` → visual interaktif  
  - `analisis_nilai_siswa.png` → versi gambar statis  

---

## 🗂️ Struktur Folder

📁 Analisis-Data-Projek
├── nilai_siswa.csv # Dataset nilai siswa
├── Praktikum_AnalisisData.py # Script utama
├── analisis_nilai_siswa.html # Output interaktif
├── analisis_nilai_siswa.png # Output gambar
└── README.md # Dokumentasi proyek ini

🚀 Cara Menjalankan Program

1. Simpan semua file (nilai_siswa.csv, Praktikum_AnalisisData.py, README.md) dalam satu folder.
2. Buka terminal atau command prompt di folder tersebut.
3. Jalankan perintah:
   **python Praktikum_AnalisisData.py**

File interaktif akan otomatis terbuka di browser (analisis_nilai_siswa.html).


📊 Contoh Pertanyaan Analisis
No	Pertanyaan	Jawaban Otomatis
1	Mapel mana yang memiliki rata-rata nilai tertinggi?	**Ditampilkan di terminal**
2	Mapel mana yang memiliki nilai terendah? **Ditampilkan di terminal**
3	Bagaimana visualisasi membantu memahami data? **Dijelaskan secara otomatis di output**


🧠 Manfaat Pembelajaran
Melalui proyek ini, siswa dapat belajar:

1. Dasar analisis data menggunakan Python
2. Visualisasi data interaktif dengan Plotly
3. Cara membuat laporan analisis otomatis
4. Penggunaan dropdown & layout grid interaktif


✍️ Identitas Pembuat
Keterangan	Data

 Nama	Dinero Sulung S.
Sekolah	SMK Telkom Malang
Kelas	(sesuaikan sendiri kalau mau ditambahkan)
Absen	09
Proyek	Analisis Nilai Siswa Interaktif dengan Python
💡 Kesimpulan

Visualisasi data membantu siswa dan guru untuk:

Melihat perbandingan antar mapel dengan cepat

Mengenali siswa dengan tren nilai bagus atau menurun

Menemukan pelajaran yang perlu perhatian lebih

Memahami data secara visual tanpa membaca angka satu per satu

🖼️ Ilustrasi Output

Berikut tampilan contoh hasil grafik analisis:

📚 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan praktikum analisis data di SMK.
Diperbolehkan digunakan dan dimodifikasi untuk keperluan edukasi dengan mencantumkan nama pembuat asli.

💬 “Data bukan hanya angka — tapi cerita yang bisa kamu pahami dengan visualisasi.”
— Dinero Sulung S., SMK Telkom Malang




