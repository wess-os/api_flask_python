## 1: (criação do ambiente virtual)
    - python -m venv venv
    - source venv/bin/activate
    - pip install flask

    - obs: para sair do ambiente virtual, basta digitar o comando: 'source deactivate'

## 2: (executar o app)
    - python src/main.py

## 3: (rotas disponíveis)
    - /api/alunos/list
    - /api/alunos/create

## 4: (conexão com o banco de dados)
    - por hora, os dados são inseridos no arquivo bd.py, mas futuramente será criado a conexão com o banco de dados