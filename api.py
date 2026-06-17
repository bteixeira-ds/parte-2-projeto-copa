from flask import Flask
from album import Album

app = Flask(__name__)

@app.route("/")
def inicio():
    return "API do album da copa"

@app.route("/figurinhas")
def listar_figurinhas():
    
    album = Album()
    album.carregar_arquivo()
    
    return album.figurinhas

@app.route("/pais/<nome_pais>")
def buscar_pais(nome_pais):
    
    album = Album()
    album.carregar_arquivo()
    
    resultado = []
    
    for figurinha in album.figurinhas:
        
        if figurinha["pais"].lower() == nome_pais.lower():
            resultado.append(figurinha)
            
    return resultado

@app.route("/info")
def info():
    
    album = Album()
    album.carregar_arquivo()
    
    return {
        "nome": "API Album da Copa 2026",
        "versao": "1.0",
        "total_figurinhas": len(album.figurinhas)        
    }
    
app.run()