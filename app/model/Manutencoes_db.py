from app.model.Database import inicializar_banco, verificar_banco

verificar_banco()


# Criar tabela manutencoes    
TABELA_MANUTENCAO =  '''
        CREATE TABLE IF NOT EXISTS manutencoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            motivo TEXT NOT NULL,
            patrimonio INTEGER NOT NULL,
            loja INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (patrimonio) REFERENCES equipamentos (id)
        )
        '''
# Inicializar o banco ao carregar o módulo
inicializar_banco("data/manutencoes.sqlite", TABELA_MANUTENCAO)