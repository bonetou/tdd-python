from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):

    def setUp(self):
        self.henrique = Usuario('Henrique')
        self.maicon = Usuario('Maicon')

        self.lance_henrique = Lance(self.henrique, 100.0)
        self.lance_maicon = Lance(self.maicon, 150.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_henrique)
        self.leilao.propoe(self.lance_maicon)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_maicon)
        self.leilao.propoe(self.lance_henrique)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_maicon)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini')
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_maicon)
        self.leilao.propoe(self.lance_henrique)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_henrique)
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_for_diferente(self):
        yuri = Usuario('Yuri')
        lance_yuri = Lance(yuri, 200.)

        self.leilao.propoe(self.lance_henrique)
        self.leilao.propoe(lance_yuri)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_o_lance_caso_o_ultimo_usuario_for_o_mesmo(self):
        lance_henrique2 = Lance(self.henrique, 200.0)
        self.leilao.propoe(self.lance_henrique)
        self.leilao.propoe(lance_henrique2)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebido)
