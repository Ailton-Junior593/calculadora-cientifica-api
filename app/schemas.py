from enum import Enum
from pydantic import BaseModel, model_validator


class Operacao(str, Enum):
    SOMA = "+"
    SUBTRACAO = "-"
    MULTIPLICACAO = "*"
    DIVISAO = "/"
    POTENCIA = "^"
    YX = "yx"

    SQRT = "sqrt"
    EXP = "exp"

    SIN = "sin"
    COS = "cos"
    TAN = "tan"

    ASIN = "asin"
    ACOS = "acos"
    ATAN = "atan"

    LN = "ln"
    LOG = "log"

    NEG = "neg"
    PI = "pi"

    SIN_GRAUS = "sin_graus"
    COS_GRAUS = "cos_graus"
    TAN_GRAUS = "tan_graus"


class Calculo(BaseModel):
    operacao: Operacao
    n1: float | None = None
    n2: float | None = None

    @model_validator(mode="after")
    def validar(self):
        unarias = {
            "sqrt", "exp", "sin", "cos", "tan",
            "asin", "acos", "atan",
            "ln", "log",
            "neg", "pi",
            "sin_graus", "cos_graus", "tan_graus"
        }

        op = self.operacao.value

        if op in unarias:
            if self.n1 is None:
                raise ValueError(f"Operação '{op}' requer n1")
        else:
            if self.n1 is None or self.n2 is None:
                raise ValueError(f"Operação '{op}' requer n1 e n2")

        return self


class ResultadoResponse(BaseModel):
    success: bool
    operacao: str
    resultado: float