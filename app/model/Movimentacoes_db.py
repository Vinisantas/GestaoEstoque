from app.model.Database import inicializar_banco, verificar_banco

verificar_banco()


# Criar tabela movimentacoes
TABELA_MOVIMENTACAO = '''
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patrimonio INTEGER NOT NULL,
            loja INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (patrimonio) REFERENCES equipamentos (id)
        )
        '''

# Inicializar o banco ao carregar o módulo
inicializar_banco("data/movimentacoes.sqlite", TABELA_MOVIMENTACAO)
