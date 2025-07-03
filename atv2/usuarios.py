
usuarios_db = {}

def cadastrar_usuario(id, nome):
    if id in usuarios_db:
        raise ValueError("Usuário já existe.")
    usuarios_db[id] = nome

def consultar_usuario(id):
    return usuarios_db.get(id)
