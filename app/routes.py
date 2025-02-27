#Define as rotas da aplicação e utiliza a função verificar_banco para checar o status do banco de dados

import sqlite3
from flask import jsonify, make_response, request
from app.database import verificar_banco
from app import app
from app.model.models import cadastrar_equipamentos





@app.route('/', methods=['GET'])
def get_equipamentos():
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
                cursor = conn.cursor()

                #listar todos os equipamentos
                lista = cursor.execute(''' SELECT * FROM  equipamentos ''').fetchall()

                #fechamento da conexão
                conn.close()

                return make_response(
                        jsonify(mensagem=f"equipamentos: {lista}"),200
                )
        else:
                return make_response(
                        jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                )




@app.route('/patrimonio/<string:patrimonio>', methods=['GET'])
def get_patrimonio():
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
                cursor = conn.cursor()

                #listar equipamentos por patrimônio
                cursor.execute(''' SELECT *  FROM equipamentos WHERE patrimonio = ? ''').fetchall()
                equipamento_patrimonio = cursor.fetchall()

                if not equipamento_patrimonio:
                        conn.close()
                        return make_response(
                                jsonify(mensagem=f"Patrimônio {equipamento_patrimonio} não encontrado"),201
                )

                if equipamento_patrimonio:
                        return make_response(
                                jsonify(f"equipamento: {equipamento_patrimonio}"),200
                        )
        else:
                return make_response(
                        jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                )




@app.route('/equipamentos', methods=['POST'])
def post_equipamentos():
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                #defina o caminho do db 
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
                cursor = conn.cursor()

                # Capturar os dados da requisição (no caso, JSON)
                dados = request.get_json()
                patrimonio = dados.get('patrimonio')
                nome = dados.get('nome')
                descricao = dados.get('descricao')
                localizacao = dados.get('localizacao')
                data_de_compra = dados.get('data_de_compra')

                if patrimonio == ""  or nome == "" or descricao == "" or localizacao == "" or data_de_compra:
                        return make_response(
                                jsonify(mensagem=f"Insira dados válidos!"),201
                        )
                
                cadastrar_equipamentos()
                return make_response(
                jsonify(mensagem=f"Equipamento {nome} patrimônio {patrimonio} inserido com sucesso!"),201
                )
        else:
                return make_response(
                jsonify(mensagem="Erro ao conectar ao banco de dados."),500
                )





@app.route('/equipamentos/patrimonio/<string:patrimonio>', methods=['DELETE'])
def delete_equipamentos(patrimonio):
        status_banco = verificar_banco()
        if status_banco ["status"] == "sucesso":
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
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
                                jsonify(mensagem=f"Patrimônio {patrimonio} deletado com sucesso!"),204
                )
        else:
                return make_response(
                        jsonify(mensagem="Erro ao conectar com banco de dados."),500
                )
        