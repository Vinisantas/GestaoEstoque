import sqlite3
from app.model.database import verificar_banco

# Inserção de dados na tabela equipamentos
def cadastrar_equipamentos(dados):
        try:    
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
                cursor = conn.cursor()
                cursor.execute('''
                        INSERT INTO equipamentos ( patrimonio, nome, descricao, localizacao, data_de_compra)
                        VALUES (?, ?, ?, ?, ?)
                        ''', (dados["patrimonio"], dados["nome"], dados["descricao"], dados["localizacao"], dados["data_de_compra"]))
                conn.commit()
                conn.close()
                return {"status": "sucesso", "mensagem": "Equipamento cadastrado com sucesso!"}
        
        except sqlite3.Error as e:

                return {"status": "erro", "mensagem": str(e)}
