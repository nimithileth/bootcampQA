# Testes Automatizados da API ServeRest

Este projeto contém testes automatizados para validação dos endpoints de usuários da API ServeRest utilizando Python, Requests e Pytest.

## Tecnologias Utilizadas

* Python 3.10 ou superior
* Pytest
* Requests

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/nimithileth/bootcampQA/blob/main/test_serverRestUsuarios.py
cd bootcampQA
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install pytest requests
```

Ou, caso exista um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Estrutura dos Testes

Os testes cobrem as seguintes funcionalidades da API de usuários:

| Teste    | Descrição                        |
| -------- | -------------------------------- |
| Teste 1  | Listagem de usuários             |
| Teste 2  | Consulta detalhada dos usuários  |
| Teste 3  | Cadastro de usuário válido       |
| Teste 4  | Validação de e-mail duplicado    |
| Teste 5  | Validação de campos obrigatórios |
| Teste 6  | Busca de usuário por ID          |
| Teste 7  | Atualização de usuário existente |
| Teste 8  | Exclusão de usuário              |
| Teste 9  | Exclusão de usuário inexistente  |
| Teste 10 | Validação de formato de e-mail   |
| Teste 11 | Consulta utilizando filtro       |

## Executando os Testes

Para executar todos os testes:

```bash
pytest -v
```

Para visualizar as mensagens exibidas pelos comandos `print`:

```bash
pytest -v -s
```

Para executar um teste específico:

```bash
pytest -v -s -k nome_do_teste
```

Exemplo:

```bash
pytest -v -s -k test_cadastrar_usuario_valido
```

## API Utilizada

Base URL:

```text
https://compassuol.serverest.dev/usuarios
```

Os testes realizam operações reais de criação, consulta, atualização e exclusão de usuários na API disponibilizada para estudos e práticas de automação.

## Autor
Alexia dos Santos de Oliveira

Projeto desenvolvido para fins de estudo e prática de testes automatizados de API utilizando Pytest e Requests.
