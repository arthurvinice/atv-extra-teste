from produto_db import produtos_db

def consultar_produto(codigo):
    return produtos_db.get(codigo)
