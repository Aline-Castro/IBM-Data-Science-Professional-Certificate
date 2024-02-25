import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Define o caminho local dos dados
caminho_dados = "D:\\CIÊNCIA DE DADOS\\CIENCIA DE DADOS - IBM - COURSERA\\10 - capstone\\5\\spacex_launch_geo.csv"

# Lê os dados do arquivo local
spacex_df = pd.read_csv(caminho_dados)

max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        dcc.Dropdown(
            id="site-dropdown",
            options=[
                {"label": "All Sites", "value": "All"},
                {"label": "CCAFS LC-40", "value": "CCAFS LC-40"},
                {"label": "CCAFS SLC-40", "value": "CCAFS SLC-40"},
                {"label": "KSC LC-39A", "value": "KSC LC-39A"},
                {"label": "VAFB SLC-4E", "value": "VAFB SLC-4E"},
            ],
            value="All",
            placeholder="Select a Launch Site here",
            searchable=True,
        ),
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            value=[min_payload, max_payload],
        ),
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)

@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == "All":
        fig = px.pie(
            filtered_df,
            values="class",
            names="Launch Site",
            title="Success Count for all launch sites",
        )
        return fig
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
        filtered_df = (
            filtered_df.groupby(["Launch Site", "class"])
            .size()
            .reset_index(name="class count")
        )
        fig = px.pie(
            filtered_df,
            values="class count",
            names="class",
            title=f"Total Success Launches for site {entered_site}",
        )
        return fig

@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def scatter(entered_site, payload):
    filtered_df = spacex_df[
        spacex_df["Payload Mass (kg)"].between(payload[0], payload[1])
    ]
    if entered_site == "All":
        fig = px.scatter(
            filtered_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title="Success count on Payload mass for all sites",
        )
        return fig
    else:
        fig = px.scatter(
            filtered_df[filtered_df["Launch Site"] == entered_site],
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title=f"Success count on Payload mass for site {entered_site}",
        )
        return fig

# Run the app
if __name__ == "__main__":
    app.run_server()
