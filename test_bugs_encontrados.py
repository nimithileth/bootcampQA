import requests
import pytest

BASE_URL = "https://compassuol.serverest.dev/usuarios"

@pytest.mark.xfail(reason="BUG CONHECIDO: A API retorna um código inesperado para ID inexistente. Comportamento esperado (REST): 404 Not Found.")
def test_bug_get_usuario_inexistente():
    print("\nTeste: GET com ID inexistente deve retornar 404")
    resposta = requests.get(f"{BASE_URL}/id_falso_qa_123")

    assert resposta.status_code == 404, f"Esperava 404, mas a API retornou {resposta.status_code} (bug)"

@pytest.mark.xfail(reason="BUG CONHECIDO: DELETE com ID inexistente retorna 200 em vez de 404 Not Found.")
def test_bug_delete_usuario_inexistente():
    print("\nTeste: DELETE com ID inexistente deve retornar 404")
    resposta = requests.delete(f"{BASE_URL}/id_falso_qa_123")

    assert resposta.status_code == 404, f"Esperava 404, mas a API retornou {resposta.status_code} (bug)"
