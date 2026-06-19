from typing import Literal
import requests as req

class Dinero:
    def __init__(self, valor_nominal: float, tipo: Literal["moneda", "billete", "digital"], emisor: Literal["Banxico", "gobierno"]):
        self.valor_nominal = float(valor_nominal)
        self.tipo = tipo
        self.emisor = emisor

    def medio_de_cambio(self, precio_producto: float) -> bool:
        return self.valor_nominal >= float(precio_producto)

    def unidad_de_cuenta(self, lista_precios: list[float]) -> list[float]:
        """Expresa los precios en relación a esta unidad monetaria"""
        
        return [float(precio) / self.valor_nominal for precio in lista_precios]

    def deposito_de_valor(self, tasas_inf: list[float], periodo: list[int | str]) -> float:
        """Calcula el valor adquisitivo restante tras la inflación"""
        years = int(periodo[1]) - int(periodo[0])
        if years < 0:
            raise ValueError("El periodo debe ser cronológico [año_inicio, año_fin]")
        
        valor_real = self.valor_nominal
        for _t in tasas_inf:
            valor_real *= (1 - _t)

        return valor_real
    
    @staticmethod
    def historial_inflacion(begin_year: str | int, end_year: str | int) -> list[float]:
        from comercio import TOKEN_BANXICO
        if not TOKEN_BANXICO: return []

        response = req.get("https://www.banxico.org.mx/SieAPIRest/service/v1/series/SR1503/datos",
                           headers={'Bmx-Token': TOKEN_BANXICO})
        full_datos: list[dict[str, str]] = response.json()['bmx']['series'][0]['datos']
        datos = full_datos[(int(begin_year) - 1990)*12 : ((int(end_year) - 1990)*12) + 1]

        inflaciones = [((float(datos[i]['dato'].replace(',','')) - float(datos[i-1]['dato'].replace(',',''))) / float(datos[i-1]['dato'].replace(',',''))) for i in range(1, datos.__len__())]
        return inflaciones
    
    @staticmethod
    def inflacion_promedio(begin_year: str | int, end_year: str | int) -> float:
        from comercio import TOKEN_BANXICO
        if not TOKEN_BANXICO: return -1.0

        response = req.get("https://www.banxico.org.mx/SieAPIRest/service/v1/series/SR1503/datos",
                           headers={'Bmx-Token': TOKEN_BANXICO})
        full_datos: list[dict[str, str]] = response.json()['bmx']['series'][0]['datos']
        datos = full_datos[(int(begin_year) - 1990)*12 : ((int(end_year) - 1990)*12) + 1]

        inflaciones = [((float(datos[i]['dato'].replace(',','')) - float(datos[i-1]['dato'].replace(',',''))) / float(datos[i-1]['dato'].replace(',',''))) for i in range(1, datos.__len__())]
        suma: float = 0.0
        for inf in inflaciones:
            suma += inf * 100

        return (suma / inflaciones.__len__()) if len(inflaciones) else suma

    @staticmethod
    def inflacion_acumulada(begin_year: str | int, end_year: str | int) -> float:
        from comercio import TOKEN_BANXICO
        if not TOKEN_BANXICO: return -1.0

        response = req.get("https://www.banxico.org.mx/SieAPIRest/service/v1/series/SR1503/datos",
                           headers={'Bmx-Token': TOKEN_BANXICO})
        full_datos: list[dict[str, str]] = response.json()['bmx']['series'][0]['datos']
        datos = full_datos[(int(begin_year) - 1990)*12 : ((int(end_year) - 1990)*12) + 1]

        inflaciones = [((float(datos[i]['dato'].replace(',','')) - float(datos[i-1]['dato'].replace(',',''))) / float(datos[i-1]['dato'].replace(',',''))) for i in range(1, datos.__len__())]
        acumulada: float = 1.0

        for inf in inflaciones:
            acumulada *= (1 + inf)
        return (acumulada - 1) * 100