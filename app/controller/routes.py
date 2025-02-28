#Define as rotas da aplicação e utiliza a função verificar_banco para checar o status do banco de dados

import sqlite3
from flask import jsonify, make_response, request
from app.model.database import verificar_banco
from app import app
from app.model.models import cadastrar_equipamentos





@app.route('/', methods=['GET'])
def get_equipamentos():
                status_banco = verificar_banco()
                if status_banco ["status"] == "sucesso":
                        conn = sqlite3.connect("data/cadastro_patrimonio.sqlite")
                        cursor = conn.cursor()
                        #listar todos os equipamentos
                        lista = cursor.execute(''' SELECT * FROM  equipamentos ''').fetchall()
                        #fechamento da conexão
                        conn.close()
                        return make_response(
                                jsonify(lista),200
                        )
                else:
                        return make_response(
                                jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                        )




@app.route('/patrimonio/<string:patrimonio>', methods=['GET'])
def get_patrimonio(patrimonio):
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                try:
                        conn = sqlite3.connect("data/cadastro_patrimonio.sqlite")
                        cursor = conn.cursor()

                        #listar equipamentos por patrimônio
                        equipamento_patrimonio = cursor.execute(''' SELECT *  FROM equipamentos WHERE patrimonio = ? ''', (patrimonio,)).fetchall()
                        if not equipamento_patrimonio:
                                return make_response(
                                        jsonify(mensagem=f"Patrimônio não encontrado"),404
                                )
                        if equipamento_patrimonio:
                                return make_response(
                                        jsonify(equipamento=equipamento_patrimonio),200
                                )
                finally:
                        conn.close()
        else:
                return make_response(
                        jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                                )




@app.route('/equipamentos', methods=['POST'])
def post_equipamentos():
        dados = request.get_json()
        if not all(key in dados for key in ['patrimonio', 'nome', 'descricao', 'localizacao', 'data_de_compra']):
                return make_response(
                jsonify(mensagem="Dados inválidos ou incompletos."), 400
                )
        if not dados["patrimonio"] or not dados["nome"] or not dados["descricao"] or not dados["localizacao"] or not dados["data_de_compra"]:
                return make_response(
                        jsonify(mensagem="Nenhum campo pode estar vazio!"), 400
                )
        status_banco = verificar_banco()
        if status_banco["status"] == "sucesso":
                resultado = cadastrar_equipamentos(dados)
                if resultado["status"] == "sucesso":
                        return make_response(jsonify(mensagem=resultado["mensagem"]), 200)
                else:
                        return make_response(jsonify(mensagem=resultado["mensagem"]), 409)
        else:
                return make_response(
                jsonify(mensagem="Erro ao conectar ao banco de dados."), 500
                )






@app.route('/equipamentos/patrimonio/<string:patrimonio>', methods=['DELETE'])
def delete_equipamentos(patrimonio):
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                conn = sqlite3.connect("data/cadastro_patrimonio.sqlite")
                cursor = conn.cursor() 

                cursor.execute('''SELECT * FROM equipamentos WHERE patrimonio = ?''', (patrimonio,))
                equipamento = cursor.fetchall()
                if not equipamento:
                        conn.close()
                        return make_response(
                                jsonify(mensagem=f"Patrimônio {patrimonio} não encontrado"),404
                )
                if equipamento:
                        cursor.execute(''' DELETE FROM equipamentos WHERE patrimonio = ?''', (patrimonio,))
                        conn.commit()
                        conn.close()
                        return make_response(
                                jsonify(mensagem=f"Patrimônio {patrimonio} deletado com sucesso!"),200
                )
        else:
                return make_response(
                        jsonify(mensagem="Erro ao conectar com banco de dados."),500
                )
        