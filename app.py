import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for High-Tech Dashboard
st.set_page_config(
    page_title="EcoPulse AI | Urban Climate Command Center",
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

# Header Section
st.title("🌍 EcoPulse AI: Holographic Urban Climate Command Center")
st.markdown("**Real-Time Spatial Intelligence & Autonomous Heat Mitigation Platform**")

# Sidebar for City Navigation
selected_city = st.sidebar.selectbox(
    "Select Metropolitan Sector",
    ["Surat, Gujarat (Pilot Core)", "London, UK (Global Prime)", "Madrid, Spain", "Tokyo, Japan"]
)

# Top Holographic Metrics Grid
c1, c2, c3, c4 = st.columns(4)
c1.metric(label="Net Zero Progress", value="78.4%", delta="+3.2%")
c2.metric(label="Air Quality Index (AQI)", value="98 (Excellent)", delta="+12 pts")
c3.metric(label="Carbon Capture Rate", value="1,420 t/h", delta="+85 t/h")
c4.metric(label="System Status", value="Autonomous 99.8%", delta="Secure")

st.markdown("---")

# Main Split Layout
col_grid, col_panel = st.columns([2, 1])

with col_grid:
    st.subheader(f"🗺️ Live Spatial Heat Map & Coordinates: {selected_city}")
    
    # Coordinates mapping based on selected city
    if "Surat" in selected_city:
        lat, lon = 21.1702, 72.8311
    elif "London" in selected_city:
        lat, lon = 51.5074, -0.1278
    elif "Madrid" in selected_city:
        lat, lon = 40.4168, -3.7038
    else:
        lat, lon = 35.6762, 139.6503

    # Map Data Generation
    np.random.seed(42)
    map_data = pd.DataFrame(
        np.random.randn(40, 2) / 50 + [lat, lon],
        columns=['lat', 'lon']
    )
    
    # Display Built-in Streamlit Map safely
    st.map(map_data, zoom=11, use_container_width=True)

    st.subheader(f"⚡ Sector Analysis Table: {selected_city}")
    zones = [f"Sector Alpha-{i}" for i in range(1, 5)]
    df_zones = pd.DataFrame({
        "Urban Sector": zones,
        "Surface Temp (°C)": np.random.uniform(38.5, 46.2, size=4).round(1),
        "Heat Stress Index": np.random.randint(60, 98, size=4),
        "Mitigation Status": ["Cool Roofs Active", "Urban Greening", "High Risk", "Optimized"]
    })
    st.dataframe(df_zones, use_container_width=True)

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
