import streamlit as st
from datetime import datetime

# --- 1. PREMIUM KONFİGÜRASYON ---
st.set_page_config(
    page_title="AU Dahiliye Portal",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ELITE CSS (MODERN UI/UX ARCHITECTURE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Bricolage+Grotesque:wght@800&display=swap');

    /* Temel Ayarlar */
    .stApp {
        background: #fcfcfd;
        font-family: 'Outfit', sans-serif;
    }

    /* Sidebar Gizleme */
    [data-testid="stSidebarNav"] {display: none !important;}

    /* Modern Hero Banner (Immersive Design) */
    .hero-container {
        background: linear-gradient(145deg, #8A1538 0%, #5a0e24 100%);
        padding: 80px 60px;
        border-radius: 40px;
        color: white;
        margin-bottom: 50px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 30px 60px rgba(138, 21, 56, 0.18);
    }
    
    .hero-container::before {
        content: "";
        position: absolute;
        top: -100px;
        right: -100px;
        width: 300px;
        height: 300px;
        background: rgba(255,255,255,0.03);
        border-radius: 50%;
    }

    .hero-tag {
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-size: 0.75rem;
        opacity: 0.8;
        margin-bottom: 10px;
    }

    .hero-title {
        font-family: 'Bricolage Grotesque', sans-serif;
        font-size: 3.5rem;
        line-height: 1;
        margin: 0;
    }

    /* Floating Elite Cards */
    .elite-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        border: 1px solid rgba(0,0,0,0.03);
        box-shadow: 0 15px 35px rgba(0,0,0,0.02);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        margin-bottom: 30px;
    }
    
    .elite-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 25px 50px rgba(138, 21, 56, 0.06);
        border-color: rgba(138, 21, 56, 0.1);
    }

    /* Section Headings */
    .section-label {
        color: #8A1538;
        font-weight: 800;
        font-size: 1.2rem;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Custom Button (Premium Feeling) */
    div.stButton > button {
        background: #8A1538 !important;
        color: white !important;
        border-radius: 16px !important;
        border: none !important;
        padding: 18px 32px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 20px rgba(138, 21, 56, 0.15) !important;
    }
    
    div.stButton > button:hover {
        background: #1a1a1a !important;
        transform: scale(1.02);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1) !important;
    }

    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. ÖZEL NAVİGASYON (SIDEBAR) ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 🏛️ Portal Navigasyonu")
    st.write("---")
    if st.button("🏠 Ana Sayfa Dashboard", use_container_width=True):
        st.rerun()
    
    with st.expander("🩺 İnteraktif Vakalar", expanded=True):
        if st.button("Vaka 1: 18Y Kadın (HT)", use_container_width=True):
            st.switch_page("pages/1_📅_16_Subat_Vakasi.py")
    
    st.markdown("<br><br>" * 5, unsafe_allow_html=True)
    st.caption("Ankara Üniversitesi Tıp Fakültesi İç Hastalıkları")

# --- 4. ANA EKRAN TASARIMI ---

# Hero Section
st.markdown("""
<div class="hero-container">
    <div style="display: flex; align-items: center; gap: 40px;">
        <img src="https://upload.wikimedia.org/wikipedia/tr/6/64/Ankara_Universitesi_Logosu.png" width="120" style="filter: brightness(0) invert(1);">
        <div>
            <p class="hero-tag">Ankara Üniversitesi Tıp Fakültesi</p>
            <h1 class="hero-title">İç Hastalıkları<br>Eğitim Portalı</h1>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Grid Layout
col_left, col_right = st.columns([1.8, 1], gap="large")

with col_left:
    # Günün Vakası - Elite Card
    st.markdown('<div class="section-label"><span>📌</span> GÜNÜN ÖNE ÇIKAN VAKASI</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card">
        <h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-size: 2.2rem; margin-bottom: 20px; color: #1a1a1a;">
            Vaka 1: Baş Ağrısı ve Hipertansiyon ile Başvuran 18 Yaş Kadın Hasta
        </h2>
        <p style="font-size: 1.1rem; color: #555; line-height: 1.7; margin-bottom: 30px;">
            Dirençli hipertansiyon ve eşlik eden hipokalemi kliniği ile başvuran genç hastanın tanısal algoritmasını interaktif olarak yönetin.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Vakayı Çözmeye Başla →"):
        st.switch_page("pages/1_📅_16_Subat_Vakasi.py")

    # Eğitim Materyalleri
    st.markdown('<div style="margin-top: 60px;" class="section-label"><span>📚</span> GÜNCEL EĞİTİM MATERYALLERİ</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card" style="border-style: dashed; background: transparent;">
        <p style="text-align: center; color: #aaa; padding: 20px 0;">Henüz yüklenmiş bir döküman bulunmamaktadır.</p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # Duyurular - Elite Card
    st.markdown('<div class="section-label"><span>📢</span> DUYURULAR</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card" style="background: #fdfdfd; border-left: 6px solid #8A1538;">
        <div style="margin-bottom: 25px;">
            <p style="font-weight: 700; color: #1a1a1a; margin-bottom: 5px; font-size: 1.1rem;">📋 Çalışma Listesi</p>
            <p style="color: #666; font-size: 0.95rem;">Mart Ayı Çalışma Listesi Açıklandı.</p>
        </div>
        <hr style="opacity: 0.1; margin: 20px 0;">
        <div>
            <p style="font-weight: 700; color: #1a1a1a; margin-bottom: 5px; font-size: 1.1rem;">🎙️ HarrisonTalks</p>
            <p style="color: #666; font-size: 0.95rem;">Birinci Bölümüyle 18 Şubat Çarşamba günü başlıyor.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hızlı Araçlar
    st.markdown('<div class="section-label"><span>🛠️</span> HIZLI ARAÇLAR</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card">
        <p style="color: #888; font-style: italic; font-size: 0.9rem;">Klinik hesaplayıcılar ve MedCalc entegrasyonu yakında eklenecektir.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 100px; padding: 40px; color: #bbb; font-size: 0.85rem; border-top: 1px solid #f0f0f0;">
    © 2026 Ankara Üniversitesi Tıp Fakültesi İç Hastalıkları Ana Bilim Dalı
</div>
""", unsafe_allow_html=True)