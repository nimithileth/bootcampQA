import requests
import pytest
import uuid

BASE_URL = "https://compassuol.serverest.dev/usuarios"

def gerar_email_dinamico():
    return f"qa_{uuid.uuid4().hex[:8]}@bootcamp.com.br"

def payload_valido():
    return {
        "nome": "Alexia QA",
        "email": gerar_email_dinamico(),
        "password": "senha_forte",
        "administrador": "true"
    }

def test_listar_usuarios_com_sucesso():
    print("\n Teste 1: Listando os usuários da base")
    resposta = requests.get(BASE_URL)
    dados = resposta.json()

    assert resposta.status_code == 200
    assert "quantidade" in dados
    print(f"Sucesso! A API listou {dados.get('quantidade')} usuários no total.")

def test_consultar_todos_usuarios():
    print("\n Teste 2: Listando os dados dos usuários da base")
    resposta = requests.get(BASE_URL)
    dados = resposta.json()

    assert resposta.status_code == 200
    assert "usuarios" in dados
    print(f"Sucesso! A API listou todos os usuários: \n{dados.get('usuarios')} .")

def test_cadastrar_usuario_valido():
    print("\n Teste 3: Cadastrando um usuário")
    dados_do_usuario = payload_valido()
    resposta = requests.post(BASE_URL, json=dados_do_usuario)

    assert resposta.status_code == 201
    assert resposta.json()["message"] == "Cadastro realizado com sucesso"
    print("Sucesso! Usuário cadastrado com sucesso.")

def test_cadastrar_usuario_duplicado():
    print("\nTeste 4: Tentando criar um usuário com e-mail repetido")
    dados_do_usuario = payload_valido()
    requests.post(BASE_URL, json=dados_do_usuario)
    resposta_duplicada = requests.post(BASE_URL, json=dados_do_usuario)

    assert resposta_duplicada.status_code == 400
    assert resposta_duplicada.json()["message"] == "Este email já está sendo usado"
    print("Sucesso! A API barrou o cadastro com o email duplicado")

def test_cadastrar_usuario_campos_faltando():
    print("\nTeste 5: Enviando formulário incompleto")
    dados_incompletos = {"nome": "Sem Email", "administrador": "true"}
    resposta = requests.post(BASE_URL, json=dados_incompletos)


    assert resposta.status_code == 400
    print("Sucesso! A API não aceitou o cadastro incompleto.")

def test_buscar_usuario_por_id():
    print("\nTeste 6: Buscando a ficha de um usuário pela ID")
    novo_usuario = requests.post(BASE_URL, json=payload_valido()).json()
    id_criado = novo_usuario["_id"]
    resposta = requests.get(f"{BASE_URL}/{id_criado}")

    assert resposta.status_code == 200
    assert resposta.json()["_id"] == id_criado
    print(f"Sucesso! Usuario com ID {id_criado} encontrado com sucesso.")

def test_atualizar_usuario_existente():
    print("\nTeste 7: Editando os dados de um usuário")
    novo_usuario = requests.post(BASE_URL, json=payload_valido()).json()
    id_criado = novo_usuario["_id"]
    dados_atualizados = payload_valido()
    dados_atualizados["nome"] = "Alexia (Nome Atualizado)"
    resposta = requests.put(f"{BASE_URL}/{id_criado}", json=dados_atualizados)

    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro alterado com sucesso"
    print("Sucesso! Os dados foram atualizados.")

def test_excluir_usuario_com_sucesso():
    print("\nTeste 8: Excluindo um usuário do sistema")
    novo_usuario = requests.post(BASE_URL, json=payload_valido()).json()
    id_criado = novo_usuario["_id"]
    resposta = requests.delete(f"{BASE_URL}/{id_criado}")

    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro excluído com sucesso"
    print("Sucesso! O usuário foi deletado da base.")


def test_excluir_usuario_inexistente():
   print("\nTeste 9: Tentando excluir quem não existe")
   resposta = requests.delete(f"{BASE_URL}/id_inexistente_456")

   assert resposta.status_code == 200
   assert resposta.json()["message"] == "Nenhum registro excluído"
   print("Sucesso! A API não apagou nada, como esperado.")

def test_cadastrar_usuario_email_formato_invalido():
    print("\nTeste 10: Validando se o sistema barra emails mal formatados")
    dados_errados = payload_valido()
    dados_errados["email"] = "email_errado_teste"
    resposta = requests.post(BASE_URL, json=dados_errados)

    assert resposta.status_code == 400
    assert "email deve ser um email válido" in resposta.text
    print("Sucesso! A API validou a estrutura do e-mail.")

def test_listar_usuarios_com_filtro_de_busca():
    print("\nTeste 11: Pesquisando com filtro na URL")
    link_com_filtro = f"{BASE_URL}?administrador=true"
    resposta = requests.get(link_com_filtro)

    assert resposta.status_code == 200
    print("Sucesso! A pesquisa com filtro funcionou sem dar erro.")


