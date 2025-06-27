import cadastro_produto
import consulta_produto
import unittest
from produto_db import produtos_db

class TestCadastroProduto(unittest.TestCase):
    def setUp(self):
        produtos_db.clear() 

    def test_cadastrar_produto_novo(self):
        resultado = cadastro_produto.cadastrar_produto("001", "Produto A", 10.0)
        self.assertTrue(resultado)
        self.assertIn("001", cadastro_produto.produtos_db)

    def test_consultar_produto_existente(self):
        cadastro_produto.cadastrar_produto("001", "Produto A", 10.0)
        resultado = consulta_produto.consultar_produto("001")
        self.assertEqual(resultado, {"nome": "Produto A", "preco": 10.0})

    def test_consultar_produto_inexistente(self):
        resultado = consulta_produto.consultar_produto("999")
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()