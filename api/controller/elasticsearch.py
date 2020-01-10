from flask import Blueprint, request, make_response, jsonify

# ルーティングの設定
elasticsearch_router = Blueprint('elasticsearch_router', __name__)

@elasticsearch_router.route('/add_ticket', methods=['POST'])
def add_ticket():
    pass