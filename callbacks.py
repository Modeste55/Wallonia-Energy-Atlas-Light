# ==========================================================
# WALLONIA ENERGY ATLAS LIGHT
# CALLBACKS.PY
# ==========================================================

from dash import Input
from dash import Output
from dash import html

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np

# ==========================================================
# REGISTER CALLBACKS
# ==========================================================

def register_callbacks(app, atlas):

    # ======================================================
    # ENTITY DROPDOWN
    # ======================================================

    @app.callback(

        Output(
            "entity-dropdown",
            "options"
        ),

        Output(
            "entity-dropdown",
            "value"
        ),

        Input(
            "scale-dropdown",
            "value"
        )

    )
    def update_entities(scale):

        if scale == "province":

            names = sorted(
                atlas["province"]["PROV_FR"]
                .unique()
            )

        elif scale == "arrondissement":

            names = sorted(
                atlas["arrondissement"]["ARROND_FR"]
                .unique()
            )

        else:

            names = sorted(
                atlas["municipality"]["COMMUNE"]
                .unique()
            )

        options = [

            {
                "label": n,
                "value": n
            }

            for n in names

        ]

        return options, names[0]

    # ======================================================
    # MAP
    # ======================================================

    @app.callback(

        Output(
            "map-graph",
            "figure"
        ),

        Input(
            "scale-dropdown",
            "value"
        ),

        Input(
            "energy-dropdown",
            "value"
        )

    )
    def update_map(scale, energy):

        # ----------------------------------------------
        # GDF
        # ----------------------------------------------

        if scale == "province":

            gdf = atlas["province"]

        elif scale == "arrondissement":

            gdf = atlas["arrondissement"]

        else:

            gdf = atlas["municipality"]

        # ----------------------------------------------
        # ENERGY COLUMN
        # ----------------------------------------------

        energy_col = {

            "HC": "CONSO_GWH",
            "HD": "BESOIN_GWH",
            "EC": "EC_GWH",
            "CED": "CED_GWH",
            "HEC": "HEC_GWH"

        }[energy]

        # ----------------------------------------------
        # MAP
        # ----------------------------------------------

        gdf = gdf.to_crs(4326)

        fig = px.choropleth_mapbox(

            gdf,

            geojson=gdf.geometry,

            locations=gdf.index,

            color=energy_col,

            hover_name=gdf.columns[1],

            mapbox_style="carto-positron",

            zoom=7,

            center={

                "lat": 50.5,
                "lon": 4.8

            },

            opacity=0.8

        )

        fig.update_layout(

            margin=dict(
                l=0,
                r=0,
                t=0,
                b=0
            ),

            height=700

        )

        return fig

    # ======================================================
    # PROFILE GRAPH
    # ======================================================

    @app.callback(

        Output(
            "profile-graph",
            "figure"
        ),

        Input(
            "scale-dropdown",
            "value"
        ),

        Input(
            "entity-dropdown",
            "value"
        )

    )
    def update_profile(scale, entity):

        fig = go.Figure()

        # ==================================================
        # PROVINCE
        # ==================================================

        if scale == "province":

            gdf = atlas["province"]

            row = gdf[
                gdf["PROV_FR"] == entity
            ].index[0]

            HC = atlas["PROVINCE"]["HC"][:, row]
            HD = atlas["PROVINCE"]["HD"][:, row]
            EC = atlas["PROVINCE"]["EC"][:, row]
            CED = atlas["PROVINCE"]["CED"][:, row]
            HEC = atlas["PROVINCE"]["HEC"][:, row]

        # ==================================================
        # ARRONDISSEMENT
        # ==================================================

        elif scale == "arrondissement":

            gdf = atlas["arrondissement"]

            row = gdf[
                gdf["ARROND_FR"] == entity
            ].index[0]

            HC = atlas["ARR"]["HC"][:, row]
            HD = atlas["ARR"]["HD"][:, row]
            EC = atlas["ARR"]["EC"][:, row]
            CED = atlas["ARR"]["CED"][:, row]
            HEC = atlas["ARR"]["HEC"][:, row]

        # ==================================================
        # MUNICIPALITY
        # ==================================================

        else:

            gdf = atlas["municipality"]

            row = gdf[
                gdf["COMMUNE"] == entity
            ].index[0]

            HC = atlas["COMMUNE"]["HC"][:, row]
            HD = atlas["COMMUNE"]["HD"][:, row]
            EC = atlas["COMMUNE"]["EC"][:, row]
            CED = atlas["COMMUNE"]["CED"][:, row]
            HEC = atlas["COMMUNE"]["HEC"][:, row]

        # ==================================================
        # CURVES
        # ==================================================

        fig.add_trace(
            go.Scatter(
                y=HC,
                name="HC",
                line=dict(width=2)
            )
        )

        fig.add_trace(
            go.Scatter(
                y=HD,
                name="HD",
                line=dict(width=2)
            )
        )

        fig.add_trace(
            go.Scatter(
                y=EC,
                name="EC",
                line=dict(width=2)
            )
        )

        fig.add_trace(
            go.Scatter(
                y=CED,
                name="CED",
                line=dict(width=2)
            )
        )

        fig.add_trace(
            go.Scatter(
                y=HEC,
                name="HEC",
                line=dict(width=2)
            )
        )

        fig.update_layout(

            title=f"Hourly Profiles - {entity}",

            template="plotly_white",

            hovermode="x unified",

            xaxis_title="Hour of Year",

            yaxis_title="Energy",

            height=550

        )

        return fig

    # ======================================================
    # STATISTICS
    # ======================================================

    @app.callback(

        Output(
            "stats-panel",
            "children"
        ),

        Input(
            "scale-dropdown",
            "value"
        ),

        Input(
            "entity-dropdown",
            "value"
        )

    )
    def update_stats(scale, entity):

        if scale == "province":

            row = atlas["province"][
                atlas["province"]["PROV_FR"]
                == entity
            ].iloc[0]

        elif scale == "arrondissement":

            row = atlas["arrondissement"][
                atlas["arrondissement"]["ARROND_FR"]
                == entity
            ].iloc[0]

        else:

            row = atlas["municipality"][
                atlas["municipality"]["COMMUNE"]
                == entity
            ].iloc[0]

        return html.Div(

            [

                html.H4(entity),

                html.Hr(),

                html.P(
                    f"Buildings : {int(row['NB_BATIMENTS']):,}"
                ),

                html.P(
                    f"Surface : {row['SURFACE_TOTALE']:,.0f} m²"
                ),

                html.P(
                    f"HC : {row['CONSO_GWH']:.2f} GWh"
                ),

                html.P(
                    f"HD : {row['BESOIN_GWH']:.2f} GWh"
                ),

                html.P(
                    f"EC : {row['EC_GWH']:.2f} GWh"
                ),

                html.P(
                    f"CED : {row['CED_GWH']:.2f} GWh"
                ),

                html.P(
                    f"HEC : {row['HEC_GWH']:.2f} GWh"
                )

            ]

        )