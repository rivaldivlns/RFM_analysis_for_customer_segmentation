import streamlit as st
import EDA
import model


page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'EDA', 'Model'])



if page == 'Home Page':
    # Menampilkan perkenalan
    st.header('Welcome To RFM Cluster Prediction')
    st.write("Selamat datang di Aplikasi Prediksi Kluster RFM kami. Aplikasi ini bertujuan untuk membantu Anda menentukan jenis keanggotaan berdasarkan RFM (Recency, Frequency, Monetary Value).")
    st.write("Anda hanya perlu memasukkan ID Anda, serta nilai Recency, Frequency, dan Monetary Value Anda, dan kami akan memberikan prediksi keanggotaan Anda.")
    st.write("Aplikasi ini sangat berguna untuk mengidentifikasi jenis pelanggan Anda, memahami perilaku pelanggan, dan merencanakan strategi pemasaran yang lebih baik.")

    # Menampilkan masalah yang akan dipecahkan
    st.subheader("Problem Statement:")
    st.write("Meningkatkan revenue sebesar 5% dalam waktu 6 bulan dengan menciptakan campaign marketing yang efektif dan efisien berdasarkan hasil dari segmentasi customer.")
    st.write("Dengan aplikasi ini, Anda dapat dengan cepat memprediksi jenis keanggotaan pelanggan dan mengambil tindakan yang sesuai untuk melayani mereka lebih baik.")

elif page == 'EDA':
    EDA.run()

else:
    model.run()