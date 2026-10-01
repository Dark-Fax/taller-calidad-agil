import pytest

from src.citas import calcular_copago


def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


def test_contributivo_paga_10_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000
    assert calcular_copago(33.33, "contributivo") == 3.33


def test_subsidiado_no_paga():
    assert calcular_copago(100000, "subsidiado") == 0


def test_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_copago(-1, "particular")
    with pytest.raises(ValueError):
        calcular_copago(1000, "vip")
