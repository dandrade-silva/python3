# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = str(input("""
===================
 TURNO DE TRABALHO
===================
ID   | Turno
[M]  | Matutino
[V]  | Vespertino
[N]  | Noturno
===================
Digite o ID do seu turno: """)).upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido!')
