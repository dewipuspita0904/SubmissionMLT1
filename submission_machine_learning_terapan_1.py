# -*- coding: utf-8 -*-
"""Submission Machine Learning Terapan 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JgulOrelPqwuMdTY77BaURdqpkzD110H

# Prediksi Nilai Ujian Berdasarkan Kebiasaan dan Gaya Hidup Mahasiswa
![passing-score-for-real-estate-exam.jpg](https://agentrealestateschools.com/wp-content/uploads/2021/11/passing-score-for-real-estate-exam.jpg)

## Latar Belakang
Pendidikan tinggi memiliki peran penting dalam membentuk masa depan individu dan masyarakat. Namun, pencapaian akademik mahasiswa tidak hanya ditentukan oleh kurikulum formal, melainkan juga oleh faktor-faktor eksternal seperti kebiasaan belajar, durasi penggunaan media sosial, kualitas tidur, kondisi kesehatan mental, dan partisipasi ekstrakurikuler. Pemahaman yang baik terhadap pengaruh variabel-variabel ini dapat membantu institusi pendidikan merancang intervensi yang tepat untuk mendukung performa mahasiswa.

Proyek ini bertujuan untuk membangun model regresi guna memprediksi exam score mahasiswa berdasarkan fitur-fitur kebiasaan harian dan gaya hidup dalam dataset “Student Habits vs Academic Performance” (Kaggle).

# 1. Import Library
"""

!pip install -q kaggle

# Commented out IPython magic to ensure Python compatibility.
# Import Data Loading
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns
import zipfile
import warnings
warnings.filterwarnings('ignore')

# Import Data Preparation
from sklearn.preprocessing import  OneHotEncoder, StandardScaler # OneHotEncoder: Encoding Fitur Kategori; StandardScaler: Standarisasi
from sklearn.model_selection import train_test_split # Split Data

# Import Model Development
from sklearn.neighbors import KNeighborsRegressor # K-Nearest Neighbor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor # Random Forest & Boosting

# Import Model Evaluation
from sklearn.metrics import mean_squared_error # MSE

"""# 2. Data Understanding

## 2.1. Data Loading

Supaya isi dataset lebih mudah dipahami, kita perlu melakukan proses loading data terlebih dahulu. Tidak lupa, import library pandas untuk dapat membaca file datanya.
"""

files.upload()

!mkdir ~/.kaggle # membuat folder .kaggle
!cp kaggle.json ~/.kaggle/ # menyalin file credential ke lokasi yang sesuai
!chmod 600 ~/.kaggle/kaggle.json # mengatur izin file agar bisa digunakan oleh kernel Colab
!kaggle datasets download -d jayaantanaath/student-habits-vs-academic-performance # mengunduh dataset dari Kaggle

# mengekstrak file ZIP dataset
zip_ref = zipfile.ZipFile('/content/student-habits-vs-academic-performance.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()

# load the dataset
ml = pd.read_csv('/content/student_habits_performance.csv')
ml

"""Output di atas memberikan informasi sebagai berikut:
- Ada 1.000 baris.
- Terdapat 16 kolom, yaitu: `student_id`, `age`, `gender`, `study_hours_per_day`, `social_media_hours`, `netflix_hours`, `part_time_job`, `attendance_percentage`, `sleep_hours`, `diet_quality`, `exercise_frequency`, `parental_education_level`, `internet_quality`, `mental_health_rating`, `extracurricular_participation`, dan `exam_score`.

## 2.2. EDA - Deskripsi Variabel

Berdasarkan informasi dari Kaggle, variabel-variabel pada Mental Health dataset adalah sebagai berikut:

|Fitur |Tujuan|
|-----------|------------------------|
|student_id |ID unik siswa (tidak penting untuk analisis; dapat dianonimkan) |
|age |Usia dalam tahun |
|gender |Jenis kelamin |
|study_hours_per_day |Rata-rata lama belajar per hari |
|social_media_hours |Rata-rata lama bermain sosial media per hari|
|netflix_hours |Rata-rata lama menonton netflix per hari |
|part_time_job |Apakah memiliki pekerjaan sebagai part time atau tidak |
|attendance_percentage |Persentase kehadiran kelas (0-100%) |
|sleep_hours |Rata-rata lama tidur harian |
|diet_quality |Kualitas makanan sehari-hari (Poor/Fair/Good) |
|exercise_frequency |Berapa kali berolahraga dalam seminggu|
|parental_education_level|Tingkat edukasi orang tua|
|internet_quality|Kualitas internet|
|mental_health_rating |Nilai kesehatan mental dari skala 1-10|
|extracurricular_participation|Apakah mengikuti ekstrakulikuler atau tidak|
|exam_score (target)|Nilai ujian|

Setelah memahami deskripsi variabel pada data, langkah selanjutnya adalah mengecek informasi pada dataset dengan fungsi `info()` berikut.
"""

ml.info()

"""Dari output terlihat bahwa:
- Terdapat 6 kolom numerik dengan tipe data float64, yaitu: `study_hours_per_day`, `social_media_hours`, `netflix_hours`, `attendance_percentage`, `sleep_hours`, dan `exam_score`.
- Terdapat 3 kolom numerik dengan tipe data int64, yaitu: `age`, `exercise_frequency`, dan `mental_health_rating`.
- Terdapat 7 kolom dengan tipe object, yaitu: `student_id`, `gender`, `part_time_job`, `diet_quality`, `parental_education_level`, dan `internet_quality`, dan `extracurricular_participation`.

Uraian di atas menunjukkan bahwa setiap kolom telah memiliki tipe data yang sesuai. Selanjutnya, kita akan mengecek deskripsi statistik data dengan fitur `describe()`.
"""

ml.describe()

"""Fungsi `describe()` memberikan informasi statistik pada masing-masing kolom, antara lain:
- `Count` adalah jumlah sampel pada data.
- `Mean` adalah nilai rata-rata.
- `Std` adalah standar deviasi.
- `Min` yaitu nilai minimum setiap kolom.
- `25%` adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama.
- `50%` adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- `75%` adalah kuartil ketiga.
- `Max` adalah nilai maksimum.

## 2.3. EDA - Menangani Missing Value dan Outliers
"""

# Karena kita tidak akan menggunakan kolom student_id, maka kolom student_id dapat kita hapus.
ml.drop(['student_id'], inplace=True, axis=1)

ml.isnull().sum()

"""Dari data di atas, terdapat 91 missing value pada data sehingga perlu kita buang."""

ml_clean = ml.dropna()

ml_clean.isnull().sum()

ml_clean.shape

"""Setelah missing value dan kolom tidak terpakai dihapus, sekarang data tersisa adalah 909 baris dengan 15 kolom."""

# Visualisasi data Mental Healths ddengan boxplot untuk mendeteksi outliers pada beberapa fitur numerik.
sns.boxplot(x=ml_clean['age']) # Age

sns.boxplot(x=ml_clean['exercise_frequency']) # Exercise Frequency

sns.boxplot(x=ml_clean['mental_health_rating']) # Mental Heatlh Rating

sns.boxplot(x=ml_clean['study_hours_per_day']) # Study Hours per Day

sns.boxplot(x=ml_clean['social_media_hours']) # Social Media Hours

sns.boxplot(x=ml_clean['netflix_hours']) # Netflix Hours

sns.boxplot(x=ml_clean['attendance_percentage']) # Attendance Percentage

sns.boxplot(x=ml_clean['sleep_hours']) # Sleep Hours

# Ambil hanya kolom numerikal
numeric_cols = ml_clean.select_dtypes(include='number').columns

# Hitung Q1, Q3, dan IQR hanya untuk kolom numerikal
Q1 = ml_clean[numeric_cols].quantile(0.25)
Q3 = ml_clean[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

# Buat filter untuk menghapus baris yang mengandung outlier di kolom numerikal
filter_outliers = ~((ml_clean[numeric_cols] < (Q1 - 1.5 * IQR)) |
                    (ml_clean[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Terapkan filter ke dataset asli (termasuk kolom non-numerikal)
ml_clean = ml_clean[filter_outliers]

# Cek ukuran dataset setelah outlier dihapus
ml_clean.shape

"""Setelah data duplikat dan data yang berada pada outlier dihapus, maka dataset tersisa 894 sampel.

## 2.4. EDA - Univariate Analysis
"""

# Membagi fitur pada dataset menjadi 2 bagian, yaitu numerical features dan categorical features.
numerical_features = ['age', 'exercise_frequency', 'mental_health_rating', 'study_hours_per_day', 'social_media_hours', 'netflix_hours', 'attendance_percentage', 'sleep_hours', 'exam_score']
categorical_features = ['gender', 'part_time_job', 'diet_quality', 'parental_education_level', 'internet_quality', 'extracurricular_participation']

"""### Categorical Features
#### Fitur Gender
"""

feature = categorical_features[0]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Distribusi gender dalam dataset relatif seimbang antara laki-laki (48.4%) dan perempuan (47.5%), dengan sejumlah kecil responden mengidentifikasi sebagai Other (4.0%). Komposisi ini menunjukkan representasi gender yang cukup merata, meskipun kategori "Other" masih minoritas.

#### Fitur Part Time Job
"""

feature = categorical_features[1]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Mayoritas responden tidak memiliki pekerjaan paruh waktu (78.6%), sementara hanya 21.4% yang bekerja paruh waktu. Ini mengindikasikan bahwa sebagian besar individu dalam populasi ini berfokus pada kegiatan lain seperti studi penuh waktu.

#### Fitur Diet Quality
"""

feature = categorical_features[2]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Responden paling banyak menilai kualitas makanan mereka sebagai Fair (43.8%), disusul oleh Good (38.4%), dan Poor (17.8%). Ini menunjukkan bahwa mayoritas responden memiliki pola makan yang cukup baik, dengan sebagian kecil mengalami pola makan yang buruk.

#### Fitur Parental Education Level
"""

feature = categorical_features[3]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Tingkat pendidikan orang tua paling banyak berada di kategori High School (43.1%), diikuti oleh Bachelor (38.6%) dan Master (18.3%). Komposisi ini menunjukkan latar belakang pendidikan orang tua yang umumnya menengah ke atas, namun masih didominasi oleh pendidikan sekolah menengah.

#### Fitur Internet Quality
"""

feature = categorical_features[4]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Mayoritas responden menilai kualitas internet mereka sebagai Good (45.2%) dan Average (38.7%), dengan hanya 16.1% yang mengalami kualitas internet Poor. Hal ini menunjukkan bahwa sebagian besar responden memiliki akses internet yang cukup baik, yang dapat berpengaruh terhadap aktivitas belajar atau hiburan mereka.

#### Fitur  Extracurricular Participation
"""

feature = categorical_features[5]
count = ml_clean[feature].value_counts()
percent = 100*ml_clean[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Sebanyak 68.0% responden tidak mengikuti kegiatan ekstrakurikuler, sementara hanya 32.0% yang berpartisipasi. Ini menandakan bahwa partisipasi dalam kegiatan ekstrakurikuler masih belum umum di kalangan responden, yang mungkin dapat memengaruhi aspek pengembangan diri di luar akademik.

### Numerical Features
"""

ml_clean.hist(bins=50, figsize=(20,15))
plt.show()

"""Berdasarkan informasi di atas, terdapat beberapa insight yang bisa kita ambil:
- `age`: Distribusi usia cukup merata antara 17 hingga 24 tahun, dengan sedikit lonjakan pada usia 20 dan 24 tahun. Ini menunjukkan bahwa responden berasal dari rentang usia mahasiswa atau remaja akhir.
- `study_hours_per_day`: Sebagian besar responden belajar antara 2 hingga 5 jam per hari, dengan puncak sekitar 3–4 jam. Distribusi agak right-skewed, artinya sedikit responden yang belajar lebih dari 6 jam per hari.
- `social_media_hours`: Distribusi waktu penggunaan media sosial cukup variatif, dengan puncak di sekitar 2–3 jam. Terlihat pola yang agak tidak teratur, tapi mayoritas masih menggunakan media sosial dalam rentang 1–4 jam per hari.
- `netflix_hours`: Sebagian besar responden menonton Netflix selama 1–2 jam per hari, dengan jumlah kecil yang menonton lebih dari 3 jam. Distribusi ini juga right-skewed, menunjukkan bahwa binge-watching bukan kebiasaan mayoritas.
- `attendance_percentage`: Sebagian besar responden memiliki persentase kehadiran tinggi, dengan konsentrasi kuat antara 85% hingga 100%. Hal ini menunjukkan tingkat kedisiplinan yang baik secara umum.
- `sleep_hours`: Distribusi jam tidur membentuk pola normal (bell-shaped) dengan puncak di 6 hingga 7 jam per hari. Artinya, sebagian besar responden tidur dalam durasi yang disarankan untuk dewasa muda.
- `exercise_frequency`: Distribusinya cukup merata antara 0 hingga 6 kali per minggu, menunjukkan kebiasaan olahraga yang beragam, dari yang tidak pernah hingga yang cukup rutin.
- `mental_health_rating`: Sebagian besar nilai mental health rating terdistribusi merata dari 1 sampai 10, yang bisa mengindikasikan persepsi kesehatan mental yang bervariasi, tanpa dominasi jelas.
- `exam_score`: Distribusi nilai ujian menyerupai bentuk normal, dengan puncak antara 60–70. Ini menunjukkan performa umum berada di tingkat sedang hingga baik.

## 2.5. EDA - Multivariate Analysis

### Categorical Features
Pada tahap ini, kita akan mengecek `exam_score` terhadap masing-masing fitur untuk mengetahui pengaruh fitur kategori terhadap `exam_score`.
"""

cat_features = ml_clean.select_dtypes(include='object').columns.to_list()

for col in cat_features:
  sns.catplot(x=col, y="exam_score", kind="bar", dodge=False, height = 4, aspect = 3,  data=ml_clean, palette="Set3")
  plt.title("Rata-rata 'exam_score' Relatif terhadap - {}".format(col))

"""Dengan mengamati rata-rata nilai ujian relatif terhadap fitur kategori di atas, kita memperoleh insight sebagai berikut:

1. `gender`
- Perempuan cenderung memiliki performa ujian yang lebih baik dibandingkan laki-laki. Bisa jadi karena perbedaan gaya belajar atau manajemen waktu.

2. `part_time_job`
- Bekerja sambil sekolah bisa mengganggu waktu belajar dan fokus sehingga berdampak negatif terhadap performa akademik.

3. `diet_quality`
- Pola makan tidak selalu berkorelasi langsung dengan performa akademik; bisa jadi siswa dengan diet `Fair` justru memiliki gaya hidup seimbang lainnya.

4. `parental_education_level`
- Hasil yang didapat tidak linear, bisa jadi memiliki faktor lain seperti dukungan emosional atau ekspektasi orang tua mungkin lebih berperan daripada tingkat pendidikan formal mereka.

5. `internet_quality`
- Koneksi internet yang terlalu baik mungkin mengarah pada distraksi online, sementara koneksi terlalu buruk menghambat akses belajar. Kualitas cukup bisa jadi ideal untuk menjaga fokus.

6. `extracurricular_participation`
- Fokus penuh pada akademik bisa meningkatkan nilai ujian, tetapi perlu ditimbang dengan keterampiral non-akademik yang dikembangkan lewat ekstrakurikuler.

### Numerical Features
"""

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(ml_clean, diag_kind = 'kde')

plt.figure(figsize=(10, 8))
correlation_matrix = ml_clean[numerical_features].corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Berdasarkan pairplot dan correlation matrix yang ditampilkan, kita bisa menyimpulkan beberapa insight, antara lain:

|Fitur                |Korelasi dengan `exam_score`     |Kekuatan Korelasi        |Tipe         |Insight Penting         |
|---------------------|-----------|----------|-----------|---------------|
|`study_hours_per_day` |0,82       |Sangat kuat |Positif |Ini adalah faktor terkuat yang menentukan nilai ujian. Semakin banyak belajar, semakin tinggi skornya. |
|`mental_health_rating` |0,32 |Sedang/Lemah |Positif |Kesehatan mental yang baik cenderung mendukung performa belajar. |
|`exercise_frequency` |0,16 |Lemah |Positif |Olahraga mungkin membantu fokus/energi tapi tidak signifikan. |
|`sleep_hours` |0,13 |Lemah |Positif |Tidak cukup sedikit membantu hasil ujian. |
|`attendance_percentage` |0,10 |Lemah |Positif |Hadir di kelas penting, tapi tidak sekuat waktu belajar. |
|`netflix_hours` |-0,16 |Lemah |Negatif |Waktu untuk hiburan berlebihan bisa menggangu performa belajar |
|`social_media_hours` |-0,18 |Lemah |Negatif |Semakin banyak waktu di media sosial, cenderung menurunkan skor. |
|`age` |-0,01 |Sangat lemah/tidak ada |Netral |Usia tidak memiliki pengaruh signifikan dalam dataset ini. |

"""

ml_clean.drop(['age'], inplace=True, axis=1)
ml_clean.head()

"""Karena `age` memiliki pengaruh yang sangat lemah bahkan hampir tidak berpengaruh, maka kita bisa menghiraukan kolom tersebut.

# 3. Data Preparation

## 3.1. Encoding Fitur Kategori
"""

ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['gender'], prefix='gender')],axis=1)
ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['part_time_job'], prefix='part_time_job')],axis=1)
ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['diet_quality'], prefix='diet_quality')],axis=1)
ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['parental_education_level'], prefix='parental_education_level')],axis=1)
ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['internet_quality'], prefix='internet_quality')],axis=1)
ml_clean = pd.concat([ml_clean, pd.get_dummies(ml_clean['extracurricular_participation'], prefix='extracurricular_participation')],axis=1)
ml_clean.drop(['gender', 'part_time_job', 'diet_quality', 'parental_education_level', 'internet_quality', 'extracurricular_participation'], axis=1, inplace=True)
ml_clean.head()

"""Sekarang, variabel kategori telah berubah menjadi variabel numerik.

## 3.2. Train-Test-Split
"""

X = ml_clean.drop(["exam_score"],axis =1)
y = ml_clean["exam_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123) # Membagi data latihan sebesar 80% dan 20% untuk data uji.

# Mengecek jumlah sampel pada masing-masing bagian
print(f'Total data of sample in whole dataset: {len(X)}')
print(f'Total data of sample in train dataset: {len(X_train)}')
print(f'Total data of sample in test dataset: {len(X_test)}')

"""## 3.3. Standarisasi"""

numerical_features = ['exercise_frequency', 'mental_health_rating', 'study_hours_per_day', 'social_media_hours', 'netflix_hours', 'attendance_percentage', 'sleep_hours']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

"""Proses standarisasi mengubah nilai rata-rata (mean) menjadi 0 dan nilai standar deviasi menjadi 1."""

X_train[numerical_features].describe().round(2)

"""Terlihat bahwa setelah proses standarisasi, hasil dari mean adalah 0 dan standar deviasi adalah 1.

# 4. Model Development
Ini adalah tahapan di mana ktia menggunakan algoritma machine learning untuk menjawab problem statement dari tahap business understanding.

Pada tahap ini, kita akan mengembangkan model machine learning dengan tiga algoritma. Kemudian, kita akan mengevaluasi performa masing-masing algoritma dan menentukan algoritma mana yang memberikan hasil prediksi terbaik. Ketiga algoritma yang akan digunakan, antara lain:
1. K-Nearest Neighbor
2. Random Forest
4. Boosting Algorithm
"""

models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'Random Forest', 'Boosting'])

"""## 4.1. K-Nearest Neighbor"""

# KNN Modeling
knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)
models.loc['train_mse','knn'] = mean_squared_error(y_pred=knn.predict(X_train), y_true=y_train)

"""## 4.2. Random Forest"""

# Random Forest Modeling
RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)
models.loc['train_mse','RF'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""## 4.3. Boosting Algorithm"""

# AdaBoosting Modeling
boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
boosting.fit(X_train, y_train)
models.loc['train_mse','boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""# 5. Evaluasi Model"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

"""Untuk memudahkan, mari kita plot metrik tersebut dengan bar chart."""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Dari gambar di atas, terlihat bahwa, model Random Forest (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma KNN memiliki eror yang paling besar (berdasarkan grafik, angkanya di atas 0.07). Sehingga model RF yang akan kita pilih sebagai model terbaik untuk melakukan prediksi nlai ujian."""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)

"""Terlihat bahwa prediksi dengan Random Forest (RF) memberikan hasil yang paling mendekati."""