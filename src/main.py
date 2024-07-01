from flask import Flask;
from routes.route import api;

# Instancio o app Flask
app = Flask(__name__);

# Não ordenar os dados
app.json.sort_keys = False;

# Busca as rotas
app.register_blueprint(api);

# Roda o app Flask
app.run();