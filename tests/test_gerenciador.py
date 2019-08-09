from gerenciado_tarefas import __version__
from gerenciado_tarefas.gerenciador import app
import pytest

@pytest.fixture
def cliente():
    with app.test_client() as cliente:
        app.config["TESTING"] = True
        yield cliente

def test_deve_existir_um_recurso_de_tarefas(cliente):
    resposta = cliente.post("/tarefas")
    assert resposta.status_code != 404

def test_recurso_tarefas_responde_ao_verbo_post(cliente):
    resposta = cliente.post("/tarefas")
    assert resposta.status_code != 405

def test_post_deve_conter_titulo_em_seu_corpo(cliente):
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 400
    assert "Missing data for required field." in resposta.json["titulo"]

def test_post_deve_conter_descricao_em_seu_corpo(cliente):
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 400
    assert "Missing data for required field." in resposta.json["descricao"]

def test_quando_bem_sucedido_deve_retornar_uma_tarefa(cliente):
    resposta = cliente.post(
            "/tarefas", json={"titulo" : "titulo" ,"descricao": "descricao"}
    )
    assert resposta.json["titulo"] == "titulo"
    assert resposta.json["descricao"] == "descricao"

def test_quando_bem_sucedido_deve_retornar_uma_tarefa_nao_concluida(cliente):
    resposta = cliente.post(
            "/tarefas", json = { "titulo":"titulo", "descricao": "descricao"}
    )
    assert resposta.json["concluida"] is False

def test_quando_bem_sucedido_uma_tarefa_deve_ter_id_unico(cliente):
    resposta_1 = cliente.post (
        "/tarefas",json = {"titulo": "titulo", "descricao":"descricao"}
    )
    resposta_2 = cliente.post (
        "/tarefas",json = {"titulo": "titulo", "descricao":"descricao"}
    )

    assert resposta_1.json["id"] != resposta_2.json["id"]
