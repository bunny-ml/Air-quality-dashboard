# 🌍 Air Quality Dashboard

This is a **Streamlit web app** that visualizes air quality data collected from over **150+ monitoring sensors across India**. It provides users with interactive map and chart views for analyzing pollution levels like **PM2.5, PM10, O₃, NO₂, CO, SO₂**, and more.

> ⚠️ _Please note: Some sensors may intermittently stop reporting data due to connectivity or maintenance issues._

---

## 🚀 Features

### 🗺️ Sensor Locations Map
- View sensor distribution across India using an **interactive map**.
- Hover on markers to see **latest parameter values** per location.

### 📊 Time Series & Distribution Plots
- Select a **location** and **parameter** to:
  - View historical **line plot trends** over time.
  - Analyze **box plots by weekdays** for pollution pattern insights.
- Filter data using an **interactive date range picker**.

### 📡 Real-Time Data Source
- Data is collected via [OpenAQ](https://openaq.org/), a global open-source air quality data platform.
- The backend database is a local **DuckDB** file storing preprocessed air quality readings.

---

## 🧰 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Visualizations:** [Plotly](https://plotly.com/python/)
- **Database:** [DuckDB](https://duckdb.org/)
- **Language:** Python 3

---

## 🛠️ Setup Instructions (Local Development)

1. **Clone the repo**:
   ```bash
   git clone https://github.com/bunny-ml/Air-quality-dashboard.git
   cd Air-quality-dashboard
