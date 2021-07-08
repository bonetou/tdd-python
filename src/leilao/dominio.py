class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_valido(valor):
            raise ValueError(
                'Não pode propor um lance com valor maior que o valor da carteira')
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    def _valor_valido(self, valor):
        return valor > self.__carteira


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def propoe(self, lance: Lance):

        if self._lance_valido(lance):
            if not self._existe_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError(
                'O mesmo usuário não pode propor dois lances seguidos')

    @property
    def lances(self):
        # devolve uma cópia da lista, para não ter a mesma ref
        # assim, poderemos usar somente o método propoe
        return self.__lances[:]

    def _existe_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_lance_maior_que_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_valido(self, lance):
        return not self._existe_lances() or (self._usuarios_diferentes(lance) and
                                             self._valor_lance_maior_que_anterior(lance))
