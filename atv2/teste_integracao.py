from usuarios import cadastrar_usuario, usuarios_db
from produtos import cadastrar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db
import unittest

class TestCadastroProduto(unittest.TestCase):
    def test_fluxo_integra_compras(self):
        print("\nIniciando teste de integração do sistema de compras...\n")

        # Limpa os "bancos" em memória
        def setUp(self):
            produtos_db.clear()
            usuarios_db.clear()
            compras_db.clear() 

        # 1. Cadastrar usuários e testar
        cadastrar_usuario("1", "Arthur")
        cadastrar_usuario("2", "Camilo")
        cadastrar_usuario("3", "David")
        
        self.assertEqual(usuarios_db["1"], "Arthur")
        self.assertEqual(usuarios_db["2"], "Camilo")
        self.assertEqual(usuarios_db["3"], "David")

        # 2. Cadastrar produtos e testar
        cadastrar_produto("1", "Xbox", 10.0)
        cadastrar_produto("2", "PS5", 20.0)
        cadastrar_produto("3", "Switch", 30.0)

        self.assertEqual(produtos_db["1"], {"nome": "Xbox", "preco": 10.0})
        self.assertEqual(produtos_db["2"], {"nome": "PS5", "preco": 20.0})  
        self.assertEqual(produtos_db["3"], {"nome": "Switch", "preco": 30.0})

        # 3. Realizar compra válida
        compra_valida = realizar_compra("1", "1")
        self.assertTrue(compra_valida)
        self.assertIn("1",compras_db)
        self.assertIn({"produtos": "1", "total": 10.0}, compras_db["1"])
        
        # 4. Tentar compra com produto inválido
        compra_produto_invalido = realizar_compra("1", "999")
        self.assertFalse(compra_produto_invalido)
        self.assertNotIn("999", compras_db["1"])

        # 5. Verificar compras do usuário 1


        # 6. Verificar um usuário que não tem compras


# Executa o teste
if __name__ == "__main__":
    unittest.main()
