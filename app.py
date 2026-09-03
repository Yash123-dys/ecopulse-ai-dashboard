import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
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
    .stAlert {
        background-color: #0b192c;
        color: #00ffcc;
        border: 1px solid #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🌍 EcoPulse AI: Holographic Urban Climate Command Center")
st.markdown("**Real-Time Spatial Intelligence & Autonomous Heat Mitigation Platform**")

# Sidebar for City & Hotspot Navigation
selected_city = st.sidebar.selectbox(
    "Select Metropolitan Sector",
    ["Surat, Gujarat (Pilot Core)", "London, UK (Global Prime)", "Madrid, Spain", "Tokyo, Japan"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Hotspot Focus & AI Diagnostics")

# Hotspot selection simulating zoom & focus click
hotspot_choice = st.sidebar.selectbox(
    "Select Red Alert Hotspot",
    [
        "Overview (All Zones)",
        "Hotspot #1: Central Data Center (High Thermal Load)",
        "Hotspot #2: Asphalt/Damar Road Corridor (Heat Trap)",
        "Hotspot #3: Industrial Heavy Zone (Carbon & Heat Spike)"
    ]
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
    if "Overview" in hotspot_choice:
        st.subheader(f"🗺️ Live Spatial Heat Map & Coordinates: {selected_city}")
        
        if "Surat" in selected_city:
            lat, lon = 21.1702, 72.8311
        elif "London" in selected_city:
            lat, lon = 51.5074, -0.1278
        elif "Madrid" in selected_city:
            lat, lon = 40.4168, -3.7038
        else:
            lat, lon = 35.6762, 139.6503

        np.random.seed(42)
        map_data = pd.DataFrame(
            np.random.randn(40, 2) / 50 + [lat, lon],
            columns=['lat', 'lon']
        )
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

    else:
        # Detailed Zoom/Focus View for Selected Hotspot
        st.subheader(f"🔍 Focused Zone Inspector: {hotspot_choice}")
        st.warning("⚠️ High-Resolution Thermal Focus Active: Surrounding regions filtered out for precision telemetry.")
        
        # Specific focused data based on selection
        if "Data Center" in hotspot_choice:
            st.markdown("### 🏢 Facility Type: Hyperscale Data Center")
            st.metric(label="Local Surface Temperature", value="48.2 °C", delta="+6.4 °C above normal")
            st.info("AI Diagnosis: High exhaust heat accumulation from server cooling units affecting local microclimate.")
            
        elif "Asphalt" in hotspot_choice:
            st.markdown("### 🛣️ Facility Type: Asphalt / Damar Road Corridor")
            st.metric(label="Pavement Surface Temp", value="52.6 °C", delta="+10.1 °C heat island effect")
            st.info("AI Diagnosis: High solar radiation absorption by dark asphalt surfaces driving up neighborhood ambient temperatures.")
            
        else:
            st.markdown("### 🏭 Facility Type: Industrial Manufacturing Cluster")
            st.metric(label="Thermal & Emission Index", value="94 / 100 (Critical)", delta="High Risk")
            st.info("AI Diagnosis: Continuous industrial processing coupled with lack of canopy cover creating a severe thermal trap.")

        st.markdown("---")
        st.subheader("📊 Local Micro-Grid Analytics")
        focus_chart_data = pd.DataFrame(
            np.random.randn(12, 2) * [1.2, 20] + [45, 1100],
            columns=['Zone Temp (°C)', 'Cooling Load (kW)']
        )
        st.line_chart(focus_chart_data)

with col_panel:
    st.subheader("🛡️ AI Autonomous Mitigation Advisor")
    
    if "Overview" in hotspot_choice:
        st.info("👈 Select a specific Red Alert Hotspot from the sidebar to view targeted AI solutions.")
        st.markdown("""
        * **Cool Roofs:** `54% Covered`
        * **Urban Greening:** `62% Optimized`
        * **Water Mist Grids:** `Active (18 zones)`
        """)
    else:
        st.success("🤖 AI Prescription Generated for Selected Hotspot:")
        
        if "Data Center" in hotspot_choice:
            st.markdown("""
            1. **Cooling System Optimization:** Lower internal chiller setpoints and deploy AI-driven variable speed fans.
            2. **Vertical Green Walls:** Install dense green vegetation panels along perimeter walls to drop ambient temperature by 3-4°C.
            3. **Cool Roof Coating:** Apply high-albedo white reflective membrane on the roof structure.
            """)
        elif "Asphalt" in hotspot_choice:
            st.markdown("""
            1. **Solar-Reflective Pavement Coating:** Spray light-colored titanium dioxide reflective sealant over the damar road.
            2. **Linear Tree Canopy:** Plant fast-growing shade trees along the corridor.
            3. **Mist Hydration Grids:** Deploy automated water mist nozzles to periodically cool the pavement during peak afternoon hours.
            """)
        else:
            st.markdown("""
            1. **Industrial Exhaust Scrubbers:** Upgrade heat exchangers to capture and recycle waste thermal energy.
            2. **Buffer Green Zones:** Establish a 50-meter perimeter buffer zone with dense multi-tier urban forestry.
            3. **Smart Ventilation Corridors:** Modify structural layouts to enhance natural wind flow through the industrial block.
            """)

st.markdown("---")
st.markdown("🔒 **EcoPulse AI Neural Core** | Connected to Satellite Telemetry & Local Sensor Mesh.")

