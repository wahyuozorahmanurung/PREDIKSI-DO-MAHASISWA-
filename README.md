# PREDIKSI-DO-MAHASISWA-
UAS DATA MINING

# SISTEM PREDIKSI DROP OUT MAHASISWA
#### Kelompok 1:
#### - Damianus Christopher Samosir (G1A022028)
#### - Torang Four Yones Manullang (G1A022052)
#### - Wahyu Ozorah Manurung (G1A022060)

#### Link Streamlit/Dashboard: [Sistem Prediksi Drop Out](https://prediksidokelompok1.streamlit.app/)

## Project Overview

### Latar Belakang

Dalam dunia pendidikan tinggi, permasalahan mahasiswa yang mengalami drop out (DO) menjadi perhatian serius bagi institusi akademik. Drop out tidak hanya mencerminkan kegagalan individu dalam menyelesaikan studi, tetapi juga menunjukkan potensi kerugian bagi institusi dari sisi reputasi, efisiensi anggaran, serta kualitas lulusan. Oleh karena itu, penting bagi institusi untuk memiliki sistem prediksi yang mampu mengidentifikasi mahasiswa berisiko tinggi sebelum mereka benar-benar keluar dari sistem pendidikan. Prediksi yang akurat memungkinkan pihak kampus untuk memberikan intervensi tepat waktu melalui program bimbingan, konseling, atau bantuan finansial (Bowers & Sprott, 2012).

Dalam penelitian ini, pendekatan semi-supervised learning digunakan sebagai solusi terhadap keterbatasan label (ground truth) DO pada data historis mahasiswa. Strategi ini dimulai dengan proses clustering menggunakan K-Means, di mana mahasiswa dikelompokkan berdasarkan fitur-fitur seperti IPK, kehadiran, dan faktor akademik lainnya untuk membedakan antara kelompok yang berisiko tinggi dan rendah. Hasil dari proses clustering ini kemudian digunakan sebagai label pseudo (pseudo-label) yang selanjutnya menjadi dasar pelatihan model klasifikasi. Dengan demikian, proses klasifikasi menggunakan Logistic Regression dapat dilakukan untuk memprediksi status risiko DO mahasiswa baru atau mahasiswa aktif lainnya yang belum diklasifikasikan (Chapelle et al., 200141).

Pemanfaatan kombinasi K-Means dan Logistic Regression ini memberikan fleksibilitas dalam membangun sistem prediksi meskipun dengan data label yang terbatas. K-Means sebagai teknik unsupervised membantu menemukan struktur alami dalam data, sedangkan Logistic Regression memberikan interpretasi yang jelas dan akurat terhadap peluang seorang mahasiswa masuk dalam kategori berisiko tinggi. Implementasi pendekatan ini sejalan dengan prinsip Educational Data Mining (EDM) yang bertujuan mendukung pengambilan keputusan berbasis data untuk meningkatkan kualitas dan efisiensi proses pendidikan (Baker & Siemens, 2014). Dengan sistem ini, institusi diharapkan dapat mengurangi angka DO secara signifikan melalui strategi preventif berbasis data.

### Referensi

Bowers, A. J., & Sprott, R. (2012). Why tenth graders fail to finish high school: Dropout predictors in a full-year cohort. Journal of Education for Students Placed at Risk (JESPAR), 17(3), 129-148.

Chapelle, O., Scholkopf, B., & Zien, A. (2006). Semi-Supervised Learning. MIT Press.

Baker, R. S. J. d., & Siemens, G. (2014). Educational Data Mining and Learning Analytics. In Cambridge Handbook of the Learning Sciences.

---

## Business Understanding
Masalah drop out (DO) mahasiswa merupakan tantangan serius dalam dunia pendidikan tinggi karena berdampak pada reputasi institusi, alokasi sumber daya, dan kualitas lulusan. Untuk menurunkan angka DO, institusi pendidikan perlu memahami pola-pola yang mengarah pada risiko mahasiswa keluar dari sistem akademik. Pemanfaatan pendekatan data-driven seperti data mining dan machine learning menjadi kunci dalam merancang sistem prediksi yang efektif, terutama ketika data label historis tidak tersedia secara lengkap. Dengan pendekatan semi-supervised learning, proses prediksi risiko DO dapat dibangun secara bertahap, dimulai dengan pengelompokan data tanpa label hingga menghasilkan model prediktif yang akurat.

### Problem Statements
- Bagaimana mengidentifikasi mahasiswa yang berisiko tinggi DO ketika data historis tidak sepenuhnya memiliki label risiko?
- Bagaimana memanfaatkan teknik unsupervised learning untuk membentuk kelompok mahasiswa berdasarkan karakteristik akademik mereka?
- Bagaimana mengembangkan model klasifikasi yang mampu memprediksi risiko DO berdasarkan hasil clustering awal tersebut?

### Goals
- Mengelompokkan mahasiswa menjadi dua kategori utama: risiko tinggi dan risiko rendah DO menggunakan metode K-Means berdasarkan fitur-fitur akademik seperti IPK, kehadiran, dan lain-lain.
- Menggunakan hasil clustering sebagai pseudo-label untuk membangun model klasifikasi prediktif menggunakan Logistic Regression.
- Mengembangkan pipeline prediksi risiko DO berbasis data yang dapat digunakan oleh institusi pendidikan untuk melakukan intervensi dini.

### Solution Statements
- **Clustering Mahasiswa dengan K-Means**: Menggunakan K-Means clustering untuk membagi mahasiswa ke dalam dua kelompok berdasarkan variabel akademik yang relevan. Cluster yang menunjukkan karakteristik negatif seperti IPK rendah dan kehadiran buruk ditetapkan sebagai kelompok risiko tinggi.
- **Klasifikasi Risiko dengan Logistic Regression**: Hasil dari proses clustering digunakan sebagai pseudo-label yang kemudian digunakan untuk melatih model Logistic Regression agar mampu memprediksi risiko DO pada mahasiswa baru atau data lain yang belum diklasifikasikan.
- **Penerapan Semi-Supervised Learning**: Mengintegrasikan metode unsupervised (K-Means) dan supervised (Logistic Regression) dalam pendekatan semi-supervised learning untuk mengatasi keterbatasan data berlabel dan tetap menghasilkan model prediksi yang efektif dan dapat dijelaskan (interpretable).

---

## DATA UNDERSTANDING

Proyek ini menggunakan dataset sintetis yang dirancang untuk memodelkan berbagai aspek akademik, perilaku, dan kondisi sosial ekonomi mahasiswa dalam konteks risiko putus studi (drop out/DO). Dataset ini digunakan sebagai dasar untuk membangun sistem prediksi mahasiswa berisiko tinggi menggunakan pendekatan semi-supervised learning, di mana tahap awal dilakukan clustering untuk mengelompokkan mahasiswa berisiko tinggi dan rendah, dan hasil cluster digunakan sebagai label dalam proses klasifikasi lanjutan.

Dataset mencerminkan data dari lebih dari 2.500 mahasiswa dengan berbagai indikator yang bers meditativeifat multidimensi, meliputi performa akademik (IPK tiap semester), kehadiran kuliah, perilaku retake, aktivitas daring, hingga status sosial ekonomi dan pekerjaan. Data ini dirancang untuk menggambarkan kondisi nyata di lingkungan pendidikan tinggi, di mana banyak faktor saling memengaruhi terhadap risiko mahasiswa untuk drop out.

- **Jumlah Data**  
  Jumlah Baris: >2.500 entri data mahasiswa.  
  Jumlah Kolom: 25 kolom fitur utama.  
  Jumlah Duplikat: Ditemukan 50 baris duplikat yang perlu dihapus dalam proses data cleaning.  
  Jumlah Missing Values: Hampir semua kolom memiliki 50–55 missing values, termasuk fitur-fitur penting seperti IPK, kehadiran, aktivitas online, dan status sosial ekonomi. Penanganan missing values akan menjadi langkah krusial dalam tahap data preparation.

### Variabel-variabel dalam dataset:
- **ipk_smt1 – ipk_smt8**: Menunjukkan IPK mahasiswa dari semester 1 hingga semester 8. Nilai ini mencerminkan performa akademik jangka panjang, dan fluktuasi nilai dapat menjadi indikator risiko DO.
- **kehadiran_mk1 – kehadiran_mk6**: Persentase kehadiran mahasiswa di 6 mata kuliah utama. Tingkat kehadiran yang rendah sering dikaitkan dengan keterlibatan akademik yang lemah, dan dapat menjadi sinyal peringatan dini terhadap risiko DO.
- **retake**: Menggambarkan jumlah mata kuliah yang harus diulang oleh mahasiswa. Fitur ini penting untuk mengidentifikasi kesulitan belajar yang berkelanjutan.
- **online_activity1 – online_activity6**: Indikator kuantitatif aktivitas mahasiswa di platform pembelajaran daring (LMS), seperti frekuensi login, pengumpulan tugas, interaksi di forum, dll. Aktivitas daring yang minim dapat mencerminkan disengagement terhadap proses pembelajaran.
- **status_pekerjaan dan beban_kerja**: Menunjukkan apakah mahasiswa bekerja dan berapa besar beban kerja mingguannya. Mahasiswa dengan tanggung jawab kerja tinggi sering mengalami tekanan waktu dan kesulitan dalam mempertahankan performa akademik.
- **sosial_ekonomi**: Kategori status sosial ekonomi mahasiswa (misalnya: rendah, menengah, tinggi). Faktor ekonomi memiliki pengaruh signifikan terhadap kelanjutan studi, baik secara langsung maupun tidak langsung.

---

## DATA PREPARATION

Proses persiapan data dilakukan untuk memastikan dataset siap digunakan dalam tahap modeling. Langkah-langkah yang dilakukan mencakup pembersihan data, penanganan missing values, transformasi data, dan normalisasi untuk mendukung performa optimal algoritma machine learning.

### 1. Data Cleaning
- **Penghapusan Duplikasi**: Terdapat sekitar 50 data duplikat yang dihapus untuk menjaga integritas data dan mencegah bias dalam analisis.
- **Penanganan Missing Values**: Missing values ditangani dengan pendekatan imputasi menggunakan nilai rata-rata (mean) untuk fitur numerik seperti IPK dan kehadiran, memastikan kelengkapan data tanpa mengorbankan distribusi aslinya.

### 2. Transformasi Data
- Fitur-fitur IPK per semester (`ipk_smt1` - `ipk_smt8`) dirata-ratakan menjadi satu kolom `ipk_rata2` untuk menyederhanakan analisis performa akademik mahasiswa.
- Demikian pula, kehadiran tiap mata kuliah (`kehadiran_mk1` - `kehadiran_mk6`) dikonsolidasikan menjadi `kehadiran_rata2` untuk menggambarkan tingkat keterlibatan mahasiswa secara keseluruhan.
- Fitur aktivitas pembelajaran daring (`online_activity1` - `online_activity6`) diringkas menjadi satu metrik `aktivitas_online` untuk mencerminkan tingkat keterlibatan mahasiswa dalam pembelajaran daring.

### 3. Normalisasi Data
- Semua fitur numerik dinormalisasi menggunakan **Min-Max Scaler** untuk menyesuaikan rentang nilai ke dalam skala [0, 1]. Langkah ini memastikan bahwa algoritma K-Means dan Logistic Regression dapat bekerja secara optimal tanpa dipengaruhi oleh perbedaan skala antar fitur.

### 4. One-Hot Encoding
- Kolom kategorikal seperti `status_pekerjaan` dan `sosial_ekonomi` diubah menjadi representasi numerik menggunakan **One-Hot Encoding** dengan `drop_first=True` untuk menghindari multicollinearity. Hal ini memastikan bahwa fitur kategorikal dapat digunakan dalam model machine learning tanpa menyebabkan masalah redundansi.

---

## MODELING

Proses modeling dalam proyek ini menggunakan pendekatan semi-supervised learning yang menggabungkan teknik clustering (unsupervised) dan klasifikasi (supervised) untuk membangun sistem prediksi risiko drop out (DO).

### 1. Clustering dengan K-Means
- **Pendekatan**: Model **K-Means** digunakan untuk mengelompokkan data menjadi dua cluster utama: **Cluster 0** (risiko rendah) dan **Cluster 1** (risiko tinggi).
- **Pemilihan Jumlah Cluster**: Jumlah cluster (`n_clusters=2`) dipilih berdasarkan tujuan segmentasi risiko, yaitu membedakan mahasiswa berisiko tinggi dan rendah.
- **Visualisasi**: Hasil clustering divisualisasikan menggunakan **PCA (Principal Component Analysis)** untuk merepresentasikan data dalam ruang 2 dimensi, memudahkan interpretasi pola kelompok.

### 2. Pembuatan Pseudo-Label
- Cluster yang memiliki karakteristik negatif, seperti IPK rendah, kehadiran buruk, dan aktivitas online minim, ditetapkan sebagai **pseudo-label DO** (drop out).
- Pseudo-label ini digunakan sebagai target sementara (label training) untuk melatih model klasifikasi pada tahap berikutnya.

### 3. Klasifikasi dengan Logistic Regression
- **Pendekatan**: Model **Logistic Regression** dilatih menggunakan data yang telah diberi pseudo-label dari hasil clustering. Data dibagi menjadi **80% training set** dan **20% testing set** untuk evaluasi.
- **Evaluasi Model**: Model dievaluasi menggunakan metode **hold-out** (pemisahan data train-test) dan **cross-validation** untuk memastikan keandalan dan generalisasi model.
- **Hasil**: Model menghasilkan probabilitas risiko yang dapat digunakan untuk memprediksi status risiko DO mahasiswa baru atau mahasiswa yang belum diklasifikasikan, mendukung intervensi dini oleh institusi.

### 4. Penyimpanan Model
- Model Logistic Regression disimpan dalam format `.pkl` (`logistic_regression_model.pkl`) untuk memungkinkan penggunaan ulang tanpa pelatihan ulang.
- Daftar nama fitur yang digunakan saat pelatihan disimpan dalam file `features.pkl` untuk menjamin konsistensi saat model dijalankan kembali, menjadikan pipeline machine learning lebih stabil dan siap untuk produksi.

---

## EVALUASI MODEL

Model Logistic Regression yang telah dilatih menunjukkan performa yang sangat baik dan stabil dalam memprediksi risiko drop out mahasiswa berdasarkan pseudo-label dari clustering K-Means. Berikut adalah hasil evaluasi model:

### 1. Akurasi Keseluruhan
- **Akurasi Training**: 92.2%  
- **Akurasi Testing**: 92.4%  
Akurasi yang sangat dekat antara data training dan testing menunjukkan bahwa model mampu mengeneralisasi dengan baik, tanpa indikasi **overfitting** (akurasi training jauh lebih tinggi dari testing) atau **underfitting** (akurasi rendah di kedua set data).

### 2. Evaluasi Per Kelas
Berdasarkan laporan klasifikasi, performa model untuk masing-masing kelas adalah sebagai berikut:
- **Kelas 0 (Risiko Rendah, Minoritas)**:  
  - **Precision**: 0.81  
  - **Recall**: 0.81  
  - **F1-Score**: 0.81  
  Model cukup baik dalam mengenali kelas minoritas (101 dari 500 sampel), meskipun performanya sedikit di bawah kelas mayoritas karena jumlah data yang lebih sedikit.
- **Kelas 1 (Risiko Tinggi, Mayoritas)**:  
  - **Precision**: 0.95  
  - **Recall**: 0.95  
  - **F1-Score**: 0.95  
  Model sangat akurat dan konsisten dalam mengenali kelas mayoritas (399 dari 500 sampel), menunjukkan kemampuan yang kuat dalam mendeteksi mahasiswa berisiko tinggi.

### 3. Rata-rata Skor
- **Macro Average**: 0.88  
Rata-rata performa antar kelas tanpa mempertimbangkan jumlah sampel masing-masing kelas, menunjukkan keseimbangan performa yang baik meskipun ada ketidakseimbangan kelas.
- **Weighted Average**: 0.92  
Skor ini mendekati akurasi keseluruhan karena lebih dipengaruhi oleh performa pada kelas mayoritas yang memiliki jumlah data lebih besar.

### 4. Confusion Matrix
Hasil confusion matrix menunjukkan distribusi prediksi sebagai berikut:
- **Kelas 0 (Risiko Rendah)**:  
  - **True Negative**: 82 data diprediksi benar.  
  - **False Positive**: 19 data diprediksi salah.
- **Kelas 1 (Risiko Tinggi)**:  
  - **True Positive**: 380 data diprediksi benar.  
  - **False Negative**: 19 data diprediksi salah.

**Analisis Confusion Matrix**:
- Kesalahan klasifikasi terjadi secara seimbang di kedua kelas (19 vs. 19), menunjukkan bahwa model tidak bias terhadap kelas mayoritas meskipun data tidak seimbang.
- Distribusi kesalahan yang merata ini mengindikasikan bahwa model memberikan perhatian yang cukup terhadap kelas minoritas, sehingga dapat diandalkan untuk mendeteksi mahasiswa berisiko rendah maupun tinggi.
- Total 461 prediksi benar (82 + 380) dari 500 sampel pada data testing menghasilkan akurasi 92.4%, konsisten dengan performa model.

![image](https://github.com/user-attachments/assets/1d817096-b6d2-4ed8-b587-9a2d1649898e)


### 5. Kesimpulan Evaluasi
- Model Logistic Regression menunjukkan performa yang sangat baik dengan akurasi tinggi dan generalisasi yang kuat, cocok untuk digunakan dalam sistem peringatan dini risiko drop out.
- Performa yang seimbang pada kedua kelas, meskipun ada ketidakseimbangan jumlah data, menunjukkan bahwa model efektif dalam menangani data dengan distribusi kelas yang tidak merata.
- Hasil ini mendukung tujuan proyek untuk mengidentifikasi mahasiswa berisiko tinggi secara akurat, memungkinkan institusi untuk menerapkan intervensi dini dengan lebih tepat sasaran.

---
