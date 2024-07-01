from flask import Blueprint, make_response, jsonify, request;
from database.bd import Alunos;

# Instancia o Blueprint
api = Blueprint('api', __name__)

# Método para retornar os dados
@api.route("/api/alunos/list", methods=["GET"])
def get_alunos():
    return make_response (
        jsonify(
            message="Alunos cadastrados.",
            data=Alunos
        )
    );

# Método para criar dados
@api.route("/api/alunos/create", methods=["POST"])
def create_aluno():
    aluno = request.json;
    Alunos.append(aluno);
    return make_response (
        jsonify(
            message="Aluno inserido com sucesso!",
            data=aluno
        )
    );