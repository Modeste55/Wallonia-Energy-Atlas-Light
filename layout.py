# ==========================================================
# WALLONIA ENERGY ATLAS LIGHT
# LAYOUT.PY
# ==========================================================

from dash import html
from dash import dcc

import plotly.graph_objects as go

# ==========================================================
# EMPTY MAP
# ==========================================================

def empty_map():

    fig = go.Figure()

    fig.update_layout(

        template="plotly_white",

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        height=700
    )

    return fig

# ==========================================================
# EMPTY PROFILE
# ==========================================================

def empty_profile():

    fig = go.Figure()

    fig.update_layout(

        template="plotly_white",

        title="Hourly Energy Profiles",

        xaxis_title="Hour of Year",

        yaxis_title="Energy",

        height=500
    )

    return fig

# ==========================================================
# LAYOUT
# ==========================================================

def create_layout(atlas):

    return html.Div(

        [

            # ==================================================
            # HEADER
            # ==================================================

            html.Div(

                [

                    html.H1(

                        "Wallonia Energy Atlas Light",

                        style={
                            "textAlign":"center",
                            "fontWeight":"bold",
                            "fontSize":"42px",
                            "marginBottom":"5px"
                        }

                    ),

                    html.H4(

                        "Dynamic Building Energy Profiles across Wallonia",

                        style={
                            "textAlign":"center",
                            "color":"gray",
                            "marginTop":"0px"
                        }

                    )

                ]

            ),

            # ==================================================
            # CONTROLS
            # ==================================================

            html.Div(

                [

                    # --------------------------------------
                    # SCALE
                    # --------------------------------------

                    html.Div(

                        [

                            html.Label(
                                "Territorial Scale"
                            ),

                            dcc.Dropdown(

                                id="scale-dropdown",

                                options=[

                                    {
                                        "label":"Province",
                                        "value":"province"
                                    },

                                    {
                                        "label":"Arrondissement",
                                        "value":"arrondissement"
                                    },

                                    {
                                        "label":"Municipality",
                                        "value":"municipality"
                                    }

                                ],

                                value="province",

                                clearable=False

                            )

                        ],

                        style={
                            "width":"30%",
                            "display":"inline-block",
                            "padding":"10px"
                        }

                    ),

                    # --------------------------------------
                    # ENERGY
                    # --------------------------------------

                    html.Div(

                        [

                            html.Label(
                                "Energy Indicator"
                            ),

                            dcc.Dropdown(

                                id="energy-dropdown",

                                options=[

                                    {
                                        "label":"Heat Consumption (HC)",
                                        "value":"HC"
                                    },

                                    {
                                        "label":"Heat Demand (HD)",
                                        "value":"HD"
                                    },

                                    {
                                        "label":"Electricity Consumption (EC)",
                                        "value":"EC"
                                    },

                                    {
                                        "label":"Cooling Electricity Demand (CED)",
                                        "value":"CED"
                                    },

                                    {
                                        "label":"Heating Electricity Consumption (HEC)",
                                        "value":"HEC"
                                    }

                                ],

                                value="HC",

                                clearable=False

                            )

                        ],

                        style={
                            "width":"30%",
                            "display":"inline-block",
                            "padding":"10px"
                        }

                    ),

                    # --------------------------------------
                    # ENTITY
                    # --------------------------------------

                    html.Div(

                        [

                            html.Label(
                                "Territory"
                            ),

                            dcc.Dropdown(

                                id="entity-dropdown",

                                clearable=False

                            )

                        ],

                        style={
                            "width":"35%",
                            "display":"inline-block",
                            "padding":"10px"
                        }

                    )

                ]

            ),

            # ==================================================
            # MAIN CONTENT
            # ==================================================

            html.Div(

                [

                    # --------------------------------------
                    # MAP
                    # --------------------------------------

                    html.Div(

                        [

                            dcc.Graph(

                                id="map-graph",

                                figure=empty_map()

                            )

                        ],

                        style={

                            "width":"50%",
                            "display":"inline-block",
                            "verticalAlign":"top"

                        }

                    ),

                    # --------------------------------------
                    # STATS
                    # --------------------------------------

                    html.Div(

                        [

                            html.H3(
                                "Statistics"
                            ),

                            html.Div(
                                id="stats-panel"
                            )

                        ],

                        style={

                            "width":"48%",
                            "display":"inline-block",
                            "verticalAlign":"top",

                            "padding":"20px",

                            "backgroundColor":"#f8f9fa",

                            "borderRadius":"15px"

                        }

                    )

                ]

            ),

            # ==================================================
            # TIME PROFILE
            # ==================================================

            html.Div(

                [

                    dcc.Graph(

                        id="profile-graph",

                        figure=empty_profile()

                    )

                ],

                style={

                    "padding":"10px"

                }

            )

        ],

        style={

            "fontFamily":"Arial",

            "padding":"20px",

            "backgroundColor":"white"

        }

    )