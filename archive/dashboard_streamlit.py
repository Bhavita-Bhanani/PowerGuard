import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(
    page_title="PowerGuard",
    page_icon="",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #0b1120;
}

.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #1f2937;
}

.metric-value {
    font-size: 2rem;
    font-weight: bold;
}

.metric-title {
    color: #9ca3af;
    font-size: 0.9rem;
}

.health-good {
    color: #22c55e;
}

.health-medium {
    color: #f59e0b;
}

.health-bad {
    color: #ef4444;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session Storage
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=["Time", "CPU", "RAM", "Battery"]
    )

# -----------------------------
# Metrics
# -----------------------------
battery = psutil.sensors_battery()

battery_percent = battery.percent if battery else 0
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent

# -----------------------------
# Health Score
# -----------------------------
health = round(
    battery_percent * 0.4 +
    (100 - cpu) * 0.3 +
    (100 - ram) * 0.3
)

if health >= 80:
    health_class = "health-good"
elif health >= 60:
    health_class = "health-medium"
else:
    health_class = "health-bad"

# -----------------------------
# Store History
# -----------------------------
new_row = pd.DataFrame({
    "Time": [datetime.now().strftime("%H:%M:%S")],
    "CPU": [cpu],
    "RAM": [ram],
    "Battery": [battery_percent]
})

st.session_state.history = pd.concat(
    [st.session_state.history, new_row],
    ignore_index=True
)

# Keep last 50 points
st.session_state.history = st.session_state.history.tail(50)

# -----------------------------
# Header
# -----------------------------
st.title("PowerGuard")
st.caption(
    "Laptop Health Assistant for Battery, Performance and Power Monitoring"
)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Battery", f"{battery_percent}%")

with col2:
    st.metric("CPU Usage", f"{cpu}%")

with col3:
    st.metric("Memory Usage", f"{ram}%")

with col4:
    st.markdown(
        f"""
        <div class="card">
            <div class="metric-title">System Health</div>
            <div class="metric-value {health_class}">
                {health}/100
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# Charts
# -----------------------------
left, right = st.columns(2)

with left:

    fig_cpu = px.line(
        st.session_state.history,
        x="Time",
        y="CPU",
        title="CPU Usage Trend"
    )

    st.plotly_chart(
        fig_cpu,
        use_container_width=True
    )

with right:

    fig_ram = px.line(
        st.session_state.history,
        x="Time",
        y="RAM",
        title="Memory Usage Trend"
    )

    st.plotly_chart(
        fig_ram,
        use_container_width=True
    )

# -----------------------------
# Battery Trend
# -----------------------------
fig_battery = px.line(
    st.session_state.history,
    x="Time",
    y="Battery",
    title="Battery Trend"
)

st.plotly_chart(
    fig_battery,
    use_container_width=True
)

# -----------------------------
# Insights
# -----------------------------
st.subheader("Insights")

insights = []

if battery_percent < 30:
    insights.append(
        "Battery level is below 30%. Consider connecting the charger."
    )

if ram > 80:
    insights.append(
        "Memory usage is high."
    )

if cpu > 80:
    insights.append(
        "CPU usage spike detected."
    )

if not insights:
    insights.append(
        "System operating normally."
    )

for item in insights:
    st.write(f"• {item}")

# -----------------------------
# Footer
# -----------------------------
st.caption(
    f"Last Updated: {datetime.now().strftime('%H:%M:%S')}"
)