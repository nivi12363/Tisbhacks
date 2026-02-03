import streamlit as st

st.set_page_config(page_title="EcoLens", page_icon="🌱", layout="wide")

# -------------------------
# Navigation state
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(page_name: str):
    st.session_state.page = page_name

# -------------------------
# HOME
# -------------------------
if st.session_state.page == "Home":
    # Big centered title
    st.markdown(
        """
        <h1 style="text-align:center; font-size:72px; margin-bottom: 0;">
            🌱 EcoLens
        </h1>
        <p style="text-align:center; font-size:18px; opacity:0.85; margin-top: 0;">
            Make smarter, sustainable buying decisions
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")  # spacer

    # "Tabs" / menu buttons centered
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.button("🌿 GreenScore", use_container_width=True, on_click=go, args=("GreenScore",))
    with c2:
        st.button("🤖 AI Chatbot", use_container_width=True, on_click=go, args=("Chatbot",))
    with c3:
        st.button("ℹ️ About", use_container_width=True, on_click=go, args=("About",))

    st.divider()

    # Home content like your sketch
    left, right = st.columns([1, 2])

    with left:
        st.image(
            "https://images.unsplash.com/photo-1542838132-92c53300491e",
            use_container_width=True
        )

    with right:
        st.subheader("What is EcoLens?")
        st.write("""
        EcoLens helps eco-conscious shoppers identify truly sustainable products.
        Scan a product, detect greenwashing, and get a clear **Green Score** with reasons.
        """)

    st.header("🚨 The Problem")
    st.write("Greenwashing and vague labels make it hard to choose products that are actually sustainable.")

    st.header("✅ Our Solution")
    st.write("EcoLens combines product scanning with transparent scoring and actionable recommendations.")

    st.header("✨ Key Features")
    f1, f2 = st.columns(2)
    with f1:
        st.subheader("🌿 GreenScore")
        st.write("- Barcode scan\n- Score + explanation\n- Better alternatives")
    with f2:
        st.subheader("🤖 AI Chatbot")
        st.write("- Ingredient explanations\n- Claim checks\n- Eco tips")

# -------------------------
# GREEN SCORE PAGE
# -------------------------
elif st.session_state.page == "GreenScore":
    st.button("← Back to Home", on_click=go, args=("Home",))
    st.title("🌿 GreenScore")

    st.write("Scan a product (start with barcode input for hackathon).")
    barcode = st.text_input("Enter barcode (EAN/UPC)")

    if st.button("Scan"):
        st.info("Next: call Open Food Facts API here and compute score.")

# -------------------------
# CHATBOT PAGE
# -------------------------
elif st.session_state.page == "Chatbot":
    st.button("← Back to Home", on_click=go, args=("Home",))
    st.title("🤖 AI Chatbot")

    st.write("Ask a question about sustainability, ingredients, and alternatives.")
    user_q = st.text_input("Your question")

    if st.button("Ask"):
        st.info("Next: connect to your chatbot logic / API.")

# -------------------------
# ABOUT PAGE
# -------------------------
elif st.session_state.page == "About":
    st.button("← Back to Home", on_click=go, args=("Home",))
    st.title("ℹ️ About")

    st.write("Built by **The Quantum Crew** for TISB Hacks.")

    st.subheader("👥 Team")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### Pihu Gupta")
        st.caption("Backend & APIs")

    with col2:
        st.markdown("### Saanvi Khetan")
        st.caption("ML & Scoring")

    with col3:
        st.markdown("### Sinita Ray")
        st.caption("UX & Frontend")

    with col4:
        st.markdown("### Nivedha Sundar")
        st.caption("Product & Pitch")

