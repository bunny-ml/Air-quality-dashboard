import streamlit as st
import plotly.express as px
import duckdb
import pandas as pd
import os

# Set DB path
db_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'air_quality.db')

# Page setup
st.set_page_config(layout="wide")
st.title("Air Quality Dashboard")

# Load sensor data for map
@st.cache_data
def load_latest_values():
    with duckdb.connect(db_path, read_only=True) as db_connection:
        return db_connection.execute(
            "SELECT * FROM presentation.latest_param_values_per_location"
        ).fetchdf()

latest_values_df = load_latest_values()

# Tab navigation
tab1, tab2 = st.tabs(["Sensor Locations", "Parameter Plots"])

with tab1:
    st.subheader("Air Quality Monitoring Locations")

    map_fig = px.scatter_map(
        latest_values_df,
        lat="lat",
        lon="lon",
        hover_name="location",
        hover_data={
            "lat": False,
            "lon": False,
            "datetime": True,
            "pm10": True,
            "pm25": True,
            'o3': True,
            'no2': True,
            'co': True,
            "so2": True
        },
        zoom=6.0
    )
    map_fig.update_layout(
        mapbox_style="open-street-map",
        height=800
    )
    st.plotly_chart(map_fig, use_container_width=True)


with tab2:
    st.subheader("Explore Parameters Over Time")

    @st.cache_data
    def load_daily_stats():
        with duckdb.connect(db_path, read_only=True) as db_connection:
            return db_connection.execute(
                "SELECT * FROM presentation.daily_air_quality_stats"
                ).fetchdf()

    df = load_daily_stats()

    # Dropdowns
    location = st.selectbox("Select Location", df["location"].unique())
    parameter = st.selectbox("Select Parameter", df["parameter"].unique())

    # Date range
    start_date = pd.to_datetime(df["measurement_date"].min())
    end_date = pd.to_datetime(df["measurement_date"].max())

    selected_date = st.date_input("Select Date Range", [start_date, end_date])

    if len(selected_date) == 2:
        s_date, e_date = pd.to_datetime(selected_date[0]), pd.to_datetime(selected_date[1])

        # Filter data
        filtered_df = df[
            (df["location"] == location) &
            (df["parameter"] == parameter) &
            (df["measurement_date"] >= s_date) &
            (df["measurement_date"] <= e_date)
        ]

        labels = {
            "average_value": filtered_df["units"].unique()[0],
            "measurement_date": "Date"
        }

        # Line chart
        line_fig = px.line(
            filtered_df.sort_values(by="measurement_date"),
            x="measurement_date",
            y="average_value",
            labels=labels,
            title=f"{parameter} Levels Over Time"
        )
        st.plotly_chart(line_fig, use_container_width=True)

        # Box plot
        box_fig = px.box(
            filtered_df.sort_values(by="weekday_number"),
            x="weekday",
            y="average_value",
            labels=labels,
            title=f"{parameter} Levels by Weekday"
        )
        st.plotly_chart(box_fig, use_container_width=True)
