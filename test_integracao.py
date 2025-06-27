import cadastro_produto
import consulta_produto


def test_fluxo_cadastro_e_consulta():
    # Limpa base de dados
    cadastro_produto.usuarios_db.clear()

    # Cadastra um usuário
    assert cadastro_produto.cadastrar_usuario(1, "João")

    # Consulta o mesmo usuário
    usuario = consulta_produto.consultar_usuario(1)
    assert usuario == "João", f"Esperado 'João', obtido {usuario}"

    # Consulta um usuário inexistente
    assert consulta_produto.consultar_usuario(2) is None

test_fluxo_cadastro_e_consulta()