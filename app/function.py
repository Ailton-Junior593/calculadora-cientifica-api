import math


# =====================
# OPERAÇÕES BÁSICAS
# =====================

def soma(n1: float, n2: float) -> float:
    return n1 + n2


def subtracao(n1: float, n2: float) -> float:
    return n1 - n2


def multiplicacao(n1: float, n2: float) -> float:
    return n1 * n2


def divisao(n1: float, n2: float) -> float:
    if n2 == 0:
        raise ValueError("Divisão por zero não é permitida")

    return n1 / n2


# =====================
# POTÊNCIAS E RAÍZES
# =====================

def potencia(n1: float, n2: float) -> float:
    return n1 ** n2


def y_elevadox(y: float, x: float) -> float:
    return y ** x


def raiz_quadrada(x: float) -> float:
    if x < 0:
        raise ValueError(
            "Não existe raiz quadrada real para números negativos"
        )

    return math.sqrt(x)


def exponencial(x: float) -> float:
    return math.exp(x)


# =====================
# TRIGONOMETRIA
# =====================

def seno(x: float) -> float:
    return math.sin(x)


def seno_inverso(x: float) -> float:
    if x < -1 or x > 1:
        raise ValueError(
            "O valor deve estar entre -1 e 1"
        )

    return math.asin(x)


def cosseno(x: float) -> float:
    return math.cos(x)


def cosseno_inverso(x: float) -> float:
    if x < -1 or x > 1:
        raise ValueError(
            "O valor deve estar entre -1 e 1"
        )

    return math.acos(x)


def tangente(x: float) -> float:
    return math.tan(x)


def tangente_inversa(x: float) -> float:
    return math.atan(x)


# =====================
# LOGARITMOS
# =====================

def log_natural(x: float) -> float:
    if x <= 0:
        raise ValueError(
            "O valor deve ser maior que zero"
        )

    return math.log(x)


def log_base10(x: float) -> float:
    if x <= 0:
        raise ValueError(
            "O valor deve ser maior que zero"
        )

    return math.log10(x)


# =====================
# OUTROS
# =====================

def negativo(x: float) -> float:
    return -x


def pi() -> float:
    return math.pi


# =====================
# GRAUS
# =====================

def seno_graus(x: float) -> float:
    return math.sin(math.radians(x))


def cosseno_graus(x: float) -> float:
    return math.cos(math.radians(x))


def tangente_graus(x: float) -> float:
    return math.tan(math.radians(x))