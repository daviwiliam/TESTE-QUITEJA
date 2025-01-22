from flask import Blueprint, jsonify
from app.services import get_tipo_by_id
from typing import Tuple

routes_blueprint = Blueprint('routes', __name__)

# Rota para obter o tipo com base no 'tipo_id' fornecido na URL
@routes_blueprint.route('/tipo/<int:tipo_id>', methods=['GET'])
def get_tipo(tipo_id: int) -> Tuple:
    response, status = get_tipo_by_id(tipo_id)
    return jsonify(response), status

