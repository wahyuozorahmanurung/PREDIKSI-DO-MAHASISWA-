# Tambahkan import yang sudah ada
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np
import plotly.graph_objects as go

# Set default visual
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# Load Data Original
@st.cache_data
def load_original_data():
    try:
        df_original = pd.read_csv("data_mahasiswa_risk.csv")
        return df_original
    except Exception as e:
        st.error(f"Error loading original data: {e}")
        return None

# Load Data Cluster
@st.cache_data
def load_cluster_data():
    try:
        df_cluster = pd.read_csv("cluster.csv")
        return df_cluster
    except Exception as e:
        st.error(f"Error loading cluster data: {e}")
        return None

# Load Model
def load_model(file_path):
    try:
        model = joblib.load(file_path)
        return model
    except Exception as e:
        st.error(f"Error loading model from {file_path}: {e}")
        return None

# Predict
def predict(model, input_df):
    try:
        pred = model.predict(input_df)
        return pred
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

# App Title
st.title("🎓 Dashboard Prediksi Drop Out Mahasiswa")
st.write("Dashboard ini membantu memprediksi kemungkinan mahasiswa mengalami Drop Out berdasarkan berbagai indikator akademik dan aktivitas online menggunakan model Logistic Regression.")

# Sidebar
st.sidebar.title("📋 Dashboard Info")
st.sidebar.subheader("Tujuan Dashboard")
st.sidebar.write("Dashboard ini dirancang untuk mengidentifikasi mahasiswa yang berisiko drop out (DO) berdasarkan data akademik, kehadiran, aktivitas online, dan faktor sosial-ekonomi. Prediksi dilakukan menggunakan model *Logistic Regression* untuk memberikan wawasan yang akurat dan mendukung intervensi dini.")
st.sidebar.subheader("Dataset")
st.sidebar.write("Data mahasiswa meliputi IPK, kehadiran, jumlah mata kuliah retake, aktivitas online, status pekerjaan, beban kerja, dan status sosial-ekonomi.")
st.sidebar.subheader("Team")
st.sidebar.write("- Wahyu Ozorah Manurung\n- Damianus Christopher Samosir\n- Torang Four Yones")
st.sidebar.markdown("<p style='text-align: center; color: #A9A9A9;'>© 2025 Predictive Analytics Team</p>", unsafe_allow_html=True)

# ✅ Load kedua dataframe sebelum tabs
df_original = load_original_data()
df_cluster = load_cluster_data()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📂 Data Overview", "🔍 Analisis Model", "🔮 Prediksi Drop Out", "📝 Kesimpulan"])

# Tab 1: Data Exploration
with tab1:
    st.subheader("📊 Data Mahasiswa")
    st.write("🗂 Dataset Original (Belum Preprocessing) data_mahasiswa_risk.csv")
    if df_original is not None:
        st.dataframe(df_original.head())

    st.markdown("---")

    st.write("🗂 Dataset Hasil Preprocessing (Clustered) cluster_.csv")
    if df_cluster is not None:
        st.dataframe(df_cluster.head())

# Tab 2: Model Analysis
with tab2:
    st.subheader("📊 Model Analysis")

    st.write("### 📌 Logistic Regression")
    
    logreg_report = """
    precision    recall  f1-score   support

    0       0.81      0.81      0.81       101
    1       0.95      0.95      0.95       399

    accuracy                           0.92       500
    macro avg       0.88      0.88      0.88       500
    weighted avg    0.92      0.92      0.92       500
    """
    st.text("Laporan Klasifikasi Logistic Regression:")
    st.text(logreg_report)

    cm_logreg = [[82, 19],
                 [19, 380]]
    
    fig_cm_logreg, ax1 = plt.subplots()
    sns.heatmap(cm_logreg, annot=True, fmt='d', cmap='Blues', ax=ax1,
                xticklabels=['0', '1'],
                yticklabels=['0', '1'])
    ax1.set_title('Confusion Matrix - Logistic Regression')
    ax1.set_xlabel('Prediksi')
    ax1.set_ylabel('Aktual')
    st.pyplot(fig_cm_logreg)

# Tab 3: Prediksi Drop Out
# Tab 3: Prediksi Drop Out - Logistic Regression
with tab3:
    st.header("🔮 Prediksi Drop Out Mahasiswa - Logistic Regression")

    try:
        logreg_model = load_model("logistic_regression_model.pkl")
    except Exception as e:
        st.error(f"Gagal memuat model Logistic Regression: {e}")
        st.stop()

    try:
        feature_columns = joblib.load("features.pkl")
    except Exception as e:
        st.error(f"Error loading feature columns: {e}")
        st.stop()

    def insight_analisis_custom(avg_ipk, avg_kehadiran, retake, beban_kerja):
        st.markdown("### 📊 Insight Analisis Data")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Rata-rata IPK", f"{avg_ipk:.2f}")
            st.metric("Jumlah Retake", retake)
        with col2:
            st.metric("Rata-rata Kehadiran", f"{avg_kehadiran:.2f}%")
            st.metric("Beban Kerja", f"{beban_kerja:.1f} jam/minggu")

    with st.form("form_logreg"):
        nama = st.text_input("Nama Mahasiswa")
        npm = st.text_input("NPM")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 IPK per Semester")
            ipk_semester = [st.number_input(f"IPK Semester {i+1}", 0.0, 4.0, 0.0, 0.01) for i in range(8)]
        with col2:
            st.subheader("📈 Kehadiran per Mata Kuliah (%)")
            kehadiran_mk = [st.number_input(f"Kehadiran MK{i+1} (%)", 0.0, 100.0, 0.0, 0.1) for i in range(6)]
            retake = st.number_input("Jumlah MK Retake", 0, 10, 0)

        st.subheader("🌐 Aktivitas Online Learning")
        online_activities = [st.number_input(f"Online Activity {i+1}", 0.0, 100.0, 0.0, 0.1) for i in range(6)]

        st.subheader("💼 Data Non-Akademik")
        status_pekerjaan = st.selectbox("Status Pekerjaan", ["Tidak Bekerja", "Paruh Waktu", "Penuh Waktu"])
        sosial_ekonomi = st.selectbox("Status Sosial Ekonomi", ["Rendah", "Menengah", "Tinggi"])
        beban_kerja = st.slider("Beban Kerja (Jam/Minggu)", 0.0, 60.0, 0.0)

        submitted = st.form_submit_button("🚀 Prediksi Drop Out")

    if submitted:
        pekerjaan_df = {
            "status_pekerjaan_Tidak Bekerja": int(status_pekerjaan == "Tidak Bekerja"),
            "status_pekerjaan_Paruh Waktu": int(status_pekerjaan == "Paruh Waktu"),
            "status_pekerjaan_Penuh Waktu": int(status_pekerjaan == "Penuh Waktu"),
        }

        sosial_df = {
            "sosial_ekonomi_Rendah": int(sosial_ekonomi == "Rendah"),
            "sosial_ekonomi_Menengah": int(sosial_ekonomi == "Menengah"),
            "sosial_ekonomi_Tinggi": int(sosial_ekonomi == "Tinggi"),
        }

        input_dict = {
            **{f"ipk_smt{i+1}": ipk_semester[i] for i in range(8)},
            **{f"kehadiran_mk{i+1}": kehadiran_mk[i] for i in range(6)},
            **{f"online_activity{i+1}": online_activities[i] for i in range(6)},
            "retake": retake,
            "beban_kerja": beban_kerja,
            **pekerjaan_df,
            **sosial_df,
        }

        input_df = pd.DataFrame([input_dict])

        for col in feature_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[feature_columns]

        prediction = predict(logreg_model, input_df)
        if prediction is not None:
            probability = (
                logreg_model.predict_proba(input_df)[0][1]
                if hasattr(logreg_model, "predict_proba")
                else 0
            )

            label_mapping = {0: "Drop Out (Berisiko Tinggi)", 1: "Tidak Drop Out (Berisiko Rendah)"}
            result = label_mapping.get(prediction[0], "Tidak Diketahui")
            status_lulus = prediction[0] == 1

            st.subheader("📌 Hasil Prediksi")
            st.markdown(f"Mahasiswa *{nama}* ({npm}) diprediksi: *{result}*")

            avg_ipk = np.mean(ipk_semester)
            avg_kehadiran = np.mean(kehadiran_mk)
            insight_analisis_custom(avg_ipk, avg_kehadiran, retake, beban_kerja)

            gauge_color = "#3EC70B" if status_lulus else "#FF4B4B"
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=probability * 100,
                title={'text': "Probabilitas Tidak Drop Out (%)"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': gauge_color},
                    'steps': [
                        {'range': [0, 50], 'color': "#FF4B4B"},
                        {'range': [50, 75], 'color': "#FFC107"},
                        {'range': [75, 100], 'color': "#3EC70B"}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': probability * 100
                    }
                }
            ))
            st.plotly_chart(fig)

            with st.expander("📄 Rangkuman Data Mahasiswa"):
                st.dataframe(pd.DataFrame({
                    "Rata-rata IPK": [avg_ipk],
                    "Rata-rata Kehadiran (%)": [avg_kehadiran],
                    "Retake": [retake],
                    "Beban Kerja": [beban_kerja],
                    "Status Pekerjaan": [status_pekerjaan],
                    "Status Sosial Ekonomi": [sosial_ekonomi]
                }))

# Tab 4: Kesimpulan
with tab4:
    st.subheader("📝 Kesimpulan")
    st.write("""
    Dashboard ini membantu memprediksi risiko *Drop Out* mahasiswa berdasarkan faktor akademik dan sosial menggunakan model *Logistic Regression*.

    *Insight:*
    - Faktor seperti IPK, Rata-rata Kehadiran, Jumlah Retake, Beban Kerja dan Aktivitas Online sangat berpengaruh terhadap prediksi.
    - Model *Logistic Regression* memberikan hasil yang cukup akurat untuk digunakan sebagai dasar intervensi.

    *Rekomendasi:*
    - Gunakan hasil prediksi ini untuk membantu *monitoring* dan *intervensi dini* pada mahasiswa berisiko tinggi.
    - Perlu integrasi lebih lanjut dengan sistem akademik untuk tindakan preventif.

    *Disclaimer:* Model ini dapat terus disempurnakan dengan penambahan data dan teknik pemodelan yang lebih canggih.
    """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #A9A9A9;'>© 2025 Predictive Drop Out Dashboard</p>", unsafe_allow_html=True)