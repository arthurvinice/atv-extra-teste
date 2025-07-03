
produtos_db = {}

def cadastrar_produto(codigo, nome, preco):
    if codigo in produtos_db:
        raise ValueError("Produto já existe.")
    produtos_db[codigo] = {"nome": nome, "preco": preco}

def consultar_produto(codigo):
    return produtos_db.get(codigo)
