# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

### Latar Belakang
Kualitas wine merupakan aspek krusial dalam industri minuman fermentasi, memengaruhi nilai jual dan reputasi produsen. Penilaian kualitas secara tradisional dilakukan oleh ahli pencicip (wine tasters), namun metode ini memiliki kelemahan seperti subjektivitas dan inkonsistensi (Xu, 2024). Untuk mengatasi hal tersebut, pendekatan berbasis data dengan algoritma machine learning menjadi solusi alternatif yang lebih objektif dan efisien (Arshad et al., 2024).

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


