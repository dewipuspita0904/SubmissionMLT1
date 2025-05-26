# Laporan Proyek Machine Learning - Dewi Puspita
![exam_score](https://agentrealestateschools.com/wp-content/uploads/2021/11/passing-score-for-real-estate-exam.jpg)

## Domain Proyek

### Latar Belakang
Pendidikan tinggi memiliki peran penting dalam membentuk masa depan individu dan masyarakat. Namun, pencapaian akademik mahasiswa tidak hanya ditentukan oleh kurikulum formal, melainkan juga oleh faktor-faktor eksternal seperti kebiasaan belajar, durasi penggunaan media sosial, kondisi kesehatan mental, dan jam belajar per hari. Pemahaman yang baik terhadap pengaruh variabel-variabel ini dapat membantu institusi pendidikan merancang intervensi yang tepat untuk mendukung performa mahasiswa.

Berbagai penelitian telah menunjukkan bahwa kebiasaan hidup sehat dan pola belajar yang baik secara signifikan berhubungan dengan capaian akademik yang lebih tinggi. Misalnya, durasi belajar yang konsisten, partisipasi dalam kegiatan fisik, serta kesehatan mental berkorelasi positif terhadap skor ujian [(Kayani, S. et al., 2024)](https://doi.org/10.3390/su10103633).

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
- **Random Forest Regressor**: Cocok untuk menangani banyak fitur dan interaksi non-linear antar variabel, serta stabil dalam performa dan mampu mengurangi overfitting melalui teknik ensemble (bagging).
- **AdaBoost Regressor**: Menggunakan pendekatan boosting adaptif untuk meningkatkan akurasi secara bertahap dari kesalahan model sebelumnya. Efektif untuk meningkatkan performa regresi pada dataset dengan noise rendah hingga sedang dan memiliki kemampuan fokus pada observasi yang sulit diprediksi, sehingga dapat meningkatkan presisi model.

### Evaluation Metric
- **Mean Squared Error (MSE)** dipilih sebagai metrik evaluasi utama karena memberikan penalti lebih besar pada kesalahan prediksi yang besar dan cocok unutk konteks regresi di mana kesalahan jauh dari nilai sebenarnya perlu diminimalkan.
- Evaluasi MSE dilakukan pada data validasi dan testing untuk membandingkan performa antar model.

## Data Understanding
Pada proyek ini, dataset yang digunakan berasal dari **Kaggle** dengan judul **"Student Exam Performance Prediction"**, yang dapat diunduh melalui tautan berikut:
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance

Dataset ini berisi informasi mengenai berbagai faktor gaya hidup, psikologis, dan kebiasaan belajar mahasiswa yang diasumsikan mempengaruhi performa akademik mereka, khususnya nilai ujian. Data ini terdiri dari 1000 baris data (entri) dan 15 kolom fitur (variabel), dengan satu variabel target yaitu "**exam_score**".

### Tahapan Data Understanding:
1. Data Loading
   
Langkah awal dilakukan dengan memuat dataset ke dalam lingkungan analisis menggunakan library Python seperti `pandas `. Proses ini bertujuan untuk melihat struktur awal data, memastikan dataset terbaca dengan benar, dan mengidentifikasi tipe data setiap kolom.


2. EDA - Deskripsi Variabel

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

3. EDA - Missing Value dan Outliers

- **Missing Value**: Hasil pengecekan menunjukkan bahwa dataset mengandung 91 missing value pada `parental_education_level`.
- **Outliers**: Deteksi dilakukan pada fitur numerik menggunakan boxplot dan metode IQR. Outlier ditemukan pada fitur seperti `study_hours_per_day`, `sosial_media_hours`, `netflix_hours`, `attendance_percentage`, dan `sleep_hours`.

4. EDA - Univariate Analysis

Analisis univariat dilakukan untuk memahami karakteristik distribusi masing-masing variabel, baik numerikal maupun kategorikal, secara individu. Hal ini bertujuan untuk melihat pola umum dan serta distribusi frekuensi dari tiap fitur.

**Fitur Kategorikal**:
- `gender`: Distribusi gender dalam dataset relatif seimbang antara laki-laki (47.7%) dan perempuan (48.1%), dengan sejumlah kecil responden mengidentifikasi sebagai Other (4.2%). Komposisi ini menunjukkan representasi gender yang cukup merata, meskipun kategori "Other" masih minoritas.
- `part_time_job`: Mayoritas responden tidak memiliki pekerjaan paruh waktu (78.5%), sementara hanya 21.5% yang bekerja paruh waktu. Ini mengindikasikan bahwa sebagian besar individu dalam populasi ini berfokus pada kegiatan lain seperti studi penuh waktu.
- `diet_quality`: Responden paling banyak menilai kualitas makanan mereka sebagai Fair (43.7%), disusul oleh Good (37.8%), dan Poor (18.5%). Ini menunjukkan bahwa mayoritas responden memiliki pola makan yang cukup baik, dengan sebagian kecil mengalami pola makan yang buruk.
- `parental_education_level`: Tingkat pendidikan orang tua paling banyak berada di kategori High School (43.1%), diikuti oleh Bachelor (38.5%) dan Master (18.4%). Komposisi ini menunjukkan latar belakang pendidikan orang tua yang umumnya menengah ke atas, namun masih didominasi oleh pendidikan sekolah menengah.
- `internet_quality`: Mayoritas responden menilai kualitas internet mereka sebagai Good (44.7%) dan Average (39.1%), dengan hanya 16.2% yang mengalami kualitas internet Poor. Hal ini menunjukkan bahwa sebagian besar responden memiliki akses internet yang cukup baik, yang dapat berpengaruh terhadap aktivitas belajar atau hiburan mereka.
- `extracurricular_activities`: Sebanyak 68.2% responden tidak mengikuti kegiatan ekstrakurikuler, sementara hanya 31.8% yang berpartisipasi. Ini menandakan bahwa partisipasi dalam kegiatan ekstrakurikuler masih belum umum di kalangan responden, yang mungkin dapat memengaruhi aspek pengembangan diri di luar akademik.

**Fitur Numerik**:
- `age`: Distribusi usia cukup merata antara 17 hingga 24 tahun, dengan sedikit lonjakan pada usia 20 dan 24 tahun. Ini menunjukkan bahwa responden berasal dari rentang usia mahasiswa atau remaja akhir.
- `atudy_hours_per_day`: Sebagian besar responden belajar antara 2 hingga 5 jam per hari, dengan puncak sekitar 3–4 jam. Distribusi agak right-skewed, artinya sedikit responden yang belajar lebih dari 6 jam per hari.
- `social_media_hours`: Distribusi waktu penggunaan media sosial cukup variatif, dengan puncak di sekitar 2–3 jam. Terlihat pola yang agak tidak teratur, tapi mayoritas masih menggunakan media sosial dalam rentang 1–4 jam per hari.
- `netflix_hours`: Sebagian besar responden menonton Netflix selama 1–2 jam per hari, dengan jumlah kecil yang menonton lebih dari 3 jam. Distribusi ini juga right-skewed, menunjukkan bahwa binge-watching bukan kebiasaan mayoritas.
- `attendance_percentage`: Sebagian besar responden memiliki persentase kehadiran tinggi, dengan konsentrasi kuat antara 85% hingga 100%. Hal ini menunjukkan tingkat kedisiplinan yang baik secara umum.
- `sleep_hours`: Distribusi jam tidur membentuk pola normal (bell-shaped) dengan puncak di 6 hingga 7 jam per hari. Artinya, sebagian besar responden tidur dalam durasi yang disarankan untuk dewasa muda.
- `exercise_frequency`: Distribusinya cukup merata antara 0 hingga 6 kali per minggu, menunjukkan kebiasaan olahraga yang beragam — dari yang tidak pernah hingga yang cukup rutin.
- `mental_health_rating`: Sebagian besar nilai mental health rating terdistribusi merata dari 1 sampai 10, yang bisa mengindikasikan persepsi kesehatan mental yang bervariasi, tanpa dominasi jelas.
- `exam_score` (target): Distribusi nilai ujian menyerupai bentuk normal, dengan puncak antara 60–70. Ini menunjukkan performa umum berada di tingkat sedang hingga baik.

5. EDA - Multivariate Analysis
**Fitur Kategorikal**:
- `gender`: Perempuan cenderung memiliki performa ujian yang lebih baik dibandingkan laki-laki. Bisa jadi karena perbedaan gaya belajar atau manajemen waktu.
- `part_time_job`: Bekerja sambil sekolah bisa mengganggu waktu belajar dan fokus sehingga berdampak negatif terhadap performa akademik.
- `diet_quality`: Pola makan tidak selalu berkorelasi langsung dengan performa akademik; bisa jadi siswa dengan diet `Fair` justru memiliki gaya hidup seimbang lainnya.
- `parental_education_level`: Hasil yang didapat tidak linear, bisa jadi memiliki faktor lain seperti dukungan emosional atau ekspektasi orang tua mungkin lebih berperan daripada tingkat pendidikan formal mereka.
- `internet_quality`: Koneksi internet yang terlalu baik mungkin mengarah pada distraksi online, sementara koneksi terlalu buruk menghambat akses belajar. Kualitas cukup bisa jadi ideal untuk menjaga fokus.
- `extracurricular_participation`: Fokus penuh pada akademik bisa meningkatkan nilai ujian, tetapi perlu ditimbang dengan keterampiral non-akademik yang dikembangkan lewat ekstrakurikuler.

**Fitur Numerik**:
|Fitur                |Korelasi dengan `exam_score`     |Kekuatan Korelasi        |Tipe         |Insight Penting         |
|---------------------|-----------|----------|-----------|---------------|
|`study_hours_per_day` |0,83       |Sangat kuat |Positif |Ini adalah faktor terkuat yang menentukan nilai ujian. Semakin banyak belajar, semakin tinggi skornya. |
|`mental_health_rating` |0,32 |Sedang/Lemah |Positif |Kesehatan mental yang baik cenderung mendukung performa belajar. |
|`exercise_frequency` |0,16 |Lemah |Positif |Olahraga mungkin membantu fokus/energi tapi tidak signifikan. |
|`sleep_hours` |0,11 |Lemah |Positif |Tidak cukup sedikit membantu hasil ujian. |
|`attendance_percentage` |0,09 |Lemah |Positif |Hadir di kelas penting, tapi tidak sekuat waktu belajar. |
|`netflix_hours` |-0,17 |Lemah |Negatif |Waktu untuk hiburan berlebihan bisa menggangu performa belajar |
|`social_media_hours` |-0,17 |Lemah |Negatif |Semakin banyak waktu di media sosial, cenderung menurunkan skor. |
|`age` |-0,01 |Sangat lemah/tidak ada |Netral |Usia tidak memiliki pengaruh signifikan dalam dataset ini. |

## Data Preparation
Tahapan data preparation dilakukan untuk mempersiapkan data mentah agar siap digunakan dalam proses pemodelan machine learning. Proses ini penting untuk memastikan bahwa data bersih, konsisten, dan berada dalam format yang dapat dipahami oleh algoritma.

Beberapa kolom seperti student_id, age, gender, diet_quality, dan lainnya di hapus karena dirasa memiliki korelasi yang rendah ataupun tidak berpengaruh sehingga tidak akan digunakan pada proses prediksi dan dihapus.

Pada tahap ini juga, missing value dan outliers yang ditemukan pada Data Understanding dihapus sehingga tersisa 898 baris dan 8 kolom.

### 1. Encoding Fitur Kategori
Encoding fitur kategori menggunakan OneHotEncoder untuk mengubah fitur kategorikal menjadi nemerik. Sebagian besar algoritma machine learning tidak bisa menangani data dalam bentuk teks atau kategori secara langsung sehingga encoding diperlukan untuk mengonversi fitur kategorikal menjadi format numerik dan memastikan seluruh fitur berada dalam skala numerik agar bisa diproses oleh model seperti clustering atau klasifikasi.

### 2. Train-Test Split
Train-Test split membagi dataset menjadi data latih (train) dan data uji (test) menggunakan rasio 80:20 dengan fungsi `train_test_split()` dari sklearn.

Sehingga total data setelah terbagi adalah 718 data latih (train) dan 180 data uji (test).

Pemisahan data ini dilakukan untuk dapat melatih model pada subset data (train), menguji performa model pada data baru yang belum pernah dilihat sebelumnya (test), dan menghindari overfitting atau hasil evaluasi yang bias.

### 3. Normalisasi
Normalisasi dilakukan menggunakan metode `MinMaxScaler` dari sklearn.preprocessing untuk mentransformasi data numerik agar memiliki data yang berkisar dari angka 0 sampai dengan 1.

Hal ini diperlukan karena beberapa algoritma yang memiliki metode berbasis jarak (termasuk clustering) sensitif terhadap skala fitur. Selain itu, fitur dengan skala besar bisa mendominasi fitur lain saat perhitungan jarak dilakukan. Normalisasi juga membantu konvergensi model lebih cepat dan akurat.

## Modeling
Tahapan modeling bertujuan untuk membangun model machine learning yang mampu memprediksi nilai `exam_score` berdasarkan fitur-fitur yang telah dipersiapkan. Tiga algoritma yang digunakan dalam proses ini adalah:

- Random Forest Regressor
- AdaBoost Regressor

Ada pun proses penerapannya adalah berikut:
- Model dilatih menggunakan data latih
- Kemudian digunakan untuk memprediksi nlai pada data train dan test

### 1. Random Forest Regressor

Algoritma: `RandomForestRegressor`

Parameter utama: 
- `n_estimators=50` -> Jumlah pohon
- `max_depth=16` -> kedalaman maksimum tiap pohon
- `random_state=55` -> untuk reproduktibilitas hasil
- `n-jobs=-1` -> untuk mempercepat pelatihan dengan menggunakan semua inti CPU

Kelebihan:
- Mengurangi overfitting dibandingkan decision tree tunggal
- Menangani data non-linear dengan baik
- Memberikan fitur penting (feature importance)

Kekurangan:
- Lebih bambah dibanding model sederhana
- Lebih kompleks untuk ditafsirkan
  
### 2. Adaptive Regressor

Algoritma: `AdaBoostRegressor`

Parameter utama: 
- `learning_rate=0.05` -> tingkat kontribusi setiap model lemah
- `random_state=55`-> untuk konsistensi hasil

Kelebihan:
- Bagus untuk menangani data dengan noise rendah
- Dapat meningkatkan akurasi model lemah (weak learners)

Kekurangan:
- Sensitif terhadap outlier
- Butuh banyak eksperimen terhadap learning rata dan jumlah estimators.

## Evaluation
Dalam proyek ini, metrik yang digunakan untuk mengukur performa model adalah Mean Squared Error (MSE). 

MSE mengukur rata-rata kuadrat selisih antara nilai prediksi dan nilai aktual. Semakin kecil nilai MSE, maka semakin baik performa model dalam memprediksi data.

MSE sangat sensitif terhadap nilai error yang besar karena menghitung kuadrat selisih, sehingga cocok untuk mengidentifikasi model yang menghasilkan prediksi yang konsisten.

Hasil evaluasi model pada data latih dan data uji untuk masing-masing model 

|       | train | test|
|-------|-------|-----|
|RF	|0.006764	|0.842023 |
|Boosting |0.059158	|0.831474 |

Berdasarkan hasil evaluasi, model Adaptive Boosting memberikan nilai eror yang paling kecil. Meskipun pada data train, nilai error cenderung lebih besar. Sehingga model Adaptive Boosting yang akan kita pilih sebagai model terbaik untuk melakukan prediksi nlai ujian.

## Referensi
Kayani, S. et al. (2018). Physical Activity and Academic Performance: The Mediating Effect of Self-Esteem and Depression. Sustainability (Switzerland). Retrieved from https://doi.org/10.3390/su10103633
