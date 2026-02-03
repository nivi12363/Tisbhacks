import streamlit as st
import streamlit.components.v1 as components

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

c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
with c1:
    st.button("🌿 GreenScore", use_container_width=True, on_click=go, args=("GreenScore",))
with c2:
    st.button("🤖 AI Chatbot", use_container_width=True, on_click=go, args=("Chatbot",))
with c3:
    st.button("🌏Total Impact", use_container_width=True, on_click=go, args=("Impact",))
with c4:
    st.button("ℹ️ About", use_container_width=True, on_click=go, args=("About",))

st.markdown("</div>", unsafe_allow_html=True)
st.write("")  # spacer

# -------------------------
# HOME
# -------------------------
if st.session_state.page == "Home":

    left, right = st.columns([1.2, 1.8], gap="large")

    with left:
        st.markdown("""
            <div style="height:420px; overflow:hidden; border-radius:12px;">
                <img src="https://images.openai.com/static-rsc-3/L_9-L2VXhvFW5NZZvI6VLjA1QxHDiDeV5vyXsgKqM2ycJVtMFds_HEsJfhXYdziNs9fdDa4f0k4koZsaN3gehTxDddohscLt0wYAfwvMxRE?purpose=fullsize"
                     style="width:100%; height:100%; object-fit:cover;">
            </div>
        """, unsafe_allow_html=True)
    
    with right:
        st.markdown(
            """<div style="height:420px; display:flex; flex-direction:column; justify-content:center;">
    <h2 style="font-size:42px; margin-bottom:18px;">What is EcoLens?</h2>
    <p style="font-size:20px; line-height:1.7; max-width:680px;">
    EcoLens helps eco-conscious shoppers identify truly sustainable products by providing clear insights into a product’s sustainability impact.
    Scan a product, detect greenwashing, and get a clear <b>Green Score</b> with reasons.
    </p>
    </div>""",
            unsafe_allow_html=True
        )

    st.header("🚨 The Problem")
    st.write("Sustainability labels are vague and poorly regulated, so consumers often rely on marketing language instead of real data. Many of these claims are misleading, allowing greenwashing to go unnoticed. Because people lack the time and expertise to properly assess environmental impact, they make well-intentioned but poor choices. Additionally, there is no standardized way to verify eco-claims, and most existing apps reduce sustainability to simple green or red labels, hiding the real environmental costs of everyday products. As a result, people want to buy more environmentally friendly products but struggle to know which ones truly are.")
    

    st.header("✨ Key Features")

    components.html("""
<div style="
    background:#3f5a4d;
    border-radius:18px;
    padding:44px 38px;
    margin-top:18px;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial;
">
  <div style="display:flex; gap:34px; align-items:center;">

    <div style="flex:1.2;">
      <h2 style="margin:0 0 14px 0; font-size:38px; color:white;">
        🌿 GreenScore Tracker
      </h2>

      <p style="margin:0 0 14px 0; font-size:18px; line-height:1.7; color:rgba(255,255,255,0.92);">
        Scan personal-care products and get a transparent sustainability score with clear reasons.
      </p>

      <ul style="margin:0; padding-left:20px; font-size:18px; line-height:1.7; color:rgba(255,255,255,0.92);">
        <li>Barcode scan / product lookup</li>
        <li>Score breakdown (ingredients, packaging, claims)</li>
        <li>Greenwashing flags + simple explanations</li>
        <li>Better alternatives for your purpose</li>
      </ul>
    </div>

    <div style="flex:1; display:flex; justify-content:flex-end;">
      <div style="
          width:520px;
          height:320px;
          border-radius:16px;
          overflow:hidden;
          box-shadow: 0 10px 30px rgba(0,0,0,0.25);
          background: rgba(255,255,255,0.06);
      ">
        <img src="https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?auto=format&fit=crop&w=1400&q=80"
             style="width:100%; height:100%; object-fit:cover;">
      </div>
    </div>

  </div>
</div>
""", height=420)


    
    #-------------------------
    # AI Chatbot
    #-------------------------

    components.html("""
    <div style="
        background:#1f2f4a;   /* blueish */
        border-radius:18px;
        padding:44px 38px;
        margin-top:22px;
        font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial;
    ">
      <div style="display:flex; gap:34px; align-items:center;">
    
        <!-- LEFT IMAGE -->
        <div style="flex:1; display:flex; justify-content:flex-start;">
          <div style="
              width:520px;
              height:320px;
              border-radius:16px;
              overflow:hidden;
              box-shadow: 0 10px 30px rgba(0,0,0,0.30);
              background: rgba(255,255,255,0.06);
          ">
            <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1400&q=80"
                 style="width:100%; height:100%; object-fit:cover;">
          </div>
        </div>
    
        <!-- RIGHT TEXT -->
        <div style="flex:1.2;">
          <h2 style="margin:0 0 14px 0; font-size:38px; color:white;">
            🤖 AI Chatbot
          </h2>
    
          <p style="margin:0 0 14px 0; font-size:18px; line-height:1.7; color:rgba(255,255,255,0.92);">
            Ask questions in plain English and get smart, personalized sustainability advice instantly.
          </p>
    
          <ul style="margin:0; padding-left:20px; font-size:18px; line-height:1.7; color:rgba(255,255,255,0.92);">
            <li>Ask about ingredients and claims</li>
            <li>Detect greenwashing language</li>
            <li>Get product recommendations</li>
            <li>Tips for safer / sustainable swaps</li>
          </ul>
        </div>
    
      </div>
    </div>
    """, height=420)



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
    st.title("🌏Total Impact")

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

    # -----------------------------
    # Step 0: Define file paths
    # -----------------------------
    PRODUCT_CSV = "product.csv"
    MATERIAL_CSV = "material.csv"

    # -----------------------------
    # Step 1: Read CSV files
    # -----------------------------
    products_df = pd.read_csv(PRODUCT_CSV)
    materials_df = pd.read_csv(MATERIAL_CSV)

    # Convert material impact dataframe to dictionary
    material_impact_dict = {}
    for _, row in materials_df.iterrows():
        material_impact_dict[row['material']] = {
            'carbon': row['carbon_kg_per_kg'],
            'water': row['water_L_per_kg'],
            'energy': row['energy_MJ_per_kg'],
            'waste': row['waste_score']
        }

    # -----------------------------
    # Step 2: Initialize result columns
    # -----------------------------
    products_df['total_carbon_kg'] = 0.0
    products_df['total_water_L'] = 0.0
    products_df['total_energy_MJ'] = 0.0
    products_df['total_waste_score'] = 0.0

    # -----------------------------
    # Step 3: Compute impacts
    # -----------------------------
    for i, product in products_df.iterrows():
        total_carbon = 0
        total_water = 0
        total_energy = 0
        total_waste = 0

        for j in range(1, 4):
            material = product.get(f'material_{j}')
            weight_g = product.get(f'weight_{j}_g')

            if pd.isna(material) or pd.isna(weight_g):
                continue

            weight_kg = weight_g / 1000
            impact = material_impact_dict.get(material)

            if impact:
                total_carbon += weight_kg * impact['carbon']
                total_water += weight_kg * impact['water']
                total_energy += weight_kg * impact['energy']
                total_waste += weight_kg * impact['waste']

        products_df.at[i, 'total_carbon_kg'] = total_carbon
        products_df.at[i, 'total_water_L'] = total_water
        products_df.at[i, 'total_energy_MJ'] = total_energy
        products_df.at[i, 'total_waste_score'] = total_waste

    # -----------------------------
    # Step 4: Normalize
    # -----------------------------
    products_df['carbon_norm'] = products_df['total_carbon_kg'] / products_df['total_carbon_kg'].max()
    products_df['water_norm'] = products_df['total_water_L'] / products_df['total_water_L'].max()
    products_df['energy_norm'] = products_df['total_energy_MJ'] / products_df['total_energy_MJ'].max()
    products_df['waste_norm'] = products_df['total_waste_score'] / products_df['total_waste_score'].max()

    # -----------------------------
    # Step 5: Eco score (0–100, higher = better)
    # -----------------------------
    products_df['eco_score'] = (
        (1 - products_df['carbon_norm']) * 0.4 +
        (1 - products_df['water_norm']) * 0.3 +
        (1 - products_df['energy_norm']) * 0.2 +
        (1 - products_df['waste_norm']) * 0.1
    ) * 100

    # -----------------------------
    # Step 6: Final output table
    # -----------------------------
    summary_df = products_df[[
        'name', 'category',
        'total_carbon_kg', 'total_water_L',
        'total_energy_MJ', 'total_waste_score',
        'eco_score'
    ]].round(2)
