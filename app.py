import streamlit as st
import base64
import os
import calendar
from datetime import datetime

# --- 1. YARDIMCI FONKSİYONLAR ---
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# --- 2. PREMIUM KONFİGÜRASYON ---
st.set_page_config(
    page_title="AU İç Hastalıkları Portalı",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 3. ELITE PRO CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Bricolage+Grotesque:wght@800&display=swap');

    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }

    .stApp { background: #fcfcfd; font-family: 'Outfit', sans-serif; }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(145deg, #8A1538 0%, #5a0e24 100%);
        padding: 50px 70px;
        border-radius: 35px;
        color: white;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 40px;
        box-shadow: 0 20px 40px rgba(138, 21, 56, 0.15);
    }
    .hero-title { font-family: 'Bricolage Grotesque', sans-serif; font-size: 2.8rem; margin: 0; line-height: 1.1; }

    /* Kart Yapısı */
    .elite-card {
        background: white;
        padding: 40px;
        border-radius: 32px;
        border: 1px solid rgba(0,0,0,0.04);
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        margin-bottom: 30px;
        transition: 0.3s;
    }
    .elite-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.05); }

    .section-label { 
        color: #8A1538; font-weight: 800; font-size: 0.85rem; letter-spacing: 2px;
        margin-bottom: 25px; display: flex; align-items: center; gap: 12px; text-transform: uppercase;
    }

    /* --- TAKVİM CSS --- */
    .calendar-container {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 10px;
        margin-top: 15px;
    }
    .day-header {
        text-align: center; color: #8A1538; font-weight: 700; font-size: 0.8rem;
        padding-bottom: 5px; border-bottom: 2px solid rgba(138,21,56,0.1); text-transform: uppercase;
    }
    .day-cell {
        background: #fcfcfc; border-radius: 12px; min-height: 100px; padding: 10px;
        border: 1px solid #eee; display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.2s;
    }
    .day-cell:hover { border-color: #8A1538; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .day-number { font-weight: 800; font-size: 1.1rem; color: #ddd; }
    .day-active { background: white; border: 1px solid #8A1538; box-shadow: 0 4px 12px rgba(138,21,56,0.08); }
    .day-active .day-number { color: #8A1538; }
    .event-badge {
        background: #8A1538; color: white; font-size: 0.7rem; padding: 6px; border-radius: 6px;
        margin-top: 5px; line-height: 1.3;
    }
    .event-time { display: block; font-size: 0.6rem; opacity: 0.8; margin-bottom: 2px; border-bottom: 1px solid rgba(255,255,255,0.2); }
    .event-speaker { display: block; font-style: italic; opacity: 0.9; margin-top: 2px; font-weight: 400; font-size: 0.65rem;}

    /* Buton Tasarımları */
    div.stButton > button {
        background: #8A1538 !important; color: white !important; border-radius: 16px !important;
        border: none !important; padding: 14px 28px !important; font-weight: 700 !important; width: 100%;
    }
    div.stButton > button:hover { background: #1a1a1a !important; transform: scale(1.02); }

</style>
""", unsafe_allow_html=True)

# --- 4. ÜST PANEL ---
logo_base64 = get_base64_of_bin_file('autf_logo.png')
logo_html = f'<img src="data:image/png;base64,{logo_base64}" width="100">' if logo_base64 else ""

st.markdown(f"""
<div class="hero-container">
    {logo_html}
    <div>
        <div style="text-transform: uppercase; letter-spacing: 3px; font-size: 0.9rem; opacity: 0.8; margin-bottom: 10px; font-weight: 600;">Ankara Üniversitesi Tıp Fakültesi</div>
        <h1 class="hero-title">İç Hastalıkları Asistan Eğitimi Portalı</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HOŞ GELDİN KARTI ---
st.markdown("""
<div class="elite-card" style="text-align: center; padding: 40px 50px; border-bottom: 5px solid #8A1538;">
    <h3 style="font-family: 'Bricolage Grotesque', sans-serif; color: #1a1a1a; margin-bottom: 15px; font-size: 1.8rem;">
        Hoş Geldiniz
    </h3>
    <p style="font-size: 1.1rem; color: #555; line-height: 1.7; max-width: 900px; margin: 0 auto;">
        Bu platform, <b>Ankara Üniversitesi Tıp Fakültesi İç Hastalıkları</b> asistan eğitim programını desteklemek amacıyla oluşturulmuştur. 
        Günlük interaktif vakalar, güncel literatüre dayanan pratik kılavuzlar ve diğer eğitim materyalleri ile asistanlık sürecinizin her adımında yanınızdayız.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. ANA İÇERİK ---
col_left, col_right = st.columns([1.8, 1], gap="large")

with col_left:
    st.markdown('<div class="section-label"><span>📌</span> GÜNÜN ÖNE ÇIKAN VAKASI</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card">
        <h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-size: 2.3rem; margin-bottom: 20px; color: #1a1a1a;">
            Vaka 1: Baş Ağrısı ve Hipertansiyon ile Başvuran 18 Yaş Kadın Hasta
        </h2>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin-bottom: 30px;">
            Ankara Üniversitesi Tıp Fakültesi İç Hastalıkları asistanları için hazırlanan interaktif vaka modülüdür.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Vakayı Çözmeye Başla →"):
        # Dosyalar artık pages klasöründe olduğu için bu çalışacak
        st.switch_page("pages/1_vaka.py")

with col_right:
    # --- EĞİTİM MATERYALLERİ ---
    st.markdown('<div class="section-label"><span>📚</span> EĞİTİM MATERYALLERİMİZ</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="elite-card" style="padding: 35px; text-align: center;">
        <p style="color: #555; margin-bottom: 20px; line-height: 1.6;">
            Güncel kılavuzlar, sunumlar ve ders notlarına arşivden ulaşabilirsiniz.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Arşive Git →"):
        # Dosyalar artık pages klasöründe olduğu için bu çalışacak
        st.switch_page("pages/2_materyal.py")


# --- 6. ÖZEL TAKVİM ALANI ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-label"><span>🗓️</span> ŞUBAT 2026 EĞİTİM FAALİYETLERİMİZ</div>', unsafe_allow_html=True)

events = {
    18: {"title": "HarrisonTalks #1", "speaker": "Uzm.Dr. R.F. Aydın", "time": "20:00"},
    24: {"title": "HarrisonTalks #2", "speaker": "Dr. Barış Bahçekapılı", "time": "20:00"},
    25: {"title": "HarrisonTalks #3", "speaker": "Dr. M.Y. Aktekin", "time": "20:00"}
}

cal = calendar.Calendar(firstweekday=0)
month_days = cal.monthdayscalendar(2026, 2)
weekdays = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]

calendar_html = '<div class="elite-card"><div class="calendar-container">'

for day in weekdays:
    calendar_html += f'<div class="day-header">{day}</div>'

for week in month_days:
    for day in week:
        if day == 0:
            calendar_html += '<div class="day-cell" style="background:transparent; border:none;"></div>'
        else:
            if day in events:
                e = events[day]
                calendar_html += f"""<div class="day-cell day-active"><div class="day-number">{day}</div><div class="event-badge"><span class="event-time">{e['time']}</span>{e['title']}<span class="event-speaker">{e['speaker']}</span></div></div>"""
            else:
                calendar_html += f"""<div class="day-cell"><div class="day-number">{day}</div></div>"""

calendar_html += '</div></div>'
st.markdown(calendar_html, unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align: center; margin-top: 50px; padding: 40px; color: #bbb; font-size: 0.85rem; border-top: 1px solid #f0f0f0;'>© 2026 Ankara Üniversitesi Tıp Fakültesi İç Hastalıkları Ana Bilim Dalı</div>", unsafe_allow_html=True)