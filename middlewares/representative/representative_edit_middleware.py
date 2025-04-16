from models.representative_model import Representative # Imports

def representative_middleware(id): # Criando uma função que recebera como parametro um id vindo de sua respectiva rota
    return Representative.query.id(id) # Ira fazer uma busca no banco de dados na tabela de representante pelo id passado na requisição da rota.