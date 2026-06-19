class ModoProduccion:
    def __init__(self, nombre: str, propiedad_medios: list[str], relaciones_sociales: str, tecnologia_dominante: str, rol_dinero: str):
        self.nombre = nombre
        self.propiedad_medios = propiedad_medios
        self.relaciones_sociales = relaciones_sociales
        self.tecnologia_dominante = tecnologia_dominante
        self.rol_dinero = rol_dinero
        self._next: ModoProduccion | None = None

    @property
    def next(self) -> 'ModoProduccion | None':
        return self._next
    
    @next.setter
    def next(self, _val: 'ModoProduccion') -> None:
        self._next = _val

    def transicion(self, cambio_tecnologico: bool, conflicto_social: bool, tipo_cambio_comercial: bool) -> 'ModoProduccion | None':
        """Simula las condiciones de la dialéctica materialista"""
        if cambio_tecnologico and conflicto_social and tipo_cambio_comercial:
            return self._next
        
        return None

def simular_evolucion() -> list[str]:
    comunismo = ModoProduccion("Comunismo Primitivo", ["Comunal"], "Cooperación", "Herramientas de piedra", "Inexistente (Trueque)")
    esclavismo = ModoProduccion("Esclavismo", ["Privada (Esclavos/Tierra)"], "Amo-Esclavo", "Agricultura avanzada", "Aparición de moneda metálica")
    feudalismo = ModoProduccion("Feudalismo", ["Privada (Tierra)"], "Señor-Siervo", "Molinos, arados", "Acumulación en metales, uso local")
    capitalismo = ModoProduccion("Capitalismo", ["Privada (Capital/Fábricas)"], "Burguesía-Proletariado", "Máquina de vapor, Industria", "Medio de cambio universal, acumulación de capital")
    globalizacion = ModoProduccion("Globalización Actual", ["Corporativa", "Intelectual"], "Redes globales de trabajo", "Internet, IA", "Dinero fiduciario y digital, flujos financieros globales")

    comunismo.next = esclavismo
    esclavismo.next = feudalismo
    feudalismo.next = capitalismo
    capitalismo.next = globalizacion

    linea_tiempo = []
    modo_actual = comunismo
    
    while modo_actual:
        resumen = f"[{modo_actual.nombre}] -> Rol del Dinero: {modo_actual.rol_dinero}"
        linea_tiempo.append(resumen)
        # Simulamos que en cada etapa se cumplen las 3 condiciones históricas para avanzar
        modo_actual = modo_actual.transicion(True, True, True)
        
    return linea_tiempo