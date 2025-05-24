# Laporan Proyek Machine Learning - Dewi Puspita

## Domain Proyek

### Latar Belakang
Pendidikan tinggi memiliki peran penting dalam membentuk masa depan individu dan masyarakat. Namun, pencapaian akademik mahasiswa tidak hanya ditentukan oleh kurikulum formal, melainkan juga oleh faktor-faktor eksternal seperti kebiasaan belajar, durasi penggunaan media sosial, kualitas tidur, kondisi kesehatan mental, dan partisipasi ekstrakurikuler. Pemahaman yang baik terhadap pengaruh variabel-variabel ini dapat membantu institusi pendidikan merancang intervensi yang tepat untuk mendukung performa mahasiswa.

Berbagai penelitian telah menunjukkan bahwa kebiasaan hidup sehat dan pola belajar yang baik secara signifikan berhubungan dengan capaian akademik yang lebih tinggi. Misalnya, durasi belajar yang konsisten (Mackenzie et al., 2021)[https://doi.org/10.1007/s10639-021-10401-x], partisipasi dalam kegiatan fisik (Aguilar-Martínez et al., 2024)[https://doi.org/10.1057/s41599-025-04630-4], serta kualitas tidur dan kesehatan mental (Yusof et al., 2020)[https://doi.org/10.6007/IJARBSS/v10-i5/7326] berkorelasi positif terhadap skor ujian.

Dengan perkembangan teknologi dan tersedianya dataset pendidikan yang kaya, pendekatan berbasis machine learning dapat digunakan untuk membangun model prediktif performa akademik. Model seperti ini tidak hanya meningkatkan efisiensi proses identifikasi risiko, tetapi juga membantu pengambilan keputusan berbasis data di lingkungan pendidikan.

### Urgensi dan Tujuan Proyek
Proyek ini bertujuan untuk membangun model regresi guna memprediksi exam score mahasiswa berdasarkan fitur-fitur kebiasaan harian dan gaya hidup dalam dataset “Student Habits vs Academic Performance” (Kaggle). Model ini diharapkan dapat:
- Memberikan insight terhadap variabel-variabel yang paling berpengaruh terhadap hasil ujian mahasiswa.
- Membantu pihak akademik dalam melakukan deteksi dini terhadap mahasiswa dengan risiko performa rendah.
- Menjadi dasar bagi intervensi akademik atau pengembangan program peningkatan performa berbasis data.

## Business Understanding
### Problem Statement
- Performa akademik (nilai ujian) tidak hanya dipengaruhi oleh kecerdasan akademik semata, tetapi juga oleh berbagai faktor eksternal yang kompleks.
- Kurangnya pemahaman dan alat untuk memprediksi pengaruh faktor-faktor ini membuat intervensi pendidikan menjadi kurang efektif.
- Diperlukan pendekatan prediktif berbasis data untuk menghubungkan gaya hidup siswa dengan performa akademiknya.

### Goals
- Mengembangkan model regresi untuk memprediksi nilai ujian siswa berdasarkan data gaya hidup, kebiasaan belajar, dan kondisi psikologis.
- Memberikan estimasi performa akademik yang akurat sebagai dasar pengambilan keputusan oleh institusi pendidikan.
- Mendukung strategi intervensi berbasis data untuk meningkatkan capaian akademik siswa.

### Solution Statements
Solution statements dilakukan dengan mengimplementasikan 3 algoritma dalam permodelan, yakni:
- **K-Nearest Neighbors (KNN)**: Memberikan gambaran awal mengenai prediksi menggunakan pendekatan berbasis kedekatan data.
- **Random Forest Regressor**: Cocok untuk menangani banyak fitur dan interaksi non-linear antar variabel, serta stabil dalam performa dan mampu mengurangi overfitting melalui teknik ensemble (bagging).
- **AdaBoost Regressor**: Menggunakan pendekatan boosting adaptif untuk meningkatkan akurasi secara bertahap dari kesalahan model sebelumnya. Efektif untuk meningkatkan performa regresi pada dataset dengan noise rendah hingga sedang dan memiliki kemampuan fokus pada observasi yang sulit diprediksi, sehingga dapat meningkatkan presisi model.

### Evaluation Metric
- **Mean Squared Error (MSE)** dipilih sebagai metrik evaluasi utama karena memberikan penalti lebih besar pada kesalahan prediksi yang besar dan cocok unutk konteks regresi di mana kesalahan jauh dari nilai sebenarnya perlu diminimalkan.
- Evaluasi MSE dilakukan pada data validasi dan testing untuk membandingkan performa antar model.

## Data Understanding
Pada proyek ini, dataset yang digunakan berasal dari **Kaggle** dengan judul **"Student Exam Performance Prediction"**, yang dapat diunduh melalui tautan berikut:
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance

Dataset ini berisi informasi mengenai berbagai faktor gaya hidup, psikologis, dan kebiasaan belajar mahasiswa yang diasumsikan mempengaruhi performa akademik mereka, khususnya nilai ujian. Data ini terdiri dari 1000 baris data (entri( dan 15 kolom fitur (variabel), dengan satu variabel target yaitu "**exam_score**".

### Tahapan Data Understanding:
1. Data Loading
   
Langkah awal dilakukan dengan memuat dataset ke dalam lingkungan analisis menggunakan library Python seperti `pandas `. Proses ini bertujuan untuk melihat struktur awal data, memastikan dataset terbaca dengan benar, dan mengidentifikasi tipe data setiap kolom.
3. EDA - Deskripsi Variabel

|Fitur      |Tujuan                              |Tipe Data |
|-----------|-----------------------------------|-----------|
|student_id |ID unik siswa (tidak penting untuk analisis; dapat dianonimkan) |object |
|age |Usia dalam tahun |int64 |
|gender |Jenis kelamin |object |
|study_hours_per_day |Rata-rata lama belajar per hari |float64 |
|social_media_hours |Rata-rata lama bermain sosial media per hari|float64 |
|netflix_hours |Rata-rata lama menonton netflix per hari |float64 |
|part_time_job |Apakah memiliki pekerjaan sebagai part time atau tidak |object |
|attendance_percentage |Persentase kehadiran kelas (0-100%) |float64 |
|sleep_hours |Rata-rata lama tidur harian |float64 |
|diet_quality |Kualitas makanan sehari-hari (Poor/Fair/Good) |object |
|exercise_frequency |Berapa kali berolahraga dalam seminggu|int64 |
|parental_education_level|Tingkat edukasi orang tua|object |
|internet_quality|Kualitas internet|object |
|mental_health_rating |Nilai kesehatan mental dari skala 1-10|int64 |
|extracurricular_participation|Apakah mengikuti ekstrakulikuler atau tidak|object |
|exam_score (target)|Nilai ujian|float64 |

3. EDA - Menangani Missing Value dan Outliers

- **Missing Value**: Hasil pengecekan menunjukkan bahwa dataset mengandung 91 missing value pada `parental_education_level` sehingga dilakukan `dropna()` untuk memangkas data tersebut.
- **Outliers**: Deteksi dilakukan pada fitur numerik menggunakan boxplot dan metode IQR. Outlier ditemukan pada fitur seperti `study_hours_per_day`, `sosial_media_hours`, `netflix_hours`, `attendance_percentage`, dan `sleep_hours`. Setelah data yang berada pada outlier dipangkas, maka dataset tersisa 894 sampel.

4. EDA - Univariate Analysis

Analisis univariat dilakukan untuk memahami karakteristik distribusi masing-masing variabel, baik numerikal maupun kategorikal, secara individu. Hal ini bertujuan untuk melihat pola umum dan serta distribusi frekuensi dari tiap fitur.

**Fitur Kategorikal**:
- gender: Distribusi gender cukup merata antara pria dan wanita, dengan sejumlah kecil responden mengidentifikasi sebagai `Other`. Ini menunjukkan representasi gender yang relatif seimbang.
- part_time_job: Mayoritas responden tidak memiliki pekerjaan paruh waktu, menandakan bahwa sebagian besar individu lebih fokus pada studi penuh waktu atau aktivitas non-kerja lainnya.
- diet_quality: Sebagian besar responden menilai kualitas makanan mereka berada pada kategori Fair dan Good, sementara hanya sebagian kecil yang berada di kategori Poor. Hal ini mencerminkan kondisi gizi dan kebiasaan makan yang relatif baik.
- parental_education_level: Tingkat pendidikan orang tua didominasi oleh kategori High School dan Bachelor, diikuti oleh Master. Ini menunjukkan latar belakang pendidikan yang cukup bervariasi dan umumnya berada di tingkat menengah ke atas.
- internet_quality: Responden umumnya melaporkan kualitas internet yang Good atau Average, dengan lebih sedikit yang mengalami kualitas Poor, yang berarti mayoritas memiliki akses internet yang memadai.
- extracurricular_activities: Lebih dari dua kali lipat jumlah responden tidak berpartisipasi dalam kegiatan ekstrakurikuler dibandingkan yang berpartisipasi. Ini mengindikasikan bahwa kegiatan ekstrakurikuler masih belum menjadi kebiasaan umum di kalangan populasi responden.

**Fitur Numerik**:
- age: Distribusinya cenderung normal atau sedikit skewed, tergantung pada kelompok usia yang mendominasi (misalnya siswa sekolah atau mahasiswa).
- netflix_hours: Distribusi miring ke kanan (right-skewed), menunjukkan sebagian besar responden menonton dalam jumlah sedang, dengan segelintir yang menonton dalam durasi ekstrem.
- exercise_frequency: Distribusi bisa bimodal (kelompok yang rutin dan yang jarang berolahraga), atau miring ke kiri jika mayoritas responden aktif berolahraga.
- attendance_percentage: Distribusi umumnya tinggi, menunjukkan bahwa sebagian besar responden memiliki tingkat kehadiran yang baik, dan cenderung miring ke kiri.
- mental_health_rating: Sebagian besar responden melaporkan kesehatan mental yang baik.
- social_media_hours: Distribusi miring ke kanan, dengan mayoritas menggunakan media sosial dalam jumlah sedang, tetapi ada outlier yang menghabiskan waktu berlebihan di media sosial.
- sleep_hours: Distribusinya mendekati normal, berkisar antara 6–9 jam per hari, sesuai dengan kebiasaan tidur sehat.
- exam_score (target): Distribusi nilai ujian menunjukkan pola yang relatif normal, meskipun terdapat kemungkinan sedikit skewed ke kiri jika mayoritas memiliki nilai tinggi, atau bimodal jika terdapat gap performa antara dua kelompok besar.

5. EDA - Multivariate Analysis
6. 
Analisis ini mengeksplorasi hubungan antar fitur, khususnya terhadap variabel target `exam_score`:

- Bar Plot
- Pair Plot
- Matrix Correlation
[image](https://github.com/user-attachments/assets/222e2a02-c44d-48c7-ba89-38d0892b6c54)

## Referensi
Aguilar-Martínez, A., Monteiro, A. M., & Pons-Salvador, G. (2024). Physical activity and academic performance: The mediating effect of cognitive engagement in university students. Humanities and Social Sciences Communications, 11(1). https://doi.org/10.1057/s41599-025-04630-4

Mackenzie, K., Perkins, S. J., & Chapman, D. (2021). Predicting students’ academic performance using machine learning: A systematic review. Education and Information Technologies, 26, 3937–3965. https://doi.org/10.1007/s10639-021-10401-x

Yusof, S. N. M., Rahim, S. S. S. A., & Hassan, S. A. (2020). The relationship between sleeping habits and academic performance among university students. International Journal of Academic Research in Business and Social Sciences, 10(5), 911–921. https://doi.org/10.6007/IJARBSS/v10-i5/7326

Rodriguez, I. A., & Cruz, M. R. (2023). Predictive modeling of student academic performance using regression techniques. Journal of Educational Computing Research, 61(4), 894–915. https://doi.org/10.1177/07356331221134589




### Permasalahan
Penilaian kualitas wine yang subjektif dapat menyebabkan inkonsistensi dalam evaluasi, yang berdampak pada kepercayaan konsumen dan efisiensi produksi. Oleh karena itu, diperlukan sistem prediksi yang dapat memberikan hasil yang konsisten dan dapat diandalkan.

### Tujuan Proyek
Proyek ini bertujuan untuk membangun model machine learning yang dapat memprediksi apakah sebuah wine memiliki kualitas baik atau tidak, berdasarkan parameter kimiawi yang tersedia. Model ini diharapkan dapat membantu produsen dalam mengontrol kualitas produk secara lebih efisien dan objektif (Zaza et al., 2023).

### Algoritma yang Digunakan
Dalam proyek ini, pendekatan supervised learning digunakan dengan menerapkan beberapa algoritma, yaitu
- Random Forest
- KNN
- SVC
- Extra Trees
- LightGBM

## Business Understanding

### Problem Statements
- Bagaimana cara meminimalkan ketergantungan terhadap penilaian subjektif dari ahli pencicip wine dalam menilai kualitas wine?
- Apa saja fitur kimiawi yang paling berpengaruh dalam menentukan kualitas wine dan bagaimana menggunakannya untuk membuat prediksi yang akurat?
- Algoritma machine learning mana yang paling optimal dalam memprediksi kualitas wine berdasarkan data yang tersedia?

### Goals
- Mengembangkan sistem prediksi kualitas wine yang objektif dan akurat menggunakan data kimia dari wine.
- Mengidentifikasi fitur kimia yang paling berpengaruh terhadap kualitas wine dan menyederhanakan model tanpa mengorbankan akurasi.
- Membandingkan beberapa algoritma machine learning untuk menentukan model terbaik.

### Solution statements
- Menggunakan beberapa algoritma machine learning seperti Random Forest, KNN, SVM, Extra Trees, dan LightGBM untuk membangun model klasifikasi kualitas wine.
- Melakukan pemilihan fitur berdasarkan korelasi dan importance score.
- Melakukan penyetelan hiperparameter pada model terbaik untuk mencapai performa optimal.
- Evaluasi model dilakukan menggunakan metrik akurasi, precision, recall, dan F1-score.
  
## Data Understanding
### Dataset
Dataset yang digunakan berasal dari UCI Machine Learning Repository, tersedia di Kaggle (Cortez et al., 2009). Dataset ini terdiri dari 1.599 sampel wine merah dengan 11 fitur kimia, seperti kadar alkohol, keasaman, dan sulfur dioksida.

Link dataset: https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

### Fitur-Fitur Dataset
|Fitur              |Deskripsi                                   |
|-------------------|--------------------------------------------|
|fixed acidity |Konsentrasi asam tetap (tidak menguap) seperti tartaric acid.|
|volatile acidity |Konsentrasi asam yang mudah menguap seperti asam asetat.|
|citric acid |Asam sitrat, memberi rasa segar dan membantu stabilisasi wine.|
|residual sugar |Gula yang tersisa setelah fermentasi (g/I). |
|chlorides |Konsentrasi garam (natrium klorida). |
|free sulfur dioxide |SO₂ bebas untuk mencegah mikroba dan oksidasi. |
|total sulfur dioxide |Total SO₂ bebas dan terikat.|
|density |Kepadatan wine, berkorelasi dengan kadar alkohol dan gula.|
|pH |Keasaman wine, skala logaritmik.|
|sulphates|Aditif yang meningkatkan stabilitas dan daya simpan.|
|alcohol|Persentase alkohol dalam wine|
|quality (Target) |Skor kualitas wine (integer 3-8) yang dinilai oleh pencicip.|

### EDA - Univariate Analysis
~ Image
Gambar 1. Analisis Univariat (Data Numerik)

[Berdasarkan Gambar 1. (Deskripsi)

### EDA - Multivariate Analysis
~ Image
Gambar 2. Analisis Multivariat

~ Image
Gambar 3. Analisis Matriks Korelasi

[Berdasarkan gambar 2.............. gambar 3...........]


## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja



Referensi Terkait
Berikut adalah beberapa referensi yang mendukung pendekatan dan pemilihan fitur dalam proyek ini:

Xu, B. (2024). Mengoptimalkan Prediksi Kualitas Anggur Merah: Dampak Pemilihan Fitur dan Evaluasi Model. Kemajuan dalam Ekonomi, Manajemen dan

Arshad, H. (2024). Prediksi Kualitas Anggur Menggunakan Machine Learning. Jurnal Komputasi Inovatif dan Teknologi Muncul, 4(2). Tautan

Zaza, S., Atemkeng, M., & Hamlomo, S. (2023). Prediksi pentingnya dan kualitas fitur anggur: Studi komparatif algoritme pembelajaran mesin dengan data yang tidak seimbang

Fabiyanto, D., & Rianto, Y. (2024). Evaluasi Kinerja Beberapa Model Pembelajaran Mendalam untuk Prediksi Kualitas Anggur

Dahal, KR, Dahal, JN, Banjade, H., & Gaire, S. (2021). Prediksi Kualitas Anggur Menggunakan Algoritma Pembelajaran Mesin

Pada bagian ini, kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.


