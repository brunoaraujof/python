from flask import Flask, request
from flask_restplus import Resource, Api, abort
from marshmallow import Schema, fields
from marshmallow.validate import Length


class EsquemaTarefas(Schema):
    titulo = fields.Str(required=True, validate=Length(min=3, max=50))
    descricao = fields.Str(required=True, validate=Length(min=3, max=140))


app = Flask("Gerenciador")

api = Api()
api.init_app(app)


@api.route("/tarefas")
class RecursoTarefas(Resource):

    id = 1

    def post(self):
        data, errors = EsquemaTarefas().load(request.json or {})
        if errors:
            abort(400, **errors)
        data["concluida"] = False
        data["id"] = RecursoTarefas.id
        RecursoTarefas.id += 1
        return data