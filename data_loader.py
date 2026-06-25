# ==========================================================
# DATA LOADER
# ==========================================================

import os
import numpy as np
import geopandas as gpd

# ==========================================================
# PATHS
# ==========================================================

ROOT = os.path.dirname(__file__)

DATA = os.path.join(ROOT, "data")
ATLAS = os.path.join(ROOT, "atlas")

# ==========================================================
# GPKG
# ==========================================================

print("Loading Municipalities...")

municipality = gpd.read_file(
    os.path.join(
        DATA,
        "building_MUNICIPALITE.gpkg"
    )
)

print("Loading Arrondissements...")

arrondissement = gpd.read_file(
    os.path.join(
        DATA,
        "building_ARRONDISSEMENT.gpkg"
    )
)

print("Loading Provinces...")

province = gpd.read_file(
    os.path.join(
        DATA,
        "building_PROVINCE.gpkg"
    )
)

# ==========================================================
# IDs
# ==========================================================

municipality["NIS_012011"] = (
    municipality["NIS_012011"]
    .astype(str)
)

# ==========================================================
# TEMPORAL DATA
# ==========================================================

ENERGIES = [
    "HC",
    "HD",
    "EC",
    "CED",
    "HEC"
]

COMMUNE = {}
ARR = {}
PROVINCE = {}

for e in ENERGIES:

    COMMUNE[e] = np.load(
        os.path.join(
            ATLAS,
            f"COMMUNE_{e}.npy"
        )
    )

    ARR[e] = np.load(
        os.path.join(
            ATLAS,
            f"ARR_{e}.npy"
        )
    )

    PROVINCE[e] = np.load(
        os.path.join(
            ATLAS,
            f"PROVINCE_{e}.npy"
        )
    )

# ==========================================================
# LOOKUPS
# ==========================================================

COMMUNES = np.load(
    os.path.join(
        ATLAS,
        "COMMUNES.npy"
    ),
    allow_pickle=True
)

ARRONDISSEMENTS = np.load(
    os.path.join(
        ATLAS,
        "ARRONDISSEMENTS.npy"
    ),
    allow_pickle=True
)

PROVINCES = np.load(
    os.path.join(
        ATLAS,
        "PROVINCES.npy"
    ),
    allow_pickle=True
)

# ==========================================================
# OBJECT
# ==========================================================

atlas = {

    "municipality": municipality,
    "arrondissement": arrondissement,
    "province": province,

    "COMMUNE": COMMUNE,
    "ARR": ARR,
    "PROVINCE": PROVINCE,

    "COMMUNES": COMMUNES,
    "ARRONDISSEMENTS": ARRONDISSEMENTS,
    "PROVINCES": PROVINCES

}

print("Atlas loaded successfully")