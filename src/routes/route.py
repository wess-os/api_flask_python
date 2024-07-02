from flask import Blueprint, make_response, jsonify, request;
from database.db import mydb;

# Instancia o Blueprint
api = Blueprint('api', __name__)

# Método para retornar os dados
@api.route("/api/alunos/list", methods=["GET"])
def get_alunos():

    my_cursor = mydb.cursor();
    my_cursor.execute("SELECT * FROM alunos");
    list_alunos = my_cursor.fetchall();

    alunos = list();

    for aluno in list_alunos:
        alunos.append(
            {
                "id": aluno[0],
                "nome": aluno[1],
                "idade": aluno[2]
            }
        );

    return make_response (
        jsonify(
            message="Alunos cadastrados.",
            data=alunos
        )
    );

# Método para criar dados
@api.route("/api/alunos/create", methods=["POST"])
def create_aluno():

    aluno = request.json;

    if "nome" not in aluno or "idade" not in aluno:
        return make_response(jsonify(message="Informe os dados obrigatórios."), 400)
    
    try:
        nome = aluno.get("nome")
        idade = aluno.get("idade")
        
        # Verificar se já existe um aluno com o mesmo nome
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM alunos WHERE nome = %s", (nome,))

        if cursor.fetchone():
            return make_response(jsonify(message="Já existe um aluno com esse nome."), 400)
        
        # Insere o novo aluno no banco de dados
        cursor.execute("INSERT INTO alunos (nome, idade) VALUES (%s, %s)", (nome, idade))
        mydb.commit()
        
        return make_response(jsonify(message="Aluno inserido com sucesso!", data=aluno), 201)
    
    except ValueError:
        return make_response(jsonify(message="Idade deve ser um número inteiro."), 400)
    
    except Exception as e:
        print(e)
        return make_response(jsonify(message="Erro ao criar aluno."), 500)