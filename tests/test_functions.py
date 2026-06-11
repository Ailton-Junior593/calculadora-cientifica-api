import pytest

from app.function import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
    potencia,
    raiz_quadrada,
    log_natural
)


def test_soma():
    assert soma(10, 5) == 15


def test_subtracao():
    assert subtracao(10, 5) == 5


def test_multiplicacao():
    assert multiplicacao(10, 5) == 50


def test_divisao():
    assert divisao(20, 4) == 5


def test_potencia():
    assert potencia(2, 3) == 8


def test_raiz_quadrada():
    assert raiz_quadrada(25) == 5


def test_log_natural():
    assert log_natural(1) == 0


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)


def test_raiz_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)


def test_log_invalido():
    with pytest.raises(ValueError):
        log_natural(0)