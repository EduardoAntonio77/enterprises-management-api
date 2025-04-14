from database import database # Imports

def edit_representative_controller(repre, data): # Criando uma função que recebe como parametros "repre" que ja é o representante buscado na rota, e "data" que sera um dicionario contendo os novo dados passados em "request_get.json" na rota.

    if 'name' in data:
        repre.name = data['name'] # Verificando se o campo "name" foi enviado na requisição e caso sim, atualizara o atributo "name" do objeto "repre" com esse novo valor (isso sera repetido nas linhas abaixo.)
    if 'cnpj' in data:
        repre.cnpj = data['cnpj']
    if 'email' in data:
        repre.email = data['email']
    if 'phone' in data:
        repre.phone = data['phone']
    
    database.session.commit() # Salvando no banco de dados as alterações feitas.

    # OBS: Não é necessario atualizar todos os atributos do representante, é necessario que cada campo esteja dentro de um if para que o usuario tenha a liberdade de editar apenas os atributos que deseja.