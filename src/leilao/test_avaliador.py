from unittest import TestCase
from src.leilao.dominio import Avaliador, Usuario, Leilao, Lance

class TestAvaliador(TestCase):
    def test_avalia(self):
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

    def test_avalia2(self):
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

