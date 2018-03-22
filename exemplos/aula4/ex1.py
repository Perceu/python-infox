
print('vou contar até 5:')
percorrer_isso = range(5)

for item in percorrer_isso:
    print(item)

print('Contei né ?')

print('vou fazer uma lista com 10 itens')

percorrer_isso = list(range(0,50,5))
for item in percorrer_isso:
    print(item)


print('vamos percorrer uma string')

nome = 'Perceu'
print(type(nome),nome, len(nome))
i=0

while i < 6:
    print(nome[i])
    i = i + 1
print("-"*50)

for c in nome:
    print(c)

for c in enumerate(nome):
    print(c)