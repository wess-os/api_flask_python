from flask import Blueprint, make_response, jsonify, request;
from database.db import mydb;

# Instancia o Blueprint
api = Blueprint('api', __name__)

# Método para criar dados
@api.route("/api/alunos/create", methods=["POST"])
def create_aluno():

    aluno = request.json;

    if "nome" not in aluno or "idade" not in aluno:
        return make_response(
            jsonify(
                message = "Informe os dados obrigatórios."
            ), 404
        );
    
    try:

        nome = aluno.get("nome");
        idade = aluno.get("idade");
        
        # Verificar se já existe um aluno com o mesmo nome
        cursor = mydb.cursor();
        cursor.execute("SELECT * FROM alunos WHERE nome = %s", (nome,));

        if cursor.fetchone():
            return make_response(
                jsonify(
                    message = "Já existe um aluno com esse nome."
                ), 404
            );
        
        # Insere o novo aluno no banco de dados
        cursor.execute("INSERT INTO alunos (nome, idade) VALUES (%s, %s)", (nome, idade));
        mydb.commit();
        
        return make_response(
            jsonify(
                message = "Aluno inserido com sucesso!", 
                data = aluno
            ), 201
        );
    
    except ValueError:

        return make_response(
            jsonify(
                message = "Idade deve ser um número inteiro."
            ), 404
        );
    
    except Exception as e:

        print(e);

        return make_response(
            jsonify(
                message = "Erro ao criar aluno."
            ), 500
        );
    
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

    return make_response(
        jsonify(
            message = "Alunos cadastrados.", 
            data = alunos
        ), 201
    );

# Método para atualizar dados
@api.route("/api/alunos/<int:id_aluno>/update", methods=["PUT"])
def update_aluno(id_aluno):

    # Verificar se o aluno existe
    my_cursor = mydb.cursor();
    my_cursor.execute("SELECT * FROM alunos WHERE id=%s", (id_aluno,));
    aluno_existente = my_cursor.fetchone();

    if not aluno_existente:
        return make_response(
            jsonify(
                message = "Aluno não encontrado."
            ), 404
        );

    # Extrair os dados da requisição
    nome = request.json.get('nome');
    idade = request.json.get('idade');

    if request.json.get('idade'):
        idade = int(request.json.get('idade'));

    # Verificar se todos os campos necessários foram fornecidos
    if not nome or not idade:
        return make_response(
            jsonify(
                message = "Informe os dados obrigatórios."
            ), 404
        );
    
    # Comparar os dados recebidos com os dados atuais
    if aluno_existente[1] == nome and aluno_existente[2] == idade:
        return make_response(
            jsonify(
                message = "Não há mudanças para serem aplicadas."
            ), 404
        );

    # Preparar a consulta SQL para atualizar o registro
    query = "UPDATE alunos SET nome=%s, idade=%s WHERE id=%s";
    values = (nome, idade, id_aluno);

    try:

        my_cursor = mydb.cursor();
        my_cursor.execute(query, values);
        mydb.commit();

        return make_response(
            jsonify(
                message = "Aluno atualizado com sucesso."
            ), 201
        );
    
    except Exception as e:

        print(e);
        
        return make_response(
            jsonify(
                message = "Erro ao atualizar o aluno."
            ), 500
        );

# Método para excluir dados
@api.route("/api/alunos/<int:id_aluno>/delete", methods=["DELETE"])
def delete_aluno(id_aluno):

    # Verificar se o aluno existe
    my_cursor = mydb.cursor();
    my_cursor.execute("SELECT * FROM alunos WHERE id=%s", (id_aluno,));
    aluno_existente = my_cursor.fetchone();

    if not aluno_existente:
        return make_response(
            jsonify(
                message = "Aluno não encontrado."
            ), 404
        );

    # Preparar a consulta SQL para excluir o registro
    query = "DELETE FROM alunos WHERE id=%s";
    values = (id_aluno,);

    try:

        my_cursor.execute(query, values);
        mydb.commit();

        return make_response(
            jsonify(
                message = "Aluno excluído com sucesso."
            ), 201
        );
    
    except Exception as e:

        print(e);

        return make_response(
            jsonify(
                message = "Erro ao excluir o aluno."
            ), 500
        );