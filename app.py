import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="EcoPulse AI | Urban Climate Command",
    page_icon="🌍",
    layout="wide"
)

# Sci-Fi Dark Theme Styling
st.markdown("""
    <style>
    .main {
        background-color: #050b14;
        color: #00ffcc;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #00ffcc !important;
        text-shadow: 0px 0px 8px rgba(0, 255, 204, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 EcoPulse AI: Holographic Urban Climate Command Center")
st.markdown("**Real-Time Spatial Intelligence & Autonomous Heat Mitigation Platform**")

selected_city = st.sidebar.selectbox(
    "Select Metropolitan Sector",
    ["Surat, Gujarat (Pilot Core)", "London, UK (Global Prime)", "Madrid, Spain", "Tokyo, Japan"]
)

# Metrics Grid
c1, c2, c3, c4 = st.columns(4)
c1.metric(label="Net Zero Progress", value="78.4%", delta="+3.2%")
c2.metric(label="Air Quality Index (AQI)", value="98 (Excellent)", delta="+12 pts")
c3.metric(label="Carbon Capture Rate", value="1,420 t/h", delta="+85 t/h")
c4.metric(label="System Status", value="Autonomous 99.8%", delta="Secure")

st.markdown("---")

col_grid, col_panel = st.columns([2, 1])

with col_grid:
    st.subheader(f"⚡ Live Thermal Stress & Sector Analysis: {selected_city}")
    st.info("Neural network telemetry active across urban heat islands and micro-climates.")

    # Structured Thermal Data Grid
    np.random.seed(42)
    zones = [f"Sector Alpha-{i}" for i in range(1, 7)]
    df_zones = pd.DataFrame({
        "Urban Sector": zones,
        "Surface Temp (°C)": np.random.uniform(38.5, 46.2, size=6).round(1),
        "Heat Stress Index": np.random.randint(60, 98, size=6),
        "Mitigation Status": np.random.choice(["Cool Roofs Active", "Urban Greening Deployed", "High Risk - Action Needed"], size=6)
    })
    
    st.dataframe(df_zones, use_container_width=True)

    st.subheader("📈 24-Hour Thermal & Carbon Analytics")
    chart_data = pd.DataFrame(
        np.random.randn(24, 2) * [1.5, 40] + [42, 1200],
        columns=['Thermal Index (°C equivalent)', 'Carbon Absorption Rate (t/h)']
    )
    st.line_chart(chart_data)

with col_panel:
    st.subheader("🛡️ AI Mitigation Strategies")
    st.info("Automated cooling actions deployed:")
    st.markdown("""
    * **Cool Roofs:** `54% Covered`
    * **Urban Greening:** `62% Optimized`
    * **Water Mist Grids:** `Active (18 zones)`
    * **Emission Reductions:** `-24.5% YoY`
    """)
    st.markdown("---")
    st.subheader("📊 Microclimate Impact")
    st.progress(0.82)
    st.caption("82% thermal reduction achieved via localized green infrastructure.")

st.markdown("---")
st.markdown("🔒 **EcoPulse AI Neural Core** | Connected to Satellite Telemetry & Local Sensor Mesh.")
