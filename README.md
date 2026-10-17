# 🌾 Crop Yield Prediction menggunakan Machine Learning

Repository ini berisi proyek tugas mata kuliah **Machine Learning** untuk melakukan analisis data pertanian dan membangun model prediksi hasil panen (*Crop Yield Prediction*) menggunakan Python.

Proyek ini bertujuan untuk mempelajari penerapan Machine Learning dalam memperkirakan hasil panen berdasarkan karakteristik pertanian dan kondisi lingkungan.

## 👩‍🎓 Informasi Mahasiswa

- **Nama:** Ilma Parma Sakia Daulay
- **Universitas:** Universitas Pamulang
- **Kelas:** 05TPLP022
- **Mata Kuliah:** Machine Learning

## 🎯 Tujuan Proyek

Tujuan dari proyek ini adalah:

1. Memahami karakteristik dataset hasil panen.
2. Melakukan eksplorasi dan pembersihan data.
3. Melakukan preprocessing dan transformasi data agar siap digunakan dalam pemodelan.
4. Membangun model Machine Learning untuk memprediksi hasil panen.
5. Membandingkan performa model menggunakan metrik evaluasi.
6. Menyimpan model terlatih agar dapat digunakan kembali untuk melakukan prediksi.

## 📊 Dataset

Dataset yang digunakan adalah `crop_yield.csv`, yang berisi informasi mengenai hasil panen dan faktor-faktor yang berhubungan dengan kegiatan pertanian.

**Ukuran dataset:** 999.741 baris dan 10 kolom berdasarkan hasil pemeriksaan DataFrame menggunakan `df.shape`.

### Variabel Target

- `Yield_tons_per_hectare` — hasil panen dalam ton per hektare yang menjadi variabel target prediksi.

### Fitur Dataset

Dataset mencakup informasi berikut:

| Fitur | Keterangan |
|---|---|
| `Region` | Wilayah pertanian |
| `Soil_Type` | Jenis tanah |
| `Crop` | Jenis tanaman |
| `Rainfall_mm` | Curah hujan dalam milimeter |
| `Temperature_Celsius` | Suhu dalam derajat Celsius |
| `Fertilizer_Used` | Informasi penggunaan pupuk |
| `Irrigation_Used` | Informasi penggunaan irigasi |
| `Weather_Condition` | Kondisi cuaca |
| `Days_to_Harvest` | Jumlah hari hingga panen |
| `Yield_tons_per_hectare` | Hasil panen per hektare sebagai variabel target |

### Sumber Dataset

Dataset dapat diakses melalui tautan Google Drive berikut:

[Unduh Dataset Crop Yield](https://drive.google.com/file/d/1m3dEAz_7HJB9ZdXlSiZcu2xuDxU6Cwtc/view?usp=sharing)

## ⚙️ Tahapan Pengerjaan

Proyek ini mencakup beberapa tahapan pengolahan data dan pemodelan Machine Learning:

1. **Import Library** — mengimpor pustaka Python yang diperlukan.
2. **Data Loading** — membaca dataset ke dalam DataFrame menggunakan Pandas.
3. **Exploratory Data Analysis (EDA)** — memahami struktur data, tipe data, statistik deskriptif, dan distribusi variabel.
4. **Data Cleaning** — memeriksa dan menangani data kosong, duplikasi, serta ketidaksesuaian data jika ditemukan.
5. **Data Transformation dan Preprocessing** — menyiapkan fitur dan melakukan transformasi data sesuai kebutuhan model.
6. **Data Splitting** — membagi dataset menjadi data training dan testing dengan rasio 80:20.
7. **Model Training** — melatih algoritma regresi untuk memprediksi hasil panen.
8. **Model Evaluation** — mengevaluasi performa model menggunakan metrik MAE, MSE, dan R².
9. **Model Saving** — menyimpan model terlatih menggunakan Joblib.
10. **Prediction Testing** — menguji model untuk menghasilkan prediksi berdasarkan data masukan.

## 🤖 Algoritma Machine Learning

Algoritma regresi yang digunakan dalam proyek ini meliputi:

- **Linear Regression** — mempelajari hubungan antara fitur dan hasil panen menggunakan pendekatan regresi linear.
- **LARS (Least Angle Regression)** — membangun model regresi menggunakan pendekatan Least Angle Regression.
- **Gradient Boosting Regressor** — menggunakan pendekatan ensemble yang membangun model secara bertahap untuk mempelajari pola pada data.

Ketiga algoritma digunakan untuk mempelajari hubungan antara karakteristik pertanian dan hasil panen. Performa masing-masing model dapat dibandingkan berdasarkan hasil evaluasi pada data testing.

## 📈 Evaluasi Model

Evaluasi dilakukan untuk mengukur kemampuan model dalam memprediksi hasil panen.

| Metrik | Keterangan |
|---|---|
| MAE (*Mean Absolute Error*) | Mengukur rata-rata selisih absolut antara nilai aktual dan prediksi. |
| MSE (*Mean Squared Error*) | Mengukur rata-rata kuadrat kesalahan prediksi. |
| R² (*Coefficient of Determination*) | Mengukur proporsi variasi nilai target yang dapat dijelaskan oleh model. |

Secara umum, nilai MAE dan MSE yang lebih rendah menunjukkan kesalahan prediksi yang lebih kecil, sedangkan nilai R² yang lebih tinggi menunjukkan kemampuan model yang lebih baik dalam menjelaskan variasi target.

Nilai evaluasi dan model terbaik mengikuti hasil eksperimen yang tercatat pada notebook.

## 🛠️ Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Jupyter Notebook** — lingkungan untuk analisis data dan eksperimen.
- **Pandas** — pengolahan dan manipulasi data.
- **NumPy** — operasi numerik.
- **Matplotlib** — visualisasi data.
- **Scikit-learn** — preprocessing, pemodelan, dan evaluasi Machine Learning.
- **Joblib** — penyimpanan dan pemuatan model terlatih.

## 📁 Struktur Repository

```text
MachineLearning-CropYield-IlmaParma/
├── CropYield.ipynb
├── crop_yield.csv
├── train.csv
├── test.csv
├── crop_yield_gbr_model.joblib
├── deploy.py
├── README.md
└── .gitignore
```

### Keterangan File

- `CropYield.ipynb` — notebook utama untuk analisis data, preprocessing, pelatihan, evaluasi, dan pengujian model.
- `crop_yield.csv` — dataset utama untuk analisis dan pemodelan.
- `train.csv` — file data training.
- `test.csv` — file data testing.
- `crop_yield_gbr_model.joblib` — file model Gradient Boosting Regressor yang telah disimpan.
- `deploy.py` — skrip Python untuk mendukung proses prediksi atau deployment.
- `README.md` — dokumentasi proyek.
- `.gitignore` — daftar file atau folder yang tidak perlu dilacak oleh Git.

## 💻 Cara Menjalankan Proyek

### 1. Clone Repository

Buka terminal, kemudian jalankan:

```bash
git clone https://github.com/ilmaparmasakiadaulay-creator/MachineLearning-CropYield-IlmaParma.git
cd MachineLearning-CropYield-IlmaParma
```

### 2. Buat Virtual Environment

Pada Windows PowerShell, jalankan:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Langkah ini opsional, tetapi disarankan agar dependensi proyek terpisah dari instalasi Python lainnya.

### 3. Instal Library

Jalankan perintah berikut:

```bash
pip install pandas numpy matplotlib scikit-learn jupyter joblib
```

### 4. Siapkan Dataset

Pastikan file `crop_yield.csv` tersedia pada lokasi yang sesuai dengan path yang digunakan dalam notebook. Jika dataset belum tersedia, unduh melalui tautan Google Drive pada bagian Dataset.

### 5. Jalankan Jupyter Notebook

Jalankan:

```bash
jupyter notebook
```

Buka file `CropYield.ipynb`, kemudian jalankan sel notebook sesuai urutan pengerjaan.

## 📝 Hasil Proyek

Proyek ini menghasilkan:

1. Analisis karakteristik dataset pertanian.
2. Dataset yang telah melalui tahapan pembersihan dan preprocessing sesuai kebutuhan pemodelan.
3. Model Machine Learning untuk memprediksi hasil panen.
4. Evaluasi performa model menggunakan MAE, MSE, dan R².
5. File model terlatih yang dapat digunakan kembali untuk proses prediksi.

Hasil numerik, perbandingan algoritma, dan kesimpulan akhir mengikuti eksperimen yang dijalankan dalam notebook.

## 📌 Catatan

Proyek ini dibuat untuk keperluan pembelajaran dan tugas mata kuliah Machine Learning. Hasil prediksi merupakan estimasi berdasarkan pola yang dipelajari dari dataset dan tidak menggantikan penilaian agronomis di lapangan.

---

**Dibuat oleh Ilma Parma Sakia Daulay**  
Universitas Pamulang — Kelas 05TPLP022
