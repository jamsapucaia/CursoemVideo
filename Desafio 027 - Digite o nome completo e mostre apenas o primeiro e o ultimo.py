name = str(input('Digite o seu nome completo: '))

print('O seu nome completo eh: {}.'.format(name))
print('Poxa, seu nome eh muito longo, vamos utilizar apenas seu primeiro e ultimo nome, OK?')

newname = name.split()
first = newname[0]
last = newname[-1]

print('Primeiro nome:', first)
print('Ultimo nome:', last)

print('Seu nome no sistema ficara: {} {}.'.format(first, last))
