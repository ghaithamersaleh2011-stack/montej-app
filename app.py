
import streamlit as st

# بيانات الدفع الأساسية
MANAGER_NAME = "منال ابو ستة"
MANAGER_PHONE = "81146047"

st.set_page_config(page_title="Montej App", layout="wide")

# نظام الدخول البسيط
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🚀 مرحباً بك في Montej")
    email = st.text_input("البريد الإلكتروني")
    password = st.text_input("كلمة المرور", type="password")
    if st.button("دخول"):
        st.session_state.logged_in = True
        st.rerun()
else:
    st.title("🌟 منصة Montej للخدمات الذكية")
    tabs = st.tabs(["🛒 الخدمات", "💎 Montej Pass", "💰 شحن الرصيد"])

    with tabs[0]:
        st.subheader("خدماتنا الذكية")
        cols = st.columns(2)
        services = ["كتابة محتوى ($5)", "تصميم صور AI ($7)", "برمجة ($10)", "ترجمة ($4)"]
        for i, s in enumerate(services):
            cols[i%2].info(s)

    with tabs[1]:
        st.subheader("اشتراكات Montej Pass (PS Plus Style)")
        st.write("Essential ($15) | Pro ($35) | Professional ($60)")

    with tabs[2]:
        st.subheader("💰 شحن الرصيد عبر Western Union")
        st.success(f"الاسم: {MANAGER_NAME} | الرقم: {MANAGER_PHONE}")
        st.file_uploader("ارفع صورة إيصال الحوالة")
        if st.button("تأكيد الإرسال"):
            st.success("تم الإرسال للمدير!")

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()
