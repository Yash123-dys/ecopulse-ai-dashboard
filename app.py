import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="EcoPulse AI | Holographic Urban Climate Command",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: #050b14;
        color: #00ffcc;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #00ffcc !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 EcoPulse AI: Holographic Urban Climate & Resilience Command")
st.markdown("**Real-Time Spatial Intelligence & Autonomous Heat Mitigation Platform**")

selected_city = st.sidebar.selectbox(
    "Select Metropolitan Sector",
    ["Surat, Gujarat (Pilot Core)", "London, UK (Global Prime)", "Madrid, Spain", "Tokyo, Japan"]
)

c1, c2, c3, c4 = st.columns(4)
c1.metric(label="Net Zero Progress", value="78.4%", delta="+3.2%")
c2.metric(label="Air Quality Index (AQI)", value="98 (Excellent)", delta="+12 pts")
c3.metric(label="Carbon Capture Rate", value="1,420 t/h", delta="+85 t/h")
c4.metric(label="System Status", value="Autonomous 99.8%", delta="Secure")

st.markdown("---")

col_map, col_panel = st.columns([2, 1])

with col_map:
    st.subheader(f"Spatial Heat Vulnerability & Thermal Grid: {selected_city}")
    
    if "Surat" in selected_city:
        lat, lon = 21.1702, 72.8311
    elif "London" in selected_city:
        lat, lon = 51.5074, -0.1278
    else:
        lat, lon = 40.4168, -3.7038

    # Generate map data points
    np.random.seed(42)
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / 50 + [lat, lon],
        columns=['lat', 'lon']
    )
    
    # Display reliable Streamlit map
    st.map(map_data, zoom=11)

with col_panel:
    st.subheader("🛡️ Mitigation Strategies")
    st.info("AI-driven automated cooling actions:")
    st.markdown("""
    * **Cool Roofs:** `54% Covered`
    * **Urban Greening:** `62% Optimized`
    * **Water Mist Grids:** `Active (18 zones)`
    * **Emission Reductions:** `-24.5% YoY`
    """)
    st.markdown("---")
    st.subheader("📊 Green Space Impact")
    st.progress(0.82)
    st.caption("82% thermal reduction achieved.")

st.markdown("---")
st.markdown("🔒 **EcoPulse AI Neural Core** | Connected to Satellite Telemetry.")
