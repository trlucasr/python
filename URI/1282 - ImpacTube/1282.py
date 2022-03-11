def dadoscanal(lista):
  for _ in range(lista):

    nome,inscritos,monetizacao,cntpremium = input().split(';')


    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    cntpremium = cntpremium == 'sim'


    canais.append([nome, inscritos, monetizacao, cntpremium])

def calc_bonificacao(premium_sim, premium_nao):
  lstbonificacao = []

  for canal in canais:
    nome = canal[0]
    inscritos = canal[1]
    vlrmonetizacao = canal[2]
    cntpremium = canal[3]

    if (cntpremium):
      vlrmonetizacao += inscritos // 1000 * premium_sim
    else:
      vlrmonetizacao += inscritos // 1000 * premium_nao
    
    lstbonificacao.append([nome, vlrmonetizacao])

  return lstbonificacao

def bonificacao(bonus):
  print('-----')
  print('BÔNUS')
  print('-----')

  for bonificacao in bonus:

    nome = bonificacao[0]
    valor = bonificacao[1]
    print(f'{nome}: R$ {valor:.2f}')

canais = []

# ENTRADAS
qtdcanais = int(input())

if (1 <= qtdcanais <= 200):
  dadoscanal(qtdcanais)
  
  premium_sim = float(input())
  premium_nao = float(input())

  bonificacao(calc_bonificacao(premium_sim, premium_nao))

# nome=input('Qual seu Nome:?')
# idade=int(input('Qual seu Nome:?'))
# salario=float(input('Qual seu Nome:?'))

# print('Olá'+nome+'')
# print('Apos uma decada voce estara com',idade+10,'anos')
# print('Se salario com 25% de aumento é:',salario*(25/100))

# i = int(input())
# s = input()

# if s == 'M':
#   prob = (1.09*i + 86.71)/100
# elif s == 'F':
#   prob = (-1.09*i + 13.29)/100
# else:
#   prob  = 'Sexo inválido'

# print(prob)


# smarts = int(input('Smartphones?'))
# abigos = int(input('Abigos?'))

# print(f'Megam e amigos receberão {smarts // abigos+1} smarts')
# print(f'Para adoção serão {smarts % abigos+1} smarts')
