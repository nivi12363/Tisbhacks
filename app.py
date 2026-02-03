import streamlit as st

st.set_page_config(page_title="EcoLens", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.block-container { padding-top: 1rem !important; }

/* Sticky header box */
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 999;
  background: #0e1117;   /* dark theme background */
  padding: 0.5rem 0 0.75rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Navigation state
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(page_name: str):
    st.session_state.page = page_name

# -------------------------
# Sticky header (always visible)
# -------------------------
st.markdown('<div class="sticky-header">', unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="text-align:center; font-size:72px; margin:0;">
        🌱 EcoLens
    </h1>
    <p style="text-align:center; font-size:18px; opacity:0.85; margin-top:6px; margin-bottom:14px;">
        Make smarter, sustainable buying decisions
    </p>
    """,
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns([1, 1, 1])
with c1:
    st.button("🌿 GreenScore", use_container_width=True, on_click=go, args=("GreenScore",))
with c2:
    st.button("🤖 AI Chatbot", use_container_width=True, on_click=go, args=("Chatbot",))
with c3:
    st.button("Total Impact", use_container_width=True, on_click=go, args=("Impact",))
with c4:
    st.button("ℹ️ About", use_container_width=True, on_click=go, args=("About",))

st.markdown("</div>", unsafe_allow_html=True)
st.write("")  # spacer

# -------------------------
# HOME
# -------------------------
if st.session_state.page == "Home":

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
        EcoLens helps eco-conscious shoppers identify truly sustainable products by providing clear insights into a product`s sustainability impact.
        Scan a product, detect greenwashing, and get a clear **Green Score** with reasons.
        """)

    st.header("🚨 The Problem")
    st.write("Sustainability labels are vague and poorly regulated, so consumers often rely on marketing language instead of real data. Many of these claims are misleading, allowing greenwashing to go unnoticed. Because people lack the time and expertise to properly assess environmental impact, they make well-intentioned but poor choices. Additionally, there is no standardized way to verify eco-claims, and most existing apps reduce sustainability to simple green or red labels, hiding the real environmental costs of everyday products. As a result, people want to buy more environmentally friendly products but struggle to know which ones truly are.")
    

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
# TOTAL IMPACT PAGE
# -------------------------
elif st.session_state.page == "Impact":
    st.button("← Back to Home", on_click=go, args=("Home",))
    st.title("Total Impact")

    st.write("Find out the environmental impact of your choices, and discover ways to increase your eco-friendliness")
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

