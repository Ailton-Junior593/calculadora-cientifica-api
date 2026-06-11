from app.function import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
    potencia,
    y_elevadox,
    raiz_quadrada,
    exponencial,
    seno,
    seno_inverso,
    cosseno,
    cosseno_inverso,
    tangente,
    tangente_inversa,
    log_natural,
    log_base10,
    negativo,
    pi,
    seno_graus,
    cosseno_graus,
    tangente_graus
)

OPERACOES = {
    "+": lambda n1, n2: soma(n1, n2),
    "-": lambda n1, n2: subtracao(n1, n2),
    "*": lambda n1, n2: multiplicacao(n1, n2),
    "/": lambda n1, n2: divisao(n1, n2),

    "^": lambda n1, n2: potencia(n1, n2),
    "yx": lambda n1, n2: y_elevadox(n1, n2),

    "sqrt": lambda n1, _: raiz_quadrada(n1),
    "exp": lambda n1, _: exponencial(n1),

    "sin": lambda n1, _: seno(n1),
    "asin": lambda n1, _: seno_inverso(n1),

    "cos": lambda n1, _: cosseno(n1),
    "acos": lambda n1, _: cosseno_inverso(n1),

    "tan": lambda n1, _: tangente(n1),
    "atan": lambda n1, _: tangente_inversa(n1),

    "ln": lambda n1, _: log_natural(n1),
    "log": lambda n1, _: log_base10(n1),

    "neg": lambda n1, _: negativo(n1),

    "sin_graus": lambda n1, _: seno_graus(n1),
    "cos_graus": lambda n1, _: cosseno_graus(n1),
    "tan_graus": lambda n1, _: tangente_graus(n1),

    "pi": lambda _, __: pi(),
}


def executar_operacao(
    operacao: str,
    n1: float | None = None,
    n2: float | None = None
):
    """
    Executa uma operação matemática baseada
    na chave informada.
    """

    if operacao not in OPERACOES:
        raise ValueError(
            f"Operação '{operacao}' não suportada."
        )

    return OPERACOES[operacao](n1, n2)