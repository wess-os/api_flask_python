## 1: (criação do ambiente virtual)
    - python -m venv venv
    - source venv/bin/activate
    - pip install flask
    - pip install mysql-connector-python
    - pip install python-dotenv

    - obs: para sair do ambiente virtual, basta digitar o comando: 'source deactivate'

## 2: (conexão com o banco de dados)
    - acesse src/docs/CreateDatabase.sql e rode tudo oque está dentro do arquivo em seu banco de dados.

## 3: (rotas disponíveis)
    - /api/alunos/list
    - /api/alunos/create

## 4: (executar o app)
    - python src/main.py