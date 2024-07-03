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
        {
            "nome":"",
            "idade":""
        }

    - /api/alunos/create
        {
            "nome":"",
            "idade":""
        }

    - /api/alunos/<id_aluno>/update
        {
            "nome":"",
            "idade":""
        }
        
    - /api/alunos/<id_aluno>/delete

## 4: (executar o app)
    - python src/main.py