# 🧮 Calculadora Científica API

Uma API REST desenvolvida com **FastAPI** para realizar operações matemáticas básicas e científicas, utilizando uma arquitetura organizada em camadas e testes automatizados.

## 🚀 Tecnologias Utilizadas

* Python 3.13
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* HTTPX

---

## 📂 Estrutura do Projeto

```text
calculadora-cientifica/
│
├── app/
│   ├── __init__.py
│   ├── function.py
│   ├── services.py
│   ├── schemas.py
│   └── routes.py
│
├── tests/
│   ├── test_functions.py
│   ├── test_services.py
│   └── test_routes.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Funcionalidades

### Operações Básicas

* Adição (+)
* Subtração (-)
* Multiplicação (*)
* Divisão (/)

### Potências e Raízes

* Potência (^)
* y elevado a x (yx)
* Raiz Quadrada (sqrt)
* Exponencial (exp)

### Trigonometria

* Seno (sin)
* Arco Seno (asin)
* Cosseno (cos)
* Arco Cosseno (acos)
* Tangente (tan)
* Arco Tangente (atan)

### Logaritmos

* Logaritmo Natural (ln)
* Logaritmo Base 10 (log)

### Outros

* Número negativo (neg)
* Constante PI (pi)
* Funções trigonométricas em graus

---

## 📦 Instalação

Clone o repositório:

```bash
git clone SEU_LINK_DO_GITHUB
```

Acesse a pasta do projeto:

```bash
cd calculadora-cientifica
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a Aplicação

```bash
uvicorn main:app --reload
```

Servidor disponível em:

```text
http://127.0.0.1:8000
```

---

## 📖 Documentação Swagger

Após iniciar a aplicação:

```text
http://127.0.0.1:8000/docs
```

A documentação interativa permite testar todos os endpoints diretamente pelo navegador.

---

## 🔍 Exemplo de Requisição

POST `/api/calcular`

```json
{
  "operacao": "+",
  "n1": 10,
  "n2": 5
}
```

Resposta:

```json
{
  "success": true,
  "operacao": "+",
  "resultado": 15
}
```

---

## 🧪 Executando os Testes

```bash
python -m pytest -v
```

Exemplo de saída:

```text
25 passed
```

---

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura em camadas:

```text
Requisição
    ↓
routes.py
    ↓
services.py
    ↓
function.py
    ↓
Retorno da API
```

### Responsabilidades

* **function.py** → Implementação das operações matemáticas.
* **services.py** → Regras de negócio e execução das operações.
* **schemas.py** → Validação de dados utilizando Pydantic.
* **routes.py** → Endpoints da API.
* **tests/** → Testes unitários e de integração.

---

## 📈 Melhorias Futuras

* Interface Web (HTML, CSS e JavaScript)
* Histórico de operações
* Banco de dados SQLite
* Docker
* Deploy em nuvem
* Tema dark/light para a interface

---

## 👨‍💻 Autor

Desenvolvido por Ailton Junior como projeto de estudo para aprofundamento em:

* Python
* FastAPI
* APIs REST
* Testes Automatizados
* Integração Front-End e Back-End
