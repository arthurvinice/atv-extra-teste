from produto_db import produtos_db

def cadastrar_produto(codigo, nome, preco):
    if codigo in produtos_db:
        return False  # Produto já cadastrado
    produtos_db[codigo] = {"nome": nome, "preco": preco}
    return True
