import streamlit as st

# بيانات الدفع الثابتة
MANAGER_NAME = "منال ابو ستة"
MANAGER_PHONE = "81146047"

st.set_page_config(page_title="Montej App", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 تسجيل الدخول - Montej")
    email = st.text_input("البريد الإلكتروني")
    password = st.text_input("كلمة المرور", type="password")
    if st.button("دخول"):
        st.session_state.logged_in = True
        st.rerun()
else:
    st.sidebar.title("👤 حسابي")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🚀 منصة Montej")
    tabs = st.tabs(["🛒 الخدمات", "💎 Montej Pass", "💰 شحن الرصيد", "🤖 المساعد AI"])

    with tabs[0]:
        st.subheader("الخدمات الذكية")
        cols = st.columns(2)
        services = ["كتابة محتوى ($5)", "تصميم صور ($7)", "برمجة ($10)", "ترجمة ($4)"]
        for i, s in enumerate(services):
            cols[i%2].info(s)
            if cols[i%2].button(f"طلب {s}", key=f"srv_{i}"):
                st.warning("يرجى التأكد من وجود رصيد كافٍ")

    with tabs[1]:
        st.subheader("باقات الاشتراك")
        c1, c2, c3 = st.columns(3)
        c1.metric("Essential", "15$")
        c2.metric("Pro 🏆", "35$")
        c3.metric("Professional 💎", "60$")

    with tabs[2]:
        st.subheader("💰 شحن الرصيد")
        st.success(f"الاسم: {MANAGER_NAME} | الرقم: {MANAGER_PHONE}")
        st.file_uploader("ارفع صورة وصل Western Union")
        if st.button("إرسال الوصل"):
            st.success("تم الإرسال للمدير للمراجعة.")

    with tabs[3]:
        st.subheader("🤖 Montej AI")
        st.text_input("كيف يمكنني مساعدتك؟")
