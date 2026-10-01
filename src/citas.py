"""Modulo de citas medicas."""

TIPOS_VALIDOS = {"contributivo": 0.10, "subsidiado": 0.0, "particular": 1.0}


def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:
    """Calcula el copago que paga el paciente."""
    if valor_consulta < 0:
        raise ValueError("El valor de la consulta no puede ser negativo")
    if tipo_afiliado not in TIPOS_VALIDOS:
        raise ValueError("Tipo de afiliado no valido")
    return round(valor_consulta * TIPOS_VALIDOS[tipo_afiliado], 2)
