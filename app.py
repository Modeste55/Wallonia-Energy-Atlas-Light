#Fichier 1 : cree app.py
# ==========================================================
# WALLONIA ENERGY ATLAS LIGHT
# APP.PY
# ==========================================================

from dash import Dash
from layout import create_layout
from callbacks import register_callbacks
from data_loader import atlas

# ==========================================================
# APP
# ==========================================================

app = Dash(
    __name__,
    suppress_callback_exceptions=True
)

server = app.server

# ==========================================================
# LAYOUT
# ==========================================================

app.layout = create_layout(atlas)

# ==========================================================
# CALLBACKS
# ==========================================================

register_callbacks(app, atlas)

# ==========================================================
# RUN LOCAL
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=8050
    )