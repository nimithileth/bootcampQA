import requests

BASE_URL = "https://compassuol.serverest.dev/usuarios"

def test_bug_get_usuario_inexistente():
    print("\nTeste: GET retorna 400 em vez de 404 para ID inexistente")
    resposta = requests.get(f"{BASE_URL}/id_falso_qa_123")

    assert resposta.status_code == 404, f"Esperava 404, mas a API retornou {resposta.status_code} (bug)"

def test_bug_delete_usuario_inexistente():
    print("\nTeste: DELETE retorna 200 quando recurso não existe")
    resposta = requests.delete(f"{BASE_URL}/id_falso_qa_123")

    assert resposta.status_code == 404, f"Esperava erro 404, mas a API retornou {resposta.status_code} (bug)"
