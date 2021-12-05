carrinho = input().split()

if (carrinho != []):

  for i in range(len(carrinho)):
    carrinho[i] = int(carrinho[i])
  
def adicionar(lista, item):
  lista.append(item)

def remover(lista, item):
  if (item in lista):
    lista.remove(item)
  else:
    print(f'código {item} não encontrado')

def exibir(lista):
  lista.sort()
  
  for i in range(len(lista)):
    if (i < len(lista) - 1):
      print(lista[i], end=' ')
    else:
      print(lista[i])

comando = input().split()

while comando[0] != 'encerrar':
  if (comando[0] == 'adicionar'):
    adicionar(carrinho, int(comando[1]))
  elif (comando[0] == 'remover'):
    remover(carrinho, int(comando[1]))
  else:
    exibir(carrinho)

  comando = input().split()

exibir(carrinho)