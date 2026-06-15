import requests
import pytest
import uuid


class TestLoginServeRest:
    URL_LOGIN = "https://compassuol.serverest.dev/login"
    URL_USUARIOS = "https://compassuol.serverest.dev/usuarios"

    def criar_usuario_admin(self):

        email = f"qa_{uuid.uuid4().hex[:8]}@bootcamp.com"
        senha = "senha_segura"
        payload = {
            "nome": "QA Login",
            "email": email,
            "password": senha,
            "administrador": "true"
        }
        requests.post(self.URL_USUARIOS, json=payload)
        return email, senha

    def test_login_credenciais_corretas(self):
        email, senha = self.criar_usuario_admin()
        resposta = requests.post(self.URL_LOGIN, json={"email": email, "password": senha})

        assert resposta.status_code == 200
        assert resposta.json()["message"] == "Login realizado com sucesso"
        assert "authorization" in resposta.json()

    def test_login_senha_errada(self):
        email, _ = self.criar_usuario_admin()
        resposta = requests.post(self.URL_LOGIN, json={"email": email, "password": "senha_errada_123"})

        assert resposta.status_code == 401
        assert resposta.json()["message"] == "Email e/ou senha inválidos"

    def test_login_email_inexistente(self):
        email_falso = f"falso_{uuid.uuid4().hex[:8]}@bootcamp.com"
        resposta = requests.post(self.URL_LOGIN, json={"email": email_falso, "password": "qualquer_senha"})

        assert resposta.status_code == 401
        assert resposta.json()["message"] == "Email e/ou senha inválidos"

    def test_login_campos_vazios(self):
        resposta = requests.post(self.URL_LOGIN, json={"email": "", "password": ""})

        assert resposta.status_code == 400
        assert "email não pode ficar em branco" in resposta.json()["email"]

    def test_login_chaves_ausentes(self):
        resposta = requests.post(self.URL_LOGIN, json={})

        assert resposta.status_code == 400

        dados_resposta = resposta.json()

        assert "email é obrigatório" in dados_resposta.get("email", "")
        assert "password é obrigatório" in dados_resposta.get("password", "")

    @pytest.mark.xfail(reason="BUG CONHECIDO: Campo 'administrador' aceita valores inválidos como 'talvez'. Comportamento esperado: 400 Bad Request.")
    def test_bug_administrador_invalido(self):
        payload = {
            "nome": "QA Teste",
            "email": f"qa_{uuid.uuid4().hex[:8]}@bootcamp.com",
            "password": "senha",
            "administrador": "talvez"
        }
        resposta = requests.post(self.URL_USUARIOS, json=payload)

        assert resposta.status_code == 400
