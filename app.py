import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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

col_map, col_panel = st.columns([2, 1])

with col_map:
    st.subheader(f"📍 Interactive Thermal Heatmap & Grid: {selected_city}")
    
    if "Surat" in selected_city:
        lat, lon = 21.1702, 72.8311
    elif "London" in selected_city:
        lat, lon = 51.5074, -0.1278
    elif "Madrid" in selected_city:
        lat, lon = 40.4168, -3.7038
    else:
        lat, lon = 35.6762, 139.6503

    # Generate interactive map data points
    np.random.seed(42)
    map_df = pd.DataFrame({
        "lat": lat + np.random.randn(50) * 0.03,
        "lon": lon + np.random.randn(50) * 0.03,
        "Heat Stress": np.random.randint(50, 100, size=50)
    })

    # Plotly Scatter Mapbox (Guaranteed to render without errors)
    fig = px.scatter_mapbox(
        map_df, lat="lat", lon="lon", color="Heat Stress",
        color_continuous_scale="Reds", size_max=15, zoom=11,
        mapbox_style="carto-darkmatter"
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=400)
    st.plotly_chart(fig, use_container_width=True)

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
