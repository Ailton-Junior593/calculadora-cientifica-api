from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Operacao(str, Enum):
    SOMA = "+"
    SUBTRACAO = "-"
    MULTIPLICACAO = "*"
    DIVISAO = "/"

    POTENCIA = "^"
    Y_ELEVADO_X = "yx"

    RAIZ_QUADRADA = "sqrt"
    EXPONENCIAL = "exp"

    SENO = "sin"
    SENO_INVERSO = "asin"

    COSSENO = "cos"
    COSSENO_INVERSO = "acos"

    TANGENTE = "tan"
    TANGENTE_INVERSA = "atan"

    LOG_NATURAL = "ln"
    LOG_BASE10 = "log"

    NEGATIVO = "neg"

    PI = "pi"

    SENO_GRAUS = "sin_graus"
    COSSENO_GRAUS = "cos_graus"
    TANGENTE_GRAUS = "tan_graus"


class Calculo(BaseModel):
    operacao: Operacao
    n1: Optional[float] = None
    n2: Optional[float] = None


class ResultadoResponse(BaseModel):
    success: bool
    operacao: str
    resultado: float | str