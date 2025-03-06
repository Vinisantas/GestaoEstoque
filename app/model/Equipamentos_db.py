import sqlite3
from app.model.Database import inicializar_banco, verificar_banco


verificar_banco()

# Criar tabela equipamentos
TABELA_EQUIPAMENTOS = '''
CREATE TABLE IF NOT EXISTS equipamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patrimonio INTEGER NOT NULL,
        nome TEXT NOT NULL,
        descricao TEXT,
        localizacao TEXT,
        data_de_compra TEXT NOT NULL
)
'''

inicializar_banco("data/equipamentos.sqlite", TABELA_EQUIPAMENTOS)


# Inserção de dados na tabela equipamentos
def cadastrar_equipamentos(dados):
        try:    
                conn = sqlite3.connect("data/equipamentos.sqlite")
                cursor = conn.cursor()
                verifica_existencia = cursor.execute(''' SELECT * FROM equipamentos WHERE patrimonio = ? ''', (dados["patrimonio"],)).fetchone()
                if verifica_existencia:
                        return {"status": "erro", "mensagem": "Equipamento já está cadastrado!"}
                else:
                        cursor.execute('''
                                INSERT INTO equipamentos ( patrimonio, nome, descricao, localizacao, data_de_compra)
                                VALUES (?, ?, ?, ?, ?)
                                ''', (dados["patrimonio"], dados["nome"], dados["descricao"], dados["localizacao"], dados["data_de_compra"]))
                
                        conn.commit()
                        conn.close()
                        return {"status": "sucesso", "mensagem": "Equipamento cadastrado com sucesso!"}
        
        except sqlite3.Error as e:

                return {"status": "erro", "mensagem": str(e)}

