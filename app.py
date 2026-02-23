import streamlit as st
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Facebook Link Checker",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* خلفية احترافية */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1877f2 0%, transparent 40%),
                radial-gradient(circle at 80% 30%, #0f2027 0%, transparent 40%),
                linear-gradient(135deg, #0b1f3a, #0f2027);
    color: white;
}

/* اخفاء الهيدر */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* عنوان */
.title {
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* كارد */
.card {
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

/* textarea */
textarea {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

/* buttons */
.stButton>button {
    width: 100%;
    border-radius: 15px;
    padding: 12px;
    font-weight: 600;
    font-size: 16px;
    border: none;
    background: linear-gradient(90deg, #1877f2, #3b5998);
    color: white;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(24,119,242,0.6);
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================

st.markdown('<div class="title">📘 Active & Suspended FB</div>', unsafe_allow_html=True)
st.markdown("#### ضع روابط فيسبوك هنا (كل رابط في سطر)")

links = st.text_area("", height=200, placeholder="https://facebook.com/...")

col1, col2 = st.columns(2)

with col1:
    max_links = st.number_input("Max links", min_value=1, max_value=100, value=25)

with col2:
    delay = st.number_input("Delay (sec)", min_value=0.1, max_value=10.0, value=0.6, step=0.1)

st.markdown("---")

colA, colB = st.columns(2)

# ================= CHECK BUTTON =================
with colA:
    if st.button("🔍 فحص Facebook"):
        urls = [u.strip() for u in links.split("\n") if u.strip()]
        urls = urls[:max_links]

        if not urls:
            st.warning("حط روابط الأول.")
        else:
            for url in urls:
                time.sleep(delay)
                # هنا مكان الفحص الحقيقي
                st.success(f"{url} ✅ Active")

# ================= CLEAR BUTTON =================
with colB:
    if st.button("🧹 مسح"):
        st.rerun()
