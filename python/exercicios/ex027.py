nome = input('Digite seu nome completo: ').strip()
div = nome.split()
print('Primeiro nome: {}'.format(div[0]))
print('último nome: {}'.format(div[-1]))
print('último nome: {}'.format(div[len(div)-1]))