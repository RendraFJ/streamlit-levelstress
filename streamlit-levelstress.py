import pickle
import streamlit as st

# load save model
model = pickle.load(open('level_stress.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Tingkat Stress')
st.text('Nama : Rendra Faisal Jatnika')
st.text('Nim : 191351192')
st.text('Matkul : Business Intelligence')

# Form Input
Humidity = st.number_input('Masukan Kelembaban (Humidity)')

Temperature = st.number_input('Masukan Suhu (Temperature)')

Stepcount = st.slider('Jumlah Langkah atau Aktifitas (Step Count', 0, 200)


# kode Prediksi
levelstress_diagnosis =''

#Button Prediksi
if st.button('Prediksi Tingkat Stress'):
    levelstress_prediction = model.predict([[Humidity, Temperature, Stepcount]])

    if(levelstress_prediction[0]==0):
        levelstress_diagnosis = 'Stress Tingkat Rendah'
    elif(levelstress_prediction[0]==1):
        levelstress_diagnosis = 'Stress Tingkat Sedang'
    else:
        levelstress_diagnosis = 'Stress Tingkat Tinggi'
st.success(levelstress_diagnosis)