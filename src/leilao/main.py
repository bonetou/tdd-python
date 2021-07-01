from dominio import Avaliador, Usuario, Leilao, Lance

henrique = Usuario('Henrique')
maicon = Usuario('Maicon')

lance_henrique = Lance(henrique, 100.0)
lance_maicon = Lance(maicon, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_henrique)
leilao.lances.append(lance_maicon)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')