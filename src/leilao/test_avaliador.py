from unittest import TestCase
from src.leilao.dominio import Avaliador, Usuario, Leilao, Lance

class TestAvaliador(TestCase):

    def setUp(self):
        self.henrique = Usuario('Henrique')
        self.maicon = Usuario('Maicon')

        self.lance_henrique = Lance(self.henrique, 100.0)
        self.lance_maicon = Lance(self.maicon, 150.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_henrique)
        self.leilao.propoe(self.lance_maicon)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_maicon)
        self.leilao.propoe(self.lance_henrique)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, avaliador.menor_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_maicon)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150, avaliador.menor_lance)
        self.assertEqual(150, avaliador.maior_lance)
        
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini')
        lance_do_vini = Lance(vini, 200.0)

        leilao = Leilao('Celular')

        leilao.propoe(self.lance_maicon)
        leilao.propoe(self.lance_henrique)
        leilao.propoe(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)