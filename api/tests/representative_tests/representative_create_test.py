# imports
import pytest
from tests.conftests import representative # mesmo que o python diga que essa import nao esta sendo acessado em lugar algum, ele esta sendo usado sim.

@pytest.fixture # Esse anotação esta indicando que a função abaixo sera um "contexto" de test, ou seja, ira executar um ações necessarias antes do teste, por exemplo passar informações no body da requisição como feito abaixo.
def test_representative_success(representative): # Função para executar o teste, aqui sim esta sendo usado o import de representative.
    body_request = {
        "name": "João da Silva",
        "email": "joao@email.com",
        "phone": "+55 11 91234-5678",
        "password": "joao1234",
        "cnpj": "1238237421"
    } # criando uma variavel que recebera um objeto que simula o que deve ser colocado no body da requisição para o teste

    route_respose = representative.post("/representative", json=body_request) # Aqui esta sendo criada uma variavel que executara um teste que por sua vez estara fazendo uma requisição com o metodo POST para a rota "/representative", enviando como dados em formato JSON o conteudo da variavel "body_request", logo depois ira armazenar o body da resposta e seu status code na propria variavel

    assert route_respose.status_code == 200 # "assert" esta verificando se o status code armazenado na variavel "route_response" é igual as 200.
    assert route_respose.json["message"] == "Successfully registered representative!" # Já este assert esta verificando se no body da resposta existe uma chave "message" com o valor "Successfully registered representative!".

def test_representative_missing_field(representative): # Função padrão para executar mais um teste
    body_request = {
        "name": "João da Silva",
        "phone": "+55 11 91234-5678",
        "password": "joao1234",
        "cnpj": "1238237421"
    } # Como neste teste estamos executando o erro de estar faltando um campo obrigatario no body da requisição, não havera o campo "email" de propósito para o teste

    route_response = representative.post("/representative", json=body_request) # defindo que o teste executara uma requisição com o metodo POST na rota e armazenara seu resultado e status code

    assert route_response.status_code == 400 # verificando se o status code foi igual a 400.
    assert "email" in route_response.json["message"] # verificando se existe o campo "email" na chave "message" no body da resposta.
