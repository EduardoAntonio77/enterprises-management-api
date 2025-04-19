# Sobre o MVC
A estrutura MVC (Model-View-Controller) é um padrão de arquitetura de software muito usado no desenvolvimento de aplicações, especialmente web. Ela separa a lógica do sistema em três camadas principais:

## 🧱 M - Model (Modelo)
Representa os dados e a lógica de negócios.
É onde você define as classes que representam os objetos do seu sistema (como usuários, produtos, etc.).
Também é responsável por interagir com o banco de dados.

## V - View (Visualização / Frontend)
É a interface com o usuário.
Mostra as informações para o usuário (como HTML, JSON ou outro formato de resposta).
Em APIs, a "view" pode ser a resposta JSON retornada.

## C - Controller (Controlador)
Orquestra tudo: recebe requisições, chama os modelos e escolhe qual visualização retornar.
Faz a ponte entre o usuário (View) e os dados (Model).



# Como é estruturado esse projeto?
## 1 - Schemas/ (diretório)
Responsável por criar a estrutura do banco de dados usando o ORM SQLAlchemy para criar tabelas, colunas, definir tipos que as colunas recebem, e relacionamentos entre tabelas.

## 2 - Database/ (diretório)
Responsável pela configuração da integração do banco de dados, definindo configurações sobre.

## 3 - Routes/ (diretório)
Responsável por definir os endpoints e métodos de cada rota existente na API, integrando Middlewares e também integrando Controllers.

## 4 - Middlewares/ (diretório)
Responsáveis por previnir erros à respeito da requisição, como por exemplo: campos obrigatórios faltando.

## 5 - Controllers/ (diretório)
São responsáveis por prevenir e segurar erros à respeito da manipulação do banco, como por exemplo: o campo "name" que chegou, não é do tipo String! Então, deve haver um tratamento de erro a respeito de coisas do tipo, e outras questões que podem gerar erro envolvendo o banco de dados.

## 6 - Models/ (diretório)
São responsáveis por criar modelos de edição/criação e deleção de dados. Modelos esses como: "findAll" ou "deleteSpecificTable" ou "updateSpecificData".