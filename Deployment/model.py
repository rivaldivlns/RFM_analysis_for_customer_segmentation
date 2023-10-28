# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Define the Streamlit app
with open('model_cluster_RFM.pkl', 'rb') as file_1:
    model_cluster = pickle.load(file_1)

def run():
    st.title("RFM Cluster Prediction")

    id_name = st.number_input(label='Masukkan nomor id name anda', min_value=0)
    Recency = st.number_input(label='Masukkan skor recency anda', min_value=0)
    Frequency = st.number_input(label='Masukkan skor frequency anda', min_value=0)
    Monetary_Value = st.number_input(label='Masukkan skor monetary value anda', min_value=0)
    

    data_inf = pd.DataFrame({
            'id_name' : [id_name],
            'Recency' : [Recency],
            'Frequency' : [Frequency],
            'Monetary_Value' : [Monetary_Value],
            }, index = [0]) #index = 0 karena listnya cuma ada satu
    st.table(data_inf)


    if st.button(label='prediksi'):
        
            # Melakukan prediksi data dummy
            y_pred_inf = model_cluster.predict(data_inf)

            # st.write(y_pred_inf[0])

            if y_pred_inf[0] == 0:
                st.write('Anda merupakan Silver Member! 😃')

            elif y_pred_inf[0] == 2:
                st.write('Anda merupakan Gold Member! 😃')
            else:
                st.write('Anda merupakan Bronze Member! 😃')


# Run the app
if __name__ == "__main__":
    run()
