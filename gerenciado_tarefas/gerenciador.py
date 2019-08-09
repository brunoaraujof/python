from flask import Flask, request
from flask_restplus import Resource, Api, abort
from marshmallow import Schema, fields

class EsquemaTarefas(Schema):
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=True)

app = Flask("Gerenciador")

api = Api()
api.init_app(app)


@api.route("/tarefas")
class RecursoTarefas(Resource):

    id = 1

    def post(self):
        data, errors = EsquemaTarefas().load(request.json or {})
        tarefa = EsquemaTarefas().load(request.json)

        if errors:
            abort(400, **errors)
        data["concluida"] = False
        data["id"] = RecursoTarefas.id
        RecursoTarefas.id += 1
        return data