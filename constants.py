from random import randint
from comercio import Tratado

__all__ = ['EXPORTS', 'IMPORTS', 'TRATADOS']

EXPORTS: dict[str, str] = {
    "EE.UU.": "SE27277",
    "Canadá": "SE27276",
    "Colombia": "SE27286",
    "Chile": "SE27285",
    "Perú": "SE27292",
    "EU": "SE44940",
    "Costa Rica": "SE27327",
    "El Salvador": "SE27328",
    "Guatemala": "SE27329",
    "Nicaragua": "SE27331",
    "Honduras": "SE27330"
}

IMPORTS: dict[str, str] = {
    "EE.UU.": "SE27544",
    "Canadá": "SE27543",
    "Colombia": "SE27553",
    "Chile": "SE27552",
    "Perú": "SE27559",
    "EU": "SE44939",
    "Costa Rica": "SE27594",
    "El Salvador": "SE27595",
    "Guatemala": "SE27596",
    "Nicaragua": "SE27598",
    "Honduras": "SE27597"
}

TRATADOS: dict[str, Tratado] = {
    "T-MEC": Tratado("T-MEC", ['EE.UU.', 'Canadá'], 16, 3.7),
    "TLCUEM": Tratado("TLCUEM", ['EU'], -1, 0.0),
    "ALLY_PACIFIC": Tratado("Alianza del Pacífico", ['Colombia', 'Chile', 'Perú'], -1, 0.0),
    "TLC_AMECENTRAL": Tratado("TLC Centroamérica", ['Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua'], -1, 18.0)
}