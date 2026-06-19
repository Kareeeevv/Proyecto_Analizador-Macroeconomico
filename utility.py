from random import randint
import requests
from requests.exceptions import RequestException, JSONDecodeError

def get(_series_id: str, _token: str | None) -> float:
    if not _token: return -1.0

    _url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{_series_id if isinstance(_series_id, str) else ",".join(_series_id)}/datos/oportuno"
    _headers = {"Bmx-Token": _token}

    try:
        response = requests.get(_url, headers=_headers)
        response.raise_for_status()
        data = response.json()
        
        str_value: str = data['bmx']['series'][0]['datos'][0]['dato']
        return float(str_value.replace(',', ''))
    
    except (RequestException, JSONDecodeError, KeyError, IndexError) as e:
        print(e)
        return -1.0

def random_color() -> str:
    r = hex(randint(0, 255))
    g = hex(randint(0, 255))
    b = hex(randint(0, 255))

    return f"#{'0' if len(r[2:]) == 1 else ''}{r[2:]}{'0' if len(g[2:]) == 1 else ''}{g[2:]}{'0' if len(b[2:]) == 1 else ''}{b[2:]}"