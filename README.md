# Tugas-PCD

# Image Restoration using Mean Filter

## 📌 Deskripsi
Proyek ini mengimplementasikan teknik **image restoration** menggunakan **mean filter** untuk mengurangi noise Gaussian pada citra digital. Program dibuat menggunakan Python dengan library ImageIO, NumPy, dan Matplotlib.

## 🧪 Tahapan Proses
1. Membaca citra input
2. Konversi citra ke grayscale
3. Penambahan noise Gaussian
4. Restorasi citra menggunakan mean filter 3×3
5. Visualisasi hasil

## 📂 Struktur Folder
image-restoration-mean-filter/

├── restoration.py

├── gambar.png

├── requirements.txt

└── README.md


## ▶️ Cara Menjalankan Program
1. Install library:
   pip install -r requirements.txt
2. Jalankan program:
   python restoration.py

   ## 📊 Output
Program akan menampilkan:
- Citra Asli
- Citra dengan Noise
- Citra Setelah Restorasi

## 📈 Analisa Singkat
Mean filter efektif dalam mengurangi noise Gaussian, namun menyebabkan efek blur pada citra sehingga detail tepi sedikit berkurang.

## 🧑‍🎓 Catatan Akademik
Proyek ini dibuat untuk keperluan pembelajaran mata kuliah **Pengolahan Citra Digital**.

PENJELASAN KODE PROGRAM (BERDASARKAN BAGIAN)
1. Import Library:

Program menggunakan tiga pustaka utama: ImageIO untuk membaca file citra, NumPy untuk manipulasi dan perhitungan numerik pada matriks piksel, serta Matplotlib untuk visualisasi hasil citra. Ketiga pustaka ini merupakan standar dalam pengolahan citra digital berbasis Python.

2. Pembacaan dan Pra-pemrosesan Citra:

Citra input dibaca dari file lokal dan disimpan dalam bentuk array numerik. Jika citra yang dibaca merupakan citra berwarna (RGB), maka dilakukan konversi ke grayscale dengan menghitung nilai rata-rata dari setiap kanal warna. Selanjutnya, tipe data citra diubah ke format float agar aman digunakan dalam operasi matematika seperti penambahan noise dan filtering.

3. Penambahan Noise:

Pada tahap ini, noise Gaussian ditambahkan ke citra untuk mensimulasikan kondisi citra rusak. Noise dibuat dengan nilai rata-rata nol dan standar deviasi tertentu sehingga distribusinya bersifat acak namun terkontrol. Setelah noise ditambahkan, nilai piksel dibatasi agar tetap berada pada rentang valid citra digital, yaitu 0 hingga 255.

4. Proses Image Restoration:

Image restoration dilakukan menggunakan metode mean filter dengan ukuran kernel 3×3. Setiap piksel pada citra ternoise diganti dengan nilai rata-rata dari piksel-piksel di sekitarnya. Proses ini bertujuan untuk mereduksi noise dengan cara meratakan fluktuasi nilai piksel, sehingga citra menjadi lebih halus.

5. Visualisasi Hasil:

Hasil pemrosesan divisualisasikan dalam satu tampilan yang terdiri dari tiga citra, yaitu citra asli, citra dengan noise, dan citra setelah restorasi. Visualisasi ini memudahkan perbandingan kualitas citra sebelum dan sesudah proses restorasi.

**ANALISA MENYELURUH PROGRAM**:

Jenis dan Pendekatan Image Restoration
Program ini menggunakan pendekatan spatial domain image restoration, di mana perbaikan citra dilakukan langsung pada nilai piksel. Metode mean filter dipilih karena sederhana dan efektif untuk mengurangi noise Gaussian dengan intensitas ringan hingga sedang.

**Kinerja dan Efektivitas**:

Mean filter mampu menurunkan tingkat noise secara signifikan, namun efek samping yang muncul adalah penurunan ketajaman citra. Hal ini terjadi karena proses perataan nilai piksel juga mempengaruhi tepi dan detail objek.

**Kelebihan Metode**:

Metode yang digunakan mudah dipahami dan diimplementasikan, tidak memerlukan pustaka tambahan yang kompleks, serta cocok untuk pembelajaran dasar pengolahan citra digital. Program ini juga fleksibel karena dapat digunakan untuk berbagai jenis citra grayscale.

**Keterbatasan Metode**:

Penggunaan mean filter menyebabkan efek blur dan kurang optimal untuk menangani noise impuls seperti salt-and-pepper noise. Selain itu, penggunaan perulangan bersarang membuat performa menurun ketika ukuran citra terlalu besar.

**Relevansi Akademik**:

Program ini sesuai dengan konsep dasar image restoration dalam mata kuliah Pengolahan Citra Digital dan dapat dijadikan contoh implementasi praktis dari teori filtering spasial. Struktur kode dan alur pemrosesan juga telah memenuhi standar dokumentasi untuk laporan dan repository GitHub.

**KESIMPULAN**


Program image restoration ini berhasil mengimplementasikan metode mean filter untuk mengurangi noise Gaussian pada citra digital. Meskipun efektif dalam mereduksi noise, metode ini memiliki keterbatasan berupa penurunan ketajaman citra. Oleh karena itu, pemilihan metode restorasi harus disesuaikan dengan jenis noise dan kebutuhan kualitas citra.
