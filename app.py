import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

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
        text-shadow: 0px 0px 10px rgba(0, 255, 204, 0.4);
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

    np.random.seed(101)
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [lat, lon],
        columns=['lat', 'lon']
    )
    map_data['heat_stress'] = np.random.randint(50, 100, size=100)

    # Reliable Scatterplot Layer along with Map to avoid blank screen
    layer = pdk.Layer(
        "ScatterplotLayer",
        map_data,
        get_position=["lon", "lat"],
        get_color='[255, 50, 50, 180]',
        get_radius=200,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=12,
        pitch=40,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Thermal Stress Index: {heat_stress}"},
        map_style="mapbox://styles/mapbox/dark-v10"
    )
    
    # Render with explicit container width
    st.pydeck_chart(r, use_container_width=True)

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
