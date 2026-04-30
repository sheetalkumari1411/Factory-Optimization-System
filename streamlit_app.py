import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.map_visualization import create_map

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Factory Optimization System", layout="wide")

# -----------------------------
# TITLE
# -----------------------------
st.title("🚀 Factory Reallocation & Optimization System")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("⚙️ Controls")

product = st.sidebar.text_input("Product Name", "Nerds")
region = st.sidebar.text_input("Region", "West")
ship_mode = st.sidebar.selectbox(
    "Ship Mode",
    ["Standard Class", "Second Class", "First Class"]
)

priority = st.sidebar.slider("Speed vs Profit Priority", 0, 100, 50)

# -----------------------------
# BUTTON
# -----------------------------
if st.button("🔍 Run Optimization"):

    st.success("Simulation executed!")

    # -----------------------------
    # SIMULATION DATA (SAFE + CLEAN)
    # -----------------------------
    sim_results = [
        {"factory": "Sugar Shack", "predicted_lead_time": 5},
        {"factory": "Secret Factory", "predicted_lead_time": 7},
        {"factory": "Lot's O' Nuts", "predicted_lead_time": 6}
    ]

    # Convert to DataFrame
    data = pd.DataFrame(sim_results)
    data.columns = ["Factory", "Lead Time"]

    # -----------------------------
    # DYNAMIC BEST FACTORY
    # -----------------------------
    best_row = data.loc[data["Lead Time"].idxmin()]
    best_factory = best_row["Factory"]
    best_time = best_row["Lead Time"]

    # Improvement %
    worst_time = data["Lead Time"].max()
    improvement = round((worst_time - best_time) / worst_time * 100, 2)

    # -----------------------------
    # RESULTS (METRICS)
    # -----------------------------
    st.subheader("📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Best Factory", best_factory)
    col2.metric("Lead Time", f"{best_time} Days")
    col3.metric("Improvement", f"{improvement}%")

    # -----------------------------
    # TABLE (COLORED)
    # -----------------------------
    st.subheader("📋 Factory Comparison")

    st.dataframe(
        data.style.highlight_min(subset=["Lead Time"], color="lightgreen"),
        use_container_width=True
    )

    # -----------------------------
    # CHART (PLOTLY)
    # -----------------------------
    st.subheader("📊 Lead Time Comparison Chart")

    fig = px.bar(
        data,
        x="Factory",
        y="Lead Time",
        color="Factory",
        title="Factory Lead Time Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # TABS (MAP + DOWNLOAD)
    # -----------------------------
    tab1, tab2 = st.tabs(["🌍 Map", "📥 Download"])

    with tab1:
        st.subheader("Factory to Customer Route")
        st.pydeck_chart(create_map(best_factory))

    with tab2:
        csv = data.to_csv(index=False)
        st.download_button(
            "Download Report",
            csv,
            "factory_report.csv",
            "text/csv"
        )
