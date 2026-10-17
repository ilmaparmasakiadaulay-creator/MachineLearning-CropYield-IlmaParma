from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat model yang sudah disimpan
model = joblib.load('crop_yield_gbr_model.joblib')

# Fitur yang digunakan saat training
feature_names = [
    'Region',
    'Soil_Type',
    'Crop',
    'Rainfall_mm',
    'Temperature_Celsius',
    'Fertilizer_Used',
    'Irrigation_Used',
    'Weather_Condition',
    'Days_to_Harvest'
]

# Membuat endpoint untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Mengambil data fitur dari JSON
        input_data = pd.DataFrame([data['data']])

        # Menyesuaikan urutan kolom dengan data training
        input_data = input_data[feature_names]

        # Melakukan prediksi hasil panen
        prediction = model.predict(input_data)

        return jsonify({
            'prediction': float(prediction[0])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)