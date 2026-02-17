import streamlit as st
import os

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Eğitim Materyalleri",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Bricolage+Grotesque:wght@800&display=swap');
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background: #fcfcfd; font-family: 'Outfit', sans-serif; }
    
    .hero-container {
        background: linear-gradient(145deg, #8A1538 0%, #5a0e24 100%);
        padding: 40px 60px;
        border-radius: 30px;
        color: white;
        margin-bottom: 40px;
    }
    .hero-title { font-family: 'Bricolage Grotesque', sans-serif; font-size: 2.2rem; margin: 0; }
    
    .elite-card {
        background: white;
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(0,0,0,0.04);
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: 0.3s;
    }
    .elite-card:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(0,0,0,0.05); }

    .stDownloadButton > button {
        background: #8A1538 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-weight: 700 !important;
    }
    .back-btn { 
        margin-bottom: 20px; display: inline-block; text-decoration: none; 
        color: #666; font-weight: 600; background: #eee; padding: 8px 15px; 
        border-radius: 10px; font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
if st.button("← Ana Sayfaya Dön"):
    st.switch_page("app.py")

st.markdown("""
<div class="hero-container">
    <div>
        <div style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; opacity: 0.8; margin-bottom: 8px;">Ankara Üniversitesi Tıp Fakültesi</div>
        <h1 class="hero-title">Eğitim Materyalleri ve Kılavuzlar</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# --- İÇERİK ---
st.markdown("### 📄 Güncel Kılavuzlar")

# YENİ BASİT DOSYA ADI
pdf_name = "gastro_kilavuz.pdf"

# Dosya ana dizinde mi yoksa pages içinde mi kontrol et
file_path = None
if os.path.exists(pdf_name):
    file_path = pdf_name
elif os.path.exists(f"pages/{pdf_name}"):
    file_path = f"pages/{pdf_name}"

if file_path:
    with st.container():
        st.markdown('<div class="elite-card">', unsafe_allow_html=True)
        col_info, col_dl = st.columns([4, 1])
        
        with col_info:
            # Ekranda güzel görünmesi için uzun ismini buraya yazıyoruz
            st.markdown(f"<h4 style='margin:0; color:#1a1a1a;'>Gastrointestinal ve Hepatolojik Aciller Pratik Kılavuzu</h4>", unsafe_allow_html=True)
            st.caption("Gastrointestinal ve hepatolojik acil durumlarda klinik yaklaşım rehberi.")
            
        with col_dl:
            with open(file_path, "rb") as f:
                st.download_button(
                    label="📥 İndir",
                    data=f,
                    file_name="Gastro_Aciller_Kilavuzu.pdf", # İndirilen dosyanın görünen adı
                    mime="application/pdf"
                )
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("⚠️ Dosya hala bulunamadı.")
    st.info(f"Lütfen GitHub'daki dosya adının tam olarak **{pdf_name}** olduğundan emin olun.")
    # Dosya listesini görmek için (Hata ayıklama):
    st.write("📂 Mevcut Dosyalar:", os.listdir('.'))