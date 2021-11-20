
nota1 = int (input('primeiro bimestre '))
if nota1 >10:
    nota1 = int(input('voce digitou errado. Primeiro bimestre '))
nota2 = int (input('segundo bimestre '))
if nota2 >10:
    nota2 = int(input('voce digitou errado. Segundo bimestre '))

nota3 = int (input('teceiro bimestre '))
if nota3 >10:
    nota3 = int(input('voce digitou errado. Terceiro bimestre '))

nota4 = int (input('quarto bimestre '))
if nota4 >10:
    nota4 = int(input('voce digitou errado. Quarto bimestre '))


media = (nota1 + nota2 + nota3 + nota4) / 4
print('media: {}'.format(media))
