#Ponto de entrada para iniciar a aplicação Flask
from app import app
from app.model.Database import verificar_banco

if __name__ == '__main__':
    resultados = verificar_banco()
    for resultado in resultados:
        print(resultado["mensagem"])
    app.run(debug=True)
