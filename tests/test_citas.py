import pytest

from src.citas import calcular_copago


def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000
