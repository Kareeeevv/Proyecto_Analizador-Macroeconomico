import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Any, Literal
import os
from dotenv import load_dotenv
from utility import *

load_dotenv()
TOKEN_BANXICO = os.getenv("TOKEN_BANXICO")

class Tratado:
    def __init__(self, nombre: str, paises: list[str], vigencia: int, aranceles_promedio: float):
        self.nombre = nombre
        self.paises = paises
        self.vigencia = vigencia
        self.aranceles_promedio = aranceles_promedio

class BalanzaComercial:
    def __init__(self):
        self.transacciones: list[dict[str, str]] = []

    def agregar_transaccion(self, fecha: str, pais: str, producto: str, monto: float | str, tipo: Literal['exportacion', 'importación']) -> None:
        self.transacciones.append({
            "fecha": fecha, "pais": pais, "producto": producto, "monto": str(monto), "tipo": tipo
        })

    def saldo_periodo(self, inicio: str, fin: str) -> float:
        formato = "%Y-%m-%d"
        fecha_inicio = datetime.strptime(inicio, formato)
        fecha_fin = datetime.strptime(fin, formato)
        saldo = 0.0
        
        for t in self.transacciones:
            fecha_t = datetime.strptime(t["fecha"], formato)
            if fecha_inicio <= fecha_t <= fecha_fin:
                if t["tipo"] == "exportacion":
                    saldo += float(t["monto"])

                elif t["tipo"] == "importacion":
                    saldo -= float(t["monto"])

        return saldo

    def socios_por_tratado(self, tratado: Tratado) -> list[str]:
        paises_con_transacciones = {t["pais"] for t in self.transacciones}
        return [pais for pais in tratado.paises if pais in paises_con_transacciones]

    def exportaciones_por_pais(self) -> pd.DataFrame:
        exportaciones = [t for t in self.transacciones if t["tipo"] == "exportacion"]

        df = pd.DataFrame(exportaciones)
        if not df.empty:
            return df.groupby("pais")["monto"].sum().reset_index()
        
        return pd.DataFrame(columns=["pais", "monto"])

    def simular(self, objetivo: list[str] | Tratado, modo: str, master_widget=None) -> None:
        if modo not in ['Exp', 'Imp']: return

        # Extrae los países a simular
        from constants import EXPORTS, IMPORTS
        paises_simular = objetivo.paises if isinstance(objetivo, Tratado) else objetivo
        all_paises = EXPORTS if modo == 'Exp' else IMPORTS
        
        datos: dict[str, Any] = {}

        for pais in paises_simular:
            if pais in all_paises:
                seriesID = all_paises[pais]
                value = get(seriesID, TOKEN_BANXICO)
                datos[pais] = value
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(list(datos.keys()), list(datos.values()), color=[random_color() for _ in datos])
        ax.set_title("Balanza Comercial Simulada (Exportaciones)")
        ax.set_ylabel("Monto (Míles de dólares)")
        
        if master_widget:
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master_widget)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=1, columnspan=2)

        else:
            plt.show()