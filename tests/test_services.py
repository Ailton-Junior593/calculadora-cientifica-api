import pytest

from app.services import executar_operacao


def test_service_soma():

    resultado = executar_operacao(
        operacao="+",
        n1=10,
        n2=5
    )

    assert resultado == 15


def test_service_subtracao():

    resultado = executar_operacao(
        operacao="-",
        n1=10,
        n2=5
    )

    assert resultado == 5


def test_service_multiplicacao():

    resultado = executar_operacao(
        operacao="*",
        n1=10,
        n2=5
    )

    assert resultado == 50


def test_service_divisao():

    resultado = executar_operacao(
        operacao="/",
        n1=20,
        n2=4
    )

    assert resultado == 5


def test_service_potencia():

    resultado = executar_operacao(
        operacao="^",
        n1=2,
        n2=3
    )

    assert resultado == 8


def test_service_sqrt():

    resultado = executar_operacao(
        operacao="sqrt",
        n1=25
    )

    assert resultado == 5


def test_service_pi():

    resultado = executar_operacao(
        operacao="pi"
    )

    assert resultado == 3.141592653589793


def test_operacao_invalida():

    with pytest.raises(ValueError):

        executar_operacao(
            operacao="banana",
            n1=10,
            n2=5
        )


def test_divisao_por_zero_service():

    with pytest.raises(ValueError):

        executar_operacao(
            operacao="/",
            n1=10,
            n2=0
        )