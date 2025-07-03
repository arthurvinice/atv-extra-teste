
from usuarios import consultar_usuario
from produtos import consultar_produto

compras_db = {}

def realizar_compra(usuario_id, lista_codigos_produtos):
    if not consultar_usuario(usuario_id):
        raise ValueError("Usuário inválido.")

    total = 0
    produtos = []

    for codigo in lista_codigos_produtos:
        produto = consultar_produto(codigo)
        if not produto:
            raise ValueError(f"Produto {codigo} não encontrado.")
        produtos.append(produto)
        total += produto["preco"]

    if usuario_id not in compras_db:
        compras_db[usuario_id] = []

    compras_db[usuario_id].append({
        "produtos": lista_codigos_produtos,
        "total": total
    })

    return total

def listar_compras(usuario_id):
    return compras_db.get(usuario_id, [])
