# Plano de Testes Automatizados - API ServeRest

## 1. Objetivo da Suíte
Garantir a qualidade, estabilidade e aderência aos contratos da API REST ServeRest. A suíte visa validar as regras de negócio, comportamentos de sucesso (happy path) e tratamento de erros nas rotas, assegurando que o sistema responda exatamente conforme documentado no Swagger.

## 2. Estratégia
* **Tipo de Teste:** Testes de API (Integração).
* **Ferramentas Utilizadas:** Python 3, framework Pytest e biblioteca Requests.
* **Arquitetura:** O projeto adota uma arquitetura híbrida que demonstra a evolução técnica da automação. A validação da rota de usuários e os testes de bugs utilizam **Programação Estruturada** com funções independentes e variáveis globais. Por outro lado, as rotas de Login e Produtos representam uma evolução e utilizam **Programação Orientada a Objetos (POO)**, encapsulando lógicas em Classes de Teste, como `TestLoginServeRest` e `TestProdutosServeRest`. Empregamos também o recurso de **Fixtures** para injeção de dependências e Setup/Teardown.

## 3. Escopo
* **O que está coberto:** A suíte obteve um alcance de **68,75%** de cobertura da API (baseado no critério de *Path Coverage* / Operações). Estão automatizadas 11 de um total de 16 operações possíveis, cobrindo de forma completa os endpoints de **Usuários**, **Login** e **Produtos**.
* **O que ficou de fora:** Todos os 5 endpoints da rota de **`/carrinhos`**. A decisão de mantê-los fora deste escopo se deu pela alta complexidade da massa de dados exigida. Essa etapa está planejada para ser desenvolvida em uma evolução futura (próximas sprints).

## 4. Cenários Implementados

**A. Rota de Usuários (`/usuarios`)**
* **Teste 1:** Listar os usuários da base.
* **Teste 2:** Consultar os dados dos usuários da base.
* **Teste 3:** Cadastrar novo usuário com dados válidos.
* **Teste 4:** Bloquear tentativa de cadastro com e-mail duplicado (repetido).
* **Teste 5:** Bloquear tentativa de cadastro enviando formulário incompleto (omitindo campos).
* **Teste 6:** Buscar a ficha de um usuário através de sua ID.
* **Teste 7:** Editar e atualizar os dados de um usuário existente.
* **Teste 8:** Excluir um usuário do sistema com sucesso.
* **Teste 9:** Validar a tentativa de excluir quem não existe no sistema.
* **Teste 10:** Validar se o sistema barra o envio de e-mail mal formatado.
* **Teste 11:** Pesquisar usuários utilizando filtro na URL.
* **Teste 12 [BUG Mapeado]:** Validar que GET retorna 400 em vez de 404 para ID inexistente.
* **Teste 13 [BUG Mapeado]:** Validar que DELETE retorna 200 quando recurso não existe.

**B. Rota de Login (`/login`)**
* Autenticar usuário com credenciais corretas.
* Bloquear login ao enviar senha incorreta.
* Bloquear login ao tentar acesso com e-mail inexistente.
* Bloquear login ao enviar campos obrigatórios vazios ou chaves ausentes.

**C. Rota de Produtos (`/produtos`)**
* Listar todos os produtos cadastrados.
* Cadastrar novo produto exigindo Token de Autorização de Administrador.
* Bloquear tentativa de cadastro de produto sem envio de Token.
* Buscar dados de um produto por ID.
* Atualizar informações (ex: alterar preço) de um produto existente.
* Excluir um produto do sistema.

## 5. Critérios de Qualidade (Definition of Done)
Para que um teste seja considerado finalizado neste projeto, ele deve seguir os seguintes critérios:
1. Utilizar o comando `assert` do Pytest para validar obrigatoriamente tanto o **Status Code** HTTP quanto mensagens específicas de resposta.
2. O teste não pode depender da execução de um teste anterior para funcionar. Massa de dados dinâmicos deve ser gerada individualmente em cada teste.
3. Todos os testes devem rodar com sucesso sem erros estruturais ao se invocar o comando `pytest -v` no terminal.