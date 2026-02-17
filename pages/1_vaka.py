import streamlit as st
import time

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="Vaka 1: 18 Yaş Kadın Hasta",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS (Ana Sayfa ile Uyumlu Elite Pro Tasarım) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Bricolage+Grotesque:wght@800&display=swap');
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background: #fcfcfd; font-family: 'Outfit', sans-serif; }
    
    .hero-title { font-family: 'Bricolage Grotesque', sans-serif; font-size: 2.2rem; color: #1a1a1a; margin-bottom: 10px; }
    .section-header { font-family: 'Bricolage Grotesque', sans-serif; font-size: 1.5rem; color: #8A1538; margin-top: 30px; margin-bottom: 15px; border-left: 5px solid #8A1538; padding-left: 15px; }
    
    .doctor-reasoning { background: #fdf2f5; padding: 25px; border-radius: 15px; border: 1px solid rgba(138,21,56,0.1); margin-top: 15px; font-style: italic; color: #555; line-height: 1.6; }
    .doctor-reasoning-title { font-weight: 800; color: #8A1538; font-size: 0.9rem; margin-bottom: 10px; display: block; text-transform: uppercase; }
    
    .lab-table { width: 100%; border-collapse: collapse; font-size: 0.95rem; margin-bottom: 15px; }
    .lab-table td { padding: 8px; border-bottom: 1px solid #eee; }
    .lab-table th { text-align: left; padding: 8px; border-bottom: 2px solid #8A1538; color: #8A1538; }
    .abnormal { color: #d9534f; font-weight: 700; }
    
    .back-link { text-decoration: none; color: #666; font-weight: 600; display: inline-block; margin-bottom: 20px; }
    
    div.stButton > button { background: #8A1538; color: white; border-radius: 10px; padding: 10px 25px; font-weight: 600; border: none; }
    div.stButton > button:hover { background: #1a1a1a; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<a href="/" class="back-link">← Ana Sayfaya Dön</a>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Vaka 1: Baş Ağrısı ve Hipertansiyon ile Başvuran 18 Yaş Kadın Hasta</h1>', unsafe_allow_html=True)
st.caption("Kaynak: NEJM Case Records 5-2026 (12 Şubat 2026) | Uyarlayan: AUTF İç Hastalıkları")

# --- STATE YÖNETİMİ ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# --- BÖLÜM 1: ÖYKÜ VE BAŞVURU ---
st.markdown('<div class="section-header">1. Öykü ve Acil Servis Başvurusu</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
    **Mevcut Şikayet:** Şiddetlenen baş ağrısı, bulantı ve fotofobi.
    
    **Öykü:**
    6 yıldır aralıklı baş ağrıları (Tansiyon/Migren tanılı) mevcut. Son 1 yıldır ağrılar günlük hale gelmiş. Sabahları uykudan uyandıran, zonklayıcı tarzda bir ağrı tarifliyor.
    
    **Önceki Kritik Değerlendirme:**
    Yakın zamanda dış merkez Nöroloji tarafından görülmüş. KB: 164/100 mmHg ölçülmüş ancak ağrıya bağlanmış. Göz dibinde **Papilödem** saptanmış. Lomber Ponksiyon (LP) açılış basıncı 36 cmH2O bulunarak **İdiyopatik İntrakraniyal Hipertansiyon (IIH)** (Psödotümör Serebri) tanısı konmuş ve Asetazolamid başlanmış.
    
    **Acil Servis Başvurusu (Güncel):**
    İlaçlara yanıtsız, "ezici" tarzda baş ağrısı ile başvurdu.
    <br><br>
    **KB:** 207/143 mmHg
    <br>
    **Akciğer:** Oskültasyonda bazallerde raller. Akciğer grafisinde perihiler dolgunluk (Pulmoner Ödem).
    <br>
    **EKG:** Sinüs taşikardisi, Sol Ventrikül Hipertrofisi (LVH) bulguları, inferoapikal ST depresyonları.
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="doctor-reasoning">
        <span class="doctor-reasoning-title">💡 Klinik Tartışma (Dr. Fadakar)</span>
        Bu hasta "İdiyopatik İntrakraniyal Hipertansiyon" tanısı almış olsa da, şu anki tablosu (Hipertansif Kriz + Akciğer Ödemi) durumu değiştiriyor. 
        <br><br>
        IIH tanısı genellikle bir dışlama tanısıdır. Ancak 18 yaşında bir hastada diyastolik tansiyonun 140'lara çıkması ve <b>Uç Organ Hasarı</b> (Papilödem, Pulmoner Ödem, LVH) gelişmesi, bizi mutlaka sistemik bir nedene, yani <b>Sekonder Hipertansiyon</b> nedenlerine götürmelidir. Papilödem, IIH'den ziyade Malign Hipertansiyonun bir sonucu olabilir.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Soru 1 ---
st.subheader("❓ İlk Yaklaşım ve Ayırıcı Tanı")
q1 = st.radio(
    "18 yaşında hipertansif kriz ve akciğer ödemi ile gelen bu hastada, ayırıcı tanıda İLK dışlanması gereken ana gruplar hangileridir?",
    ["Sadece Esansiyel Hipertansiyon ve Migren", "Renal Parankimal Hastalıklar ve Renovasküler Nedenler", "Psikojenik Polidipsi", "Basit Vitamin D Eksikliği"],
    index=None
)

if q1 == "Renal Parankimal Hastalıklar ve Renovasküler Nedenler":
    st.success("Doğru. Genç hastalarda sekonder HT'nin en sık nedenleri renal (parankimal veya vasküler) kökenlidir.")
    if st.button("Laboratuvar Sonuçlarını Gör"):
        st.session_state.stage = 1
elif q1:
    st.warning("Tekrar düşünün. Genç yaşta malign hipertansiyon ve organ hasarı (akciğer ödemi, papilödem) varlığında sistemik ve özellikle renal nedenler araştırılmalıdır.")

# --- BÖLÜM 2: LABORATUVAR BULGULARI ---
if st.session_state.stage >= 1:
    st.markdown('<div class="section-header">2. Kritik Laboratuvar Bulguları</div>', unsafe_allow_html=True)
    
    col_lab, col_clue = st.columns([1.5, 1])
    
    with col_lab:
        st.markdown("""
        <table class="lab-table">
            <tr><th>Test</th><th>Sonuç</th><th>Referans Aralığı</th></tr>
            <tr><td>Kreatinin</td><td>1.19 mg/dL (Hidrasyon sonrası 0.87)</td><td>0.5-1.5</td></tr>
            <tr><td>Sodyum (Na)</td><td>132 mmol/L</td><td>135-145</td></tr>
            <tr><td class="abnormal">Potasyum (K)</td><td class="abnormal">2.0 mmol/L (KRİTİK DÜŞÜK)</td><td>3.4-5.0</td></tr>
            <tr><td>Bikarbonat</td><td>26 mmol/L</td><td>23-32</td></tr>
            <tr><td>Troponin T</td><td>43 ng/L</td><td>0-9</td></tr>
            <tr><td>İdrar Tetkiki</td><td>Protein (2+)</td><td>Negatif</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with col_clue:
        st.markdown("""
        <div class="doctor-reasoning">
            <span class="doctor-reasoning-title">💡 Klinik İpucu (Dr. Pourvaziri)</span>
            Hastada <b>Şiddetli Hipokalemi (2.0 mmol/L)</b> ve Hipertansiyon birlikteliği var.
            <br>
            Diüretik kullanımı yoksa, bu tablo aksi ispat edilene kadar <b>Mineralokortikoid Fazlalığını</b> (RAAS aktivasyonu) işaret eder.
            <br><br>
            Ayırıcı tanı şu 3 ana başlıkta toplanır:
            1. <b>Primer Hiperaldosteronizm</b> (Conn Sendromu - Düşük Renin)
            2. <b>Sekonder Hiperaldosteronizm</b> (Renovasküler HT, Reninoma - Yüksek Renin)
            3. <b>Liddle Sendromu / Cushing</b> (Düşük Renin / Düşük Aldosteron)
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # --- Soru 2 ---
    st.subheader("❓ Tanısal Test Seçimi")
    q2 = st.selectbox(
        "Hipokalemik hipertansiyon etiyolojisini aydınlatmak için istenmesi gereken en kritik test hangisidir?",
        ["Seçiniz...", "24 Saatlik İdrar Kortizolü", "Plazma Renin Aktivitesi ve Aldosteron Konsantrasyonu", "Genetik Test Paneli", "Böbrek Biyopsisi"]
    )
    
    if q2 == "Plazma Renin Aktivitesi ve Aldosteron Konsantrasyonu":
        st.success("Kesinlikle. Renin düzeyi, tanıyı primer (böbrek üstü bezi kaynaklı) ve sekonder (böbrek/damar kaynaklı) nedenler arasında ayıracak anahtardır.")
        if st.button("Hormon ve Görüntüleme Sonuçlarını Aç"):
            st.session_state.stage = 2
    elif q2 != "Seçiniz...":
        st.info("Bu test ileride gerekebilir ancak şu an RAAS aksını değerlendirmek (Renin/Aldosteron) en öncelikli adımdır.")

# --- BÖLÜM 3: RAAS PROFİLİ VE GÖRÜNTÜLEME ---
if st.session_state.stage >= 2:
    st.markdown('<div class="section-header">3. Endokrin ve Radyolojik Değerlendirme</div>', unsafe_allow_html=True)
    
    st.info("""
    **RAAS Sonuçları:**
    **Plazma Renin Aktivitesi:** 150 ng/mL/saat (Çok Yüksek) (Normal: 1.2-2.4)
    **Plazma Aldosteron:** 4.1 ng/dL (Normal/Düşük) (Normal: <21)
    """)
    
    st.markdown("""
    <div class="doctor-reasoning">
        <span class="doctor-reasoning-title">💡 Dr. Fadakar'ın Yorumu</span>
        Renin'in bu kadar yüksek olması (Hiperreninemik Hipertansiyon), Liddle sendromu ve Primer Hiperaldosteronizm (Conn) gibi düşük reninle giden durumları kesin olarak eledi.
        <br><br>
        Normalde Aldosteronun da çok yüksek olmasını beklerdik (Sekonder Hiperaldo). Ancak Aldosteron normal sınırlarda geldi. Bu durum şiddetli hipokaleminin aldosteron sentezini baskılamasına bağlanabilir. Klinik tablo net olarak <b>Renin Bağımlı Hipertansiyon</b> ile uyumlu.
        <br><br>
        <b>En olası tanılar:</b> Renovasküler Hipertansiyon (FMD) veya Renin salgılayan tümör (Reninoma).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col_img_text, col_img_box = st.columns([1, 1])
    
    with col_img_text:
        st.subheader("Radyoloji Bulguları (BT Anjiyo)")
        st.markdown("""
        <b>Renal Arterler:</b> Bilateral tek renal arter, aksesuar arter yok. Stenoz (darlık) veya 'tesbih tanesi' (FMD) görünümü YOK.
        <br><br>
        <b>Böbrek Parankimi:</b> Sol böbrek interpolar bölgede hipodens, az kontrastlanan lezyon izlendi.
        <br><br>
        <b>MR Teyidi:</b> T1 ve T2 hipointens, 8 mm kistik komponenti olan lezyon.
        """, unsafe_allow_html=True)
        
    with col_img_box:
         st.markdown("""
        <div class="doctor-reasoning">
            <span class="doctor-reasoning-title">💡 Görüntüleme Yorumu</span>
            Renal arterlerin açık olması, genç kadınlarda en sık görülen sekonder neden olan Fibromusküler Displaziyi (FMD) dışladı. 
            Ancak böbrekte bir kitle var.
            <br>
            Genç hasta + Yüksek Renin + Renal Kitle = ?
        </div>
        """, unsafe_allow_html=True)

    # --- Soru 3 ---
    st.subheader("❓ Final Tanınız Nedir?")
    q3 = st.radio(
        "Tüm bulgular ışığında (Genç yaş + Hiperreninemi + Renal Arterler Açık + Renal Kitle) en olası tanı nedir?",
        ["Renal Hücreli Karsinom (RCC)", "Anjiyomiyolipom", "Reninoma (Jukstaglomerüler Hücreli Tümör)", "Wilms Tümörü"],
        index=None
    )
    
    if q3 == "Reninoma (Jukstaglomerüler Hücreli Tümör)":
        st.balloons()
        st.success("Tebrikler! Doğru Tanı.")
        if st.button("Tanı, Tedavi ve Patolojiyi Gör"):
            st.session_state.stage = 3
    elif q3:
        st.error("Düşünülen tümör, hastadaki 'aşırı renin' üretimini açıklamalıdır. RCC nadiren renin salgılasa da, bu klinik tabloda primer renin salgılayan tümör daha olasıdır.")

# --- BÖLÜM 4: FİNAL RAPORU ---
if st.session_state.stage >= 3:
    st.markdown('<div class="section-header">🏁 Final Tanı ve Patoloji</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🧬 Patolojik Tanı: Reninoma
    Hasta robotik parsiyel nefrektomiye alındı.
    <br><br>
    <b>Makroskopi:</b> İyi sınırlı, kapsüllü nodüler lezyon.
    <br>
    <b>Mikroskopi:</b> Poligonal iğsi hücreler.
    <br>
    <b>İmmünohistokimya:</b> CD34 (+), GATA3 (+) ve Renin (+).
    <br>
    <b>Elektron Mikroskopi:</b> Renin kristalleri (Rhomboid protogranüller) görüldü.
    """, unsafe_allow_html=True)
    
    st.info("""
    ### 📈 Klinik Seyir ve IIH İlişkisi
    * Tümör çıkarıldıktan sonra hastanın tansiyonu normale döndü, antihipertansifler kesildi.
    * Potasyum replasmanı ihtiyacı kalmadı.
    * **İlginç Patofizyolojik Bağlantı:** Yüksek Renin -> Yüksek Anjiyotensin II -> Aldosteron benzeri etkiyle koroid pleksustan BOS yapımını artırarak **Papilödem ve IIH (Psödotümör Serebri)** benzeri tabloya yol açtığı düşünüldü.
    * Operasyon sonrası görme alanı defektleri ve papilödem düzeldi.
    """)
    
    if st.button("Vaka Analizini Bitir"):
        st.switch_page("app.py")
