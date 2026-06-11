from fastapi import APIRouter, HTTPException

from app.schemas import Calculo, ResultadoResponse
from app.services import executar_operacao

router = APIRouter(
    prefix="/api",
    tags=["Calculadora"]
)

@router.post(
    "/calcular",
    response_model=ResultadoResponse
)
def calcular(dados: Calculo):

    try:

        resultado = executar_operacao(
            operacao=dados.operacao.value,
            n1=dados.n1,
            n2=dados.n2
        )

        return ResultadoResponse(
            success=True,
            operacao=dados.operacao.value,
            resultado=resultado
        )

    except ValueError as erro:

        raise HTTPException(
            status_code=400,
            detail=str(erro)
        )