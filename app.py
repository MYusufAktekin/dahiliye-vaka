import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="NEJM İnteraktif Vaka", page_icon="🏥", layout="centered")

# Session State (Kullanıcının hangi aşamada olduğunu takip eder)
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def next_stage():
    st.session_state.stage += 1
    st.rerun()

def restart():
    st.session_state.stage = 0
    st.rerun()

# --- HEADER ---
st.title("🏥 Vaka 5-2026: Baş Ağrısı ve Hipertansiyon")
st.markdown("**Kaynak:** *NEJM Case Records of the Massachusetts General Hospital*")
st.markdown("---")

# --- SIDEBAR (Sabit Hasta Bilgileri) ---
with st.sidebar:
    st.header("📋 Hasta Dosyası")
    st.info("**Hasta:** 18 Yaşında, Kadın")
    
    if st.session_state.stage >= 1:
        st.write("---")
        st.write("**⚠️ Vital Bulgular (Acil):**")
        st.write("TA: **207/143 mmHg**")
        st.write("Nabız: 102/dk")
        st.write("Sat: %96")
        
    if st.session_state.stage >= 2:
        st.write("---")
        st.write("**🧪 Kritik Lab:**")
        st.write("Potasyum: **2.0 mmol/L** ⬇️")
        st.write("Kreatinin: 1.19 -> 0.87 mg/dL")
        st.write("Renin: **150 ng/mL/hr** ⬆️⬆️")
        st.write("Aldosteron: 4.1 ng/dL")

# --- AŞAMA 0: BAŞLANGIÇ ---
if st.session_state.stage == 0:
    st.subheader("1. Bölüm: Başvuru Hikayesi")
    st.write("""
    18 yaşında kadın hasta, **kötüleşen baş ağrısı** ve **hipertansiyon** şikayetiyle acile başvuruyor.
    
    **Öykü:**
    * 6 yıldır aralıklı baş ağrıları var (Migren/Gerilim tipi denmiş).
    * Son 1 yıldır sabahları olan, uykudan uyandıran baş ağrıları artmış.
    * 1 yıl önceki bir ölçümde TA: **164/100 mmHg** görülmüş ancak o anki ağrıya bağlanmış.
    * İlaçlar: Oral kontraseptif (OKS), NSAID, Triptanlar.
    
    **Fizik Muayene:**
    * Göz dibinde **Papilödem** saptanıyor.
    * Nörolojik muayene normal.
    """)
    
    st.warning("Bu aşamada hastaya dış merkezde LP (Lumber Ponksiyon) yapılıyor: Açılış basıncı 36 cmH2O (Yüksek). BOS biyokimyası normal.")
    
    st.info("❓ **SORU 1:** Bu tablo (Genç obez hasta, baş ağrısı, papilödem, yüksek BOS basıncı) size ilk planda hangi tanıyı düşündürür?")
    
    tani = st.radio("Ön Tanınız:", 
             ["Viral Menenjit", 
              "İdiyopatik İntrakraniyal Hipertansiyon (Psödotümör Serebri)", 
              "Subaraknoid Kanama", 
              "Temporal Arterit"])
    
    if st.button("Cevabı Onayla"):
        if tani == "İdiyopatik İntrakraniyal Hipertansiyon (Psödotümör Serebri)":
            st.success("✅ Doğru! İlk planda bu düşünüldü. Asetazolamid başlandı.")
            time.sleep(1)
            st.markdown("### 🚨 AMA BİR SORUN VAR...")
            st.write("Hasta birkaç gün sonra **Akciğer Ödemi** tablosu ve **207/143 mmHg** tansiyon ile tekrar geldi!")
            st.button("Vakayı Derinleştir ➡️", on_click=next_stage)
        else:
            st.error("❌ Yanlış. Papilödem ve yüksek açılış basıncı ile genç kadın hastada IIH ön plandadır ama hikaye burada bitmiyor...")

# --- AŞAMA 1: KRİZ VE LAB ---
elif st.session_state.stage == 1:
    st.subheader("2. Bölüm: Hipertansif Kriz ve Hipokalemi")
    st.error("Hasta ACİL SERVİSTE. TA: 207/143 mmHg. Akciğer ödemi bulguları var.")
    
    st.write("""
    Yoğun bakıma alınıyor. İnvaziv monitörizasyon yapılıyor.
    Lab sonuçları çıkıyor ve çok kritik bir bulgu var:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Sodyum", value="132 mmol/L")
        st.metric(label="Potasyum", value="2.0 mmol/L", delta="-1.4 (Kritik Düşük)", delta_color="inverse")
    with col2:
        st.metric(label="Kreatinin", value="0.87 mg/dL")
        st.metric(label="Metanefrinler", value="Normal")

    st.info("❓ **SORU 2:** Ciddi Hipertansiyon + Hipokalemi (K: 2.0). Bu ikiliyi görünce aklına gelmesi gereken 'Büyük 3'lü' ayırıcı tanı nedir?")
    
    secenek2 = st.selectbox("Tanı grubunu seçin:", 
                            ["Seçiniz...", 
                             "Renal Arter Stenozu / Hiperaldosteronizm / Cushing-Liddle", 
                             "Hipotiroidi / Addison / Tip 1 Diyabet", 
                             "SLE / Romatoid Artrit / Vaskülit"])
    
    if secenek2 == "Renal Arter Stenozu / Hiperaldosteronizm / Cushing-Liddle":
        st.success("✅ Kesinlikle. Mineralokortikoid fazlalığı (Aldosteron etkisi) düşünmeliyiz.")
        st.write("""
        **Ekarte Edilenler:**
        * Metanefrin normal -> Feokromasitoma dışlandı.
        * Cushing stigmata yok -> Dışlandı.
        * Renal USG Doppler normal -> Renal Arter Stenozu (FMD) daha düşük ihtimal ama hala masada.
        """)
        st.button("İleri Tetkik İste ➡️", on_click=next_stage)

# --- AŞAMA 2: İLERİ TETKİK VE GÖRÜNTÜLEME ---
elif st.session_state.stage == 2:
    st.subheader("3. Bölüm: Renin - Aldosteron Aksı")
    st.write("Hormon paneli istediniz ve sonuçlar geldi:")
    
    st.markdown("""
    * **Plazma Renin Aktivitesi:** `150 ng/mL/hr` (Normal: 1.2 - 2.4) 😱 **(AŞIRI YÜKSEK)**
    * **Aldosteron:** `4.1 ng/dL` (Normal: <21) **(NORMAL/DÜŞÜK?)**
    """)
    
    st.warning("""
    🤔 **Düşünme Zamanı:** Primer Hiperaldosteronizmde (Conn Sendromu), Renin BASKILANMIŞ (<1) olurdu.
    Burada Renin çok yüksek. Demek ki böbrek "susuz kaldığını" sanıyor veya otonom renin salgılıyor.
    """)
    
    # --- RESİM EKLEME BÖLÜMÜ ---
    import os
    if os.path.exists("bt.png"):
        st.image("bt.png", caption="Şekil 2: Sol Böbrekte Hipodens Kitle (Ok ile gösterilen alan)", use_container_width=True)
    else:
        # Resim yoksa internetten temsili bir resim göster
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqO0N62u0O-J9gwOETEqFSryZDvlU3SrR6ow&s", caption="Temsili BT Görüntüsü (Dosya bulunamadı)")
    # ---------------------------

    st.info("❓ **SORU 3:** Genç hasta + Hipertansiyon + Hipokalemi + Yüksek Renin + Böbrekte Kitle. Tanınız nedir?")
    
    tani_final = st.radio("Kesin Tanı:", 
                          ["Renal Hücreli Karsinom (RCC)", 
                           "Reninoma (Jukstaglomerüler Hücre Tümörü)", 
                           "Anjiomiyolipom", 
                           "Wilms Tümörü"])
    
    if st.button("Tanıyı Koy"):
        if tani_final == "Reninoma (Jukstaglomerüler Hücre Tümörü)":
            st.balloons()
            st.success("🎉 TEBRİKLER! Doğru Tanı: RENİNOMA")
            st.markdown("""
            **Vaka Çözümü:**
            Hasta Robotik Parsiyel Nefrektomiye alındı.
            Patoloji: **Jukstaglomerüler Hücre Tümörü (Reninoma)**.
            
            **Sonuç:**
            Ameliyat sonrası tansiyonları ilaçsız normale döndü. Potasyum düzeldi.
            """)
            st.button("Özet ve Dersler ➡️", on_click=next_stage)
        else:
            # DİKKAT: Buradaki else, if tani_final'in hizasında olmalı (içeride)
            st.error("❌ Yanlış. RCC en sık böbrek tümörüdür ama bu kadar yüksek Renin salgılamaz ve ciddi hipokalemi yapmaz. Tekrar düşün.")

# --- AŞAMA 3: EVE GÖTÜRÜLECEK MESAJLAR ---
elif st.session_state.stage == 3:
    st.header("📚 Eve Götürülecek Mesajlar")
    st.success("Vaka Başarıyla Tamamlandı.")
    
    st.markdown("""
    1.  **Genç Hipertansiyonu Ciddiye Alın:** 18 yaşında (hatta 40 yaş altı) birinde hipertansiyon varsa "Esansiyel" demeden önce mutlaka sekonder nedenleri araştır.
    2.  **Hipokalemi İpucudur:** Hipertansif bir hastada sebepsiz hipokalemi varsa (diüretik kullanımı yoksa) mutlaka **Renin-Aldosteron** bak.
    3.  **Reninoma Nadirdir ama Öğreticidir:**
        * **Primer Hiperaldosteronizm:** Düşük Renin / Yüksek Aldosteron.
        * **Sekonder Hipertansiyon (Renovasküler/Reninoma):** Yüksek Renin / Yüksek Aldosteron.
        *(Not: Bu vakada aldosteronun normal sınırlarda çıkması şaşırtıcıydı ama devasa renin seviyesi tanıyı koydurdu.)*
    4.  **IIH Yanıltabilir:** Hastanın göz dibi bulguları (papilödem) hipertansif ensefalopatiye bağlı olabilir, hemen psödotümör demeyin.
    """)
    
    if st.button("🔄 Başka Vaka İçin Başa Dön", on_click=restart):
        pass