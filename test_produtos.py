import requests
import pytest
import uuid


class TestProdutosServeRest:
    URL_PRODUTOS = "https://compassuol.serverest.dev/produtos"
    URL_USUARIOS = "https://compassuol.serverest.dev/usuarios"
    URL_LOGIN = "https://compassuol.serverest.dev/login"

    @pytest.fixture
    def token_admin(self):

        email = f"qa_{uuid.uuid4().hex[:8]}@bootcamp.com"
        senha = "senha_admin"

        requests.post(self.URL_USUARIOS,
                      json={"nome": "Admin", "email": email, "password": senha, "administrador": "true"})
        resposta_login = requests.post(self.URL_LOGIN, json={"email": email, "password": senha})

        return resposta_login.json()["authorization"]

    def payload_produto(self):
        return {
            "nome": f"Produto QA {uuid.uuid4().hex[:8]}",
            "preco": 470,
            "descricao": "Mouse QA",
            "quantidade": 381
        }

    def test_listar_produtos(self):
        resposta = requests.get(self.URL_PRODUTOS)

        assert resposta.status_code == 200
        assert "produtos" in resposta.json()

    def test_cadastrar_produto_com_token_admin(self, token_admin):
        headers = {"Authorization": token_admin}

        resposta = requests.post(self.URL_PRODUTOS, json=self.payload_produto(), headers=headers)

        assert resposta.status_code == 201
        assert resposta.json()["message"] == "Cadastro realizado com sucesso"

    def test_cadastrar_produto_sem_token_admin(self):
        resposta = requests.post(self.URL_PRODUTOS, json=self.payload_produto())

        assert resposta.status_code == 401
        assert resposta.json()[
                   "message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    def test_buscar_produto_por_id(self, token_admin):
        headers = {"Authorization": token_admin}

        resp_post = requests.post(self.URL_PRODUTOS, json=self.payload_produto(), headers=headers)
        id_produto = resp_post.json()["_id"]

        resp_get = requests.get(f"{self.URL_PRODUTOS}/{id_produto}")

        assert resp_get.status_code == 200
        assert resp_get.json()["_id"] == id_produto

    def test_atualizar_produto(self, token_admin):
        headers = {"Authorization": token_admin}

        resp_post = requests.post(self.URL_PRODUTOS, json=self.payload_produto(), headers=headers)
        id_produto = resp_post.json()["_id"]

        payload_novo = self.payload_produto()
        payload_novo["preco"] = 9999
        resp_put = requests.put(f"{self.URL_PRODUTOS}/{id_produto}", json=payload_novo, headers=headers)

        assert resp_put.status_code == 200
        assert resp_put.json()["message"] == "Registro alterado com sucesso"

    def test_excluir_produto(self, token_admin):
        headers = {"Authorization": token_admin}

        resp_post = requests.post(self.URL_PRODUTOS, json=self.payload_produto(), headers=headers)
        id_produto = resp_post.json()["_id"]

        resp_delete = requests.delete(f"{self.URL_PRODUTOS}/{id_produto}", headers=headers)

        assert resp_delete.status_code == 200
        assert "Registro excluído com sucesso" in resp_delete.json()["message"]

    def test_bug_cadastrar_produto_preco_negativo(self, token_admin):
        headers = {"Authorization": token_admin}
        payload = self.payload_produto()
        payload["preco"] = -50

        resposta = requests.post(self.URL_PRODUTOS, json=payload, headers=headers)

        assert resposta.status_code == 400

    def test_bug_produto_tipo_invalido(self, token_admin):
        headers = {"Authorization": token_admin}
        payload = {
            "nome": f"Produto QA {uuid.uuid4().hex[:8]}",
            "preco": "cem",
            "descricao": "Mouse QA",
            "quantidade": 10
        }
        resposta = requests.post(self.URL_PRODUTOS, json=payload, headers=headers)

        assert resposta.status_code == 400

    def test_bug_cadastrar_produto_quantidade_negativo(self, token_admin):
        headers = {"Authorization": token_admin}
        payload = self.payload_produto()
        payload["quantidade"] = -1000

        resposta = requests.post(self.URL_PRODUTOS, json=payload, headers=headers)

        assert resposta.status_code == 400

        