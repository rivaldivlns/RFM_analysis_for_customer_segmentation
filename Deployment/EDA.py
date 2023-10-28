import streamlit as st



def run():
    st.title("Analisis Data CLustering")

    # Menampilkan gambar monetary_value_cluster.png
    st.image("monetary_value_cluster.png", caption="Distribusi Cluster berdasarkan rata-rata Monetary Value")
    
    # Menampilkan gambar recency_cluster.png
    st.image("recency_cluster.png", caption="Distribusi Cluster berdasarkan rata-rata Recency")
    
    # Menampilkan gambar frequency_cluster.png
    st.image("frequency_cluster.png", caption="Distribusi Cluster berdasarkan rata-rata Frequency")
    
    # Menampilkan gambar scatter_cluster.png
    st.image("scatter_cluster.png", caption="Scatter plot pembagian Cluster berdasarkan model RFM")
    
    # Menampilkan gambar line_cluster.png
    st.image("line_cluster.png", caption="Visualisasi Line Cluster berdasarkan model RFM")

    st.write("Visualisasi di atas menunjukkan pembagian cluster berdasarkan model RFM yang telah dilatih. Dengan memahami distribusi cluster ini, Amazon dapat mengembangkan strategi pemasaran yang lebih terfokus dan efektif.")


if __name__ == "__main__":
    run()
