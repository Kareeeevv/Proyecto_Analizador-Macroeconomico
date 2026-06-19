from typing import Callable, Any
from functools import wraps

def marco_legal_dinero() -> dict[str, str]:
    return {
        "Art. 28 Constitucional": "Otorga a Banxico el monopolio de emisión monetaria y prohíbe monopolios comerciales.",
        "Ley Monetaria": "Define las monedas y billetes de curso legal y sus denominaciones autorizadas.",
        "Ley del Banco de México": "Establece la autonomía del banco central para preservar el poder adquisitivo."
    }

def validar_denominacion(func: Callable) -> Callable:
    """Denominaciones actualmente válidas en México"""
    denominaciones = {0.05, 0.10, 0.20, 0.50, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0}
    
    @wraps(func)
    def wrapper(monto: float, *args: Any, **kwargs: Any) -> Any:
        if float(monto) not in denominaciones:
            raise ValueError(f"Error legal: La denominación de {monto} pesos no está autorizada por Banxico.")
        return func(monto, *args, **kwargs)
    return wrapper

@validar_denominacion
def procesar_pago(monto: float) -> str:
    return f"Pago de {monto} procesado bajo las normativas vigentes."