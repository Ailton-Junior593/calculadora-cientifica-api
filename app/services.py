from app.function import *

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
    "cos": lambda n1, _: cosseno(n1),
    "tan": lambda n1, _: tangente(n1),

    "asin": lambda n1, _: seno_inverso(n1),
    "acos": lambda n1, _: cosseno_inverso(n1),
    "atan": lambda n1, _: tangente_inversa(n1),

    "ln": lambda n1, _: log_natural(n1),
    "log": lambda n1, _: log_base10(n1),

    "neg": lambda n1, _: negativo(n1),

    "sin_graus": lambda n1, _: seno_graus(n1),
    "cos_graus": lambda n1, _: cosseno_graus(n1),
    "tan_graus": lambda n1, _: tangente_graus(n1),

    "pi": lambda *_: pi(),
}


def executar_operacao(operacao: str, n1=None, n2=None):
    if operacao not in OPERACOES:
        raise ValueError("Operação inválida")

    try:
        resultado = OPERACOES[operacao](n1, n2)

        if resultado is None:
            raise ValueError("Resultado inválido")

        return resultado

    except ZeroDivisionError:
        raise ValueError("Divisão por zero não permitida")

    except TypeError:
        raise ValueError("Parâmetros inválidos para operação")