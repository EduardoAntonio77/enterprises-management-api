# imports
from flask import jsonify;
from models.representative_model import Representative;

# Criando a função que recebera como parametro o id
def representative_delete_middleware(id):
    representant = Representative.query.get(id)
    if not representant:
        # Se não for encontrado nenhum representante com o id passado, retornara uma resposta json com um erro 404 (not found).
        return 'Representative not found'

    if representant.delete_at:
        # Se o campo "delete_at" do id passado ja tiver preenchido, retorna uma respota json com erro 400.
        return 'This representative has already been deleted' 
    
    # retorna nenhum valor (de erro, significa q foi tudo certo)
    return None
