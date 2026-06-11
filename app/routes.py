from fastapi import APIRouter, HTTPException
from app.schemas import Calculo, ResultadoResponse
from app.services import executar_operacao

router = APIRouter(prefix="/api")

@router.post("/calcular", response_model=ResultadoResponse)
def calcular(dados: Calculo):

    try:
        resultado = executar_operacao(
            dados.operacao.value,
            dados.n1,
            dados.n2
        )

        return ResultadoResponse(
            success=True,
            operacao=dados.operacao.value,
            resultado=resultado
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        
        raise HTTPException(status_code=500, detail="Erro interno")