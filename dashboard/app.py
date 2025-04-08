import dash
from dash import dcc , html , Input , Output
import plotly.express as px
import duckdb 
import pandas as pd

with duckdb.connect("/home/abhishek/Desktop/Data_Science/Air-quality-dashboard/notebooks/air_quality.db" , read_only= True) as db_connection:


        df = db_connection.execute("SELECT * FROM air_quality.presentation.air_quality_data").fetchdf()

        daily_stats_df = db_connection.execute("SELECT * FROM presentation.daily_air_quality_stats").fetchdf()

        latest_values_df = db_connection.execute("SELECT * FROM presentation.latest_param_values_per_location").fetchdf()

app = dash.Dash(__name__)


app.layout = html.Div()

if __name__ == "__main__":
    app.run_server(debug=True)

