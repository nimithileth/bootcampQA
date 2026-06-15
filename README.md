# Testes Automatizados da API ServeRest

Este projeto contém testes automatizados para validação dos endpoints da API ServeRest (Usuários, Login e Produtos) utilizando Python, Requests e Pytest. 

A arquitetura do projeto demonstra uma evolução técnica, utilizando uma abordagem híbrida: scripts baseados em **Programação Estruturada** para validações diretas e identificação de bugs, e **Programação Orientada a Objetos (POO)** com o uso de `Fixtures` para rotas complexas que exigem injeção de dependência e autenticação.

## Tecnologias Utilizadas

* Python 3.10 ou superior
* Pytest
* Requests

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/nimithileth/bootcampQA.git
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

Instale as bibliotecas necessárias utilizando o arquivo `requirements.txt` presente no repositório:
```bash
pip install -r requirements.txt
```

## Estrutura dos Testes e Arquivos

Os cenários de teste foram modularizados nos seguintes arquivos para facilitar a manutenção:

### 1. `test_serverRestUsuarios.py` (Programação Estruturada)
Focado no CRUD e validações da rota de `/usuarios`.
* Listagem e consulta detalhada de usuários.
* Cadastro de usuário válido e validação de e-mail duplicado.
* Validação de campos obrigatórios e formato de e-mail.
* Busca de usuário por ID e consulta utilizando filtro.
* Atualização de usuário existente.
* Exclusão de usuário (com sucesso e inexistente).

### 2. `test_login.py` (Programação Orientada a Objetos)
Focado nas regras de negócio e segurança da rota `/login`.
* Login com credenciais corretas.
* Validação de bloqueio com senha errada.
* Validação de bloqueio com e-mail inexistente.
* Validação de segurança ao enviar payload vazio ou com chaves ausentes.

### 3. `test_produtos.py` (Programação Orientada a Objetos)
Focado no CRUD da rota `/produtos`, utilizando `@pytest.fixture` para injeção de Tokens de Administrador.
* Listagem de produtos.
* Cadastro de produto exigindo Token de Administrador.
* Bloqueio de cadastro de produto sem Token no Header.
* Busca de produto por ID.
* Atualização de informações de produto existente.
* Exclusão de produto.

### 4. `test_bugs_encontrados.py` (Reporte de Falhas)
Arquivo dedicado a comprovar falhas de padronização HTTP (Status Codes) da API em relação à arquitetura REST.
* **Bug 1:** Busca por ID inexistente (GET `/usuarios`) retorna 400 em vez do padrão 404.
* **Bug 2:** Exclusão de ID inexistente (DELETE `/usuarios`) retorna sucesso 200 em vez do padrão 404 de erro.

## Análise de Cobertura de Testes

A cobertura de testes desta sprint foi calculada utilizando o método de **Path Coverage / Operator Coverage**, que divide a quantidade de rotas/métodos cobertos pela quantidade total de rotas da API REST.

* **Método de cálculo:** Operações automatizadas (11) / Total de operações da API ServeRest (16).
* **Cobertura total atingida:** **68,75%** da API.
* **Cenários fora do escopo:** Todos os 5 endpoints referentes à rota de **Carrinhos** (`/carrinhos`).
* **Justificativa:** Os testes de carrinhos foram mantidos fora do escopo inicial pois exigem um encadeamento altamente complexo de massa de dados (criar usuário -> login -> extrair token -> criar produto -> vincular o produto ao carrinho). Serão abordados em futuras evoluções do projeto.

## Executando os Testes

Para executar toda a suíte de testes:
```bash
pytest -v
```

Para executar visualizando as mensagens de `print` customizadas no terminal:
```bash
pytest -v -s
```

Para executar apenas um arquivo específico (exemplo: rodar apenas os testes de produtos):
```bash
pytest test_produtos.py -v
```

## API Utilizada

Base URL:
```text
https://compassuol.serverest.dev
```
Os testes realizam operações reais na API pública do ServeRest, criada exclusivamente para estudos e práticas de automação.

## Autor
**Alexia dos Santos de Oliveira**

Projeto desenvolvido para fins de estudo e prática de testes automatizados de API utilizando Pytest e Requests.
```
