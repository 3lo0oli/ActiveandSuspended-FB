import streamlit as st

st.set_page_config(page_title="Active & Suspended FB", layout="wide")

st.title("✅ Active & Suspended FB")
st.write("لو شايف الرسالة دي يبقى Streamlit شغال تمام 🎉")

name = st.text_input("اكتب اسمك")
if name:
    st.success(f"أهلاً يا {name} 👋")
