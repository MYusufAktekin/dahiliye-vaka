import streamlit as st

# Sayfa Ayarları
st.set_page_config(
    page_title="Ankara Tıp Dahiliye",
    page_icon="🩺",
    layout="centered"
)

# Başlık ve Logo Bölümü
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# Eğer internetten logo çekeceksen (Ankara Üni Logosu):
st.image("https://upload.wikimedia.org/wikipedia/tr/6/64/Ankara_Universitesi_Logosu.png", width=150)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #8A1538;'>Ankara Üniversitesi Tıp Fakültesi</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #333;'>İç Hastalıkları Ana Bilim Dalı</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>İnteraktif Vaka Platformu</h3>", unsafe_allow_html=True)

st.markdown("---")

st.info("""
👋 **Hoşgeldiniz Dr. Arkadaşım,**

Bu platform, asistan eğitimi için günlük pratik vakalar sunmak amacıyla hazırlanmıştır.
Soldaki menüden **"Günün Vakası"nı** veya geçmiş vakaları seçerek çözmeye başlayabilirsin.

**Bugünün Özeti:**
* 📅 **16 Şubat:** Dirençli Hipertansiyon ve Hipokalemi (NEJM)
""")

st.success("👈 Lütfen sol menüden bir vaka seçiniz.")