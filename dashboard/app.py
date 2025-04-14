import dash
from dash import dcc , html , Input , Output
import plotly.express as px
import duckdb 
import pandas as pd

with duckdb.connect("/home/abhishek/Desktop/Data_Science/Air-quality-dashboard/notebooks/air_quality.db" , read_only= True) as db_connection:


        df = db_connection.execute("SELECT * FROM presentation.air_quality_data").fetchdf()

        daily_stats_df = db_connection.execute("SELECT * FROM presentation.daily_air_quality_stats").fetchdf()

        latest_values_df = db_connection.execute("SELECT * FROM presentation.latest_param_values_per_location").fetchdf()


def map_figure():

    map_fig = px.scatter_map(
        latest_values_df,
        lat="lat",
        lon="lon",
        hover_name="location",
        hover_data={
            "lat":False,
            "lon":False,
            "datetime": True,
            "pm10": True,
            "pm25": True,
            "so2": True,
            'o3': True,
            'no2': True,
            'no': True,
            'relativehumidity': True,
            'so2': True,
            'co': True
        },
        zoom=6.0
    )

    map_fig.update_layout(
        mapbox_style="open-street-map",
        height=800,
        title="Air Quality Monitoring System"
    )
    return map_fig


def line_figure():

        line_fig=px.line(
                daily_stats_df.sort_values(by="measurement_date"),
                x="measurement_date",
                y="average_value",
                title="Plot Over Time"
        )
        return line_fig

        
app = dash.Dash(__name__)


app.layout = html.Div([
                dcc.Graph(id="Sensor Locations" , figure=map_figure())
])

if __name__ == "__main__":
    app.run(debug=True)

