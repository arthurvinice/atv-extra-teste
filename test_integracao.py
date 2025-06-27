import cadastro_produto
import consulta_produto


def test_fluxo_cadastro_e_consulta():
    # Limpa base de dados
    cadastro_produto.produtos_db.clear()

    # Cadastra um produto
    assert cadastro_produto.cadastrar_produto(1, "Iphone", 20) is True

    # Consulta o mesmo produto
    produto = consulta_produto.consultar_produto(1)
    assert produto["nome"] == "Iphone", f"Esperado 'Iphone', obtido {produto}"

    # Consulta um produto inexistente
    assert consulta_produto.consultar_produto(2) is None

test_fluxo_cadastro_e_consulta()