from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_api_soma():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "+",
            "n1": 10,
            "n2": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["resultado"] == 15


def test_api_divisao():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "/",
            "n1": 20,
            "n2": 4
        }
    )

    assert response.status_code == 200
    assert response.json()["resultado"] == 5


def test_api_raiz_quadrada():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "sqrt",
            "n1": 25
        }
    )

    assert response.status_code == 200
    assert response.json()["resultado"] == 5


def test_api_pi():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "pi"
        }
    )

    assert response.status_code == 200
    assert response.json()["resultado"] == 3.141592653589793


def test_api_divisao_por_zero():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "/",
            "n1": 10,
            "n2": 0
        }
    )

    assert response.status_code == 400


def test_api_operacao_invalida():

    response = client.post(
        "/api/calcular",
        json={
            "operacao": "banana",
            "n1": 10,
            "n2": 5
        }
    )

    # Enum do Pydantic rejeita antes da rota
    assert response.status_code == 422