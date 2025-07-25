from usuarios import cadastrar_usuario, usuarios_db
from produtos import cadastrar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db
import unittest

class TestCadastroProduto(unittest.TestCase):
    
    # Limpa os "bancos" em memória
    def setUp(self):
        produtos_db.clear()
        usuarios_db.clear()
        compras_db.clear()
        print("\nBanco de dados limpo para o teste de integração.\n")
    
    def tearDown(self):
        print("\nTeste de integração concluído.\n")

    def test_fluxo_integra_compras(self):
        print("\nIniciando teste de integração do sistema de compras...\n")

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
        with self.assertRaises(ValueError):
            realizar_compra("1", "999")

        # 5. Verificar compras do usuário 1
        compras_usuario_1 = listar_compras("1")
        self.assertEqual(len(compras_usuario_1), 1)

        # 6. Verificar um usuário que não tem compras
        compras_usuario_2 = listar_compras("2")
        self.assertEqual(len(compras_usuario_2), 0)


# Executa o teste
if __name__ == "__main__":
    unittest.main()
