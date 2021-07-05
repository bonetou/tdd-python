from unittest import TestCase
from src.leilao.dominio import Avaliador, Usuario, Leilao, Lance

class TestAvaliador(TestCase):
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        henrique = Usuario('Henrique')
        maicon = Usuario('Maicon')

        lance_henrique = Lance(henrique, 100.0)
        lance_maicon = Lance(maicon, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_henrique)
        leilao.lances.append(lance_maicon)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        henrique = Usuario('Henrique')
        maicon = Usuario('Maicon')

        lance_henrique = Lance(henrique, 100.0)
        lance_maicon = Lance(maicon, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_maicon)
        leilao.lances.append(lance_henrique)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        maior_lance_esperado = 150.0
        menor_lance_esperado = 100.0

        self.assertEqual(maior_lance_esperado, avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, avaliador.menor_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_o_leilao_tiver_um_lance(self):
        gui = Usuario('Gui')
        lance = Lance(gui, 150)
        leilao = Leilao('Celular')
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150, avaliador.menor_lance)
        self.assertEqual(150, avaliador.maior_lance)
        
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')

        lance_do_gui = Lance(yuri, 100.0)
        lance_do_yuri = Lance(yuri, 150.0)
        lance_do_vini = Lance(vini, 200.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)