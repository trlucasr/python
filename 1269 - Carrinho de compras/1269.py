lista_compras = input().split()

def convert(lista):
  if (lista != []):

    for i in range(len(lista)):
        lista[i] = int(lista[i])
    
    return lista

lista_compras = convert(lista_compras)

# Função para adicionar um item à lista
def append(lista, item):
  lista.append(item)

# Função para remover um item da lista
def remove(lista, item):
  if (item in lista):
    lista.remove(item)
  else:
    print(f'código {item} não encontrado')

# Função para exibir os itens da lista de forma ordenada
def show(lista):
  lista.sort()
  
  for i in range(len(lista)):
    if (i < len(lista) - 1):
      print(lista[i], end=' ')
    else:
      print(lista[i])

acao = input().split()

while acao[0] != 'encerrar':

  if (acao[0] == 'adicionar'):
    append(lista_compras, int(acao[1]))
  elif (acao[0] == 'remover'):
    remove(lista_compras, int(acao[1]))
  elif (acao[0] == 'exibir'):
    show(lista_compras)

acao = input().split()

show(lista_compras)


# # Definir a nossa lista de carrinho de compras
# carrinho_de_compras = input().split() # 1 2 3 4 => ['1', '2', '3', '4']

# # Verificação se o carrinho não for vazio, converter os itens string para inteiros
# if (carrinho_de_compras != []):

#   # Conversão de string para inteiros
#   for i in range(len(carrinho_de_compras)):
#     carrinho_de_compras[i] = int(carrinho_de_compras[i])
#     # ['3', '5'] => [3, 5]
  
# # Função para adicionar um item à lista
# def adicionar(lista, item):
#   lista.append(item)

# # Função para remover um item da lista
# def remover(lista, item):
#   if (item in lista):
#     lista.remove(item)
#   else:
#     print(f'código {item} não encontrado')

# # Função para exibir os itens da lista de forma ordenada
# def exibir(lista):
#   lista.sort()
  
#   for i in range(len(lista)):
#     if (i < len(lista) - 1):
#       print(lista[i], end=' ')
#     else:
#       print(lista[i])

# # Receber os comandos digitados (comando valor) pelo usuário 
# comando = input().split()
# # ['exibir']
# # ['adicionar', '1']

# # Estrutura de repetição enquanto "encerrar" não for digitado
# while comando[0] != 'encerrar':
#   # Se digitar "adicionar", executar a função que adiciona e assim por diante
#   if (comando[0] == 'adicionar'):
#     adicionar(carrinho_de_compras, int(comando[1]))
#   elif (comando[0] == 'remover'):
#     remover(carrinho_de_compras, int(comando[1]))
#   else:
#     exibir(carrinho_de_compras)

#   comando = input().split()

# exibir(carrinho_de_compras)

