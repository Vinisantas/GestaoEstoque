import sqlite3

from flask import app, jsonify, make_response
from app.model.Database import verificar_banco


@app.route('/manutencao', methods=['GET'])
def get_equipamentos():
                status_banco = verificar_banco()
                if status_banco ["status"] == "sucesso":
                        conn = sqlite3.connect("data/manutencoes.sqlite")
                        cursor = conn.cursor()
                        #listar todos os equipamentos
                        lista = cursor.execute(''' SELECT * FROM  manutencao ''').fetchall()
                        #fechamento da conexão
                        conn.close()
                        return make_response(
                                jsonify(lista),200
                        )
                else:
                        return make_response(
                                jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                        )