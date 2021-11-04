#EXERCICIO1
# vlrprd = float(input())
# qtd = int(input())

# total = (vlrprd * qtd)
# perdesc = 10 + qtd

# totdesc = total * perdesc / 100

# print("{:.2f}".format(total))
# print("{:.2f}".format(total - totdesc))

#EXERCICIO02
# tmp1 = int(input())
# tmp2 = int(input())
# tmp3 = int(input())

# tmptotal = (tmp1 + tmp2 + tmp3)

# print(tmptotal, "minutos")

#EXERCICIO03
# valor = float(input())
# poleg = 2.54

# total = valor * poleg

# print("{:.3f}".format(total))

#EXERCICIO04

# valor = int(input())

# if valor%2 == 0:
#     valor_impar = valor-1
#     valor_par = valor+2
# else:
#     valor_impar = valor-2
#     valor_par = valor+1

# print(valor_impar, valor_par)

# EXERCICIO05

# nota_trb = float(input())
# nota_prv = float(input())
# nota_minima_trb = 2.00

# media = (nota_trb + nota_prv) / 2

# if media >= 6:
#     print('aprovado')
# elif media < 6 and nota_trb >= nota_minima_trb :
#     print('talvez com a sub')
# else:
#     print('reprovado')

# EXERCICIO06

# dia_compra = input()
# prz_entreg = int(input())

# dia_da_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

# dia = dia_da_semana.index(dia_compra)

# dia_selecionado = dia_da_semana[dia + 1 : 7] + dia_da_semana[0 : dia]

# dia_de_entrega = dia_selecionado[prz_entreg - 1]

# if prz_entreg == 0:
#     print('chega hoje!')
# else:
#     print(f'sera entregue', {dia_de_entrega})

############################# EXERCICIOS JUDGE ###############################

## raio = float(input())
## n = 3.14159
## area = n * (raio * raio)
## print(f'A={"{:.4f}".format(area)}')

## n = input('Por favor, entre com sua idade: ')
## print (type(n))

## print(2 ** 2 ** 3 * 3)

##print('A=',"{:.4f}".format(area))
##print("A={}".format(round(area,4)))

## Media Ponderada
##A = float(input()) * 2
##B = float(input()) * 3
##C = float(input()) * 5
##X = (A + B + C) / 10
##print('MEDIA =', "{:.1f}".format(X))

## Diferença do produto
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# diff = (A * B - C * D)
# print('DIFERENCA =', diff)

## Calculo de Salario
# numero = int(input())
# hrtrab = int(input())
# vlrhr  = float(input())

# salario = vlrhr * hrtrab

# print('NUMBER =', numero)
# print('SALARY = U$', "{:.2f}".format(salario))

#SALARIO COM BONUS
# nome = str(input())
# salario = float(input())
# vendas = float(input())

# comis = vendas * (0.15)

# total = comis + salario

# print("TOTAL = R$","{:.2f}".format(total))


#CALCULO SIMPLES
# p1_cod, p1_num, p1_vlr = input().split(" ")
# p2_cod, p2_num, p2_vlr = input().split(" ")

# totpnivel1 = int(p1_num) * float(p1_vlr)
# totpnivel2 = int(p2_num) * float(p2_vlr)

# totgeral = totpnivel1 + totpnivel2

# print("VALOR A PAGAR: R$","{:.2f}".format(totgeral))

#CONSUMO
# x = int(input())
# y = float(input())

# media = (x/y)

# print("{:.3f}".format(media),"km/l")


#AREA
# A, B, C = input().split(" ")
# pi = 3.14159

# area = (float(A) * float(C))/2 
# circulo = pi * (float(C)**2) 
# trapezio = ((float(A) + float(B)) * float(C)) / 2 
# quadrado = float(B) * float(B) 
# retangulo = float(A) * float(B) 

# print("TRIANGULO:", "{:.3f}".format(area))
# print("CIRCULO:", "{:.3f}".format(circulo))
# print("TRAPEZIO:", "{:.3f}".format(trapezio))
# print("QUADRADO:", "{:.3f}".format(quadrado))
# print("RETANGULO:", "{:.3f}".format(retangulo))

#DISTANCIA
# import math

# x1,y1 = input().split(" ")
# x2,y2 = input().split(" ")

# calnivel1 = pow(float(x2)-float(x1),2)
# calnivel2 = pow(float(y2)-float(y1),2)

# total = calnivel1+calnivel2

# distancia = math.pow(total,0.5)

# print("{:.4f}".format(distancia))

#CALCULO DE MESES COM LISTA
# mes = int(input()) - 1
# lista = [[1,'January'],
#         [2,'February'],
#         [3,'March'],
#         [4,'April'],
#         [5,'May'],
#         [6,'June'],
#         [7,'July'],
#         [8,'August'],
#         [9,'September'],
#         [10,'October'],
#         [12,'November'],
#         [13,'December']]

# extenso = lista[mes][1]

# print(extenso)

#PARES ENTRE 5 NUMEROS
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())

# contador = 0
# n = 0

# lista = [num1,
#         num2,
#         num3,
#         num4,
#         num5]

# for n in lista:
#     if n % 2 == 0:
#         contador+=1


# print(contador, "valores pares") 

#ESTA DENTRO DO RANGE ?
# valor = float(input())
# n = int()
# intervalo = 0
# range = [[0,25],
#         [25,50],
#         [50,75],
#         [75,100]]

# for n in range:
#     if valor >= float(n[0]) and valor <= float(n[1]):
#         intervalo = n               

# if intervalo:
#     print("Intervalo",intervalo)
# else:
#     print("Fora de intervalo")

# n = float(input())

# if (n>=0 and n<=25): print ('Intervalo [0,25]')
# if (n>25 and n<=50): print ('Intervalo (25,50]')
# if (n>50 and n<=75): print ('Intervalo [50,75]')
# if (n>75 and n<=100): print ('Intervalo (75,100]')
# if (n<0 or n>100): print ('Fora de intervalo')

# #CASES
# nivel1 = str(input()).lower()
# nivel2 = str(input()).lower()
# nivel3 = str(input()).lower()

# if nivel1=="vertebrado":
#     if nivel2 == "ave":
#         if nivel3=="carnivoro":
#             print("aguia")
#         elif nivel3=="onivoro":
#             print("pomba")
#     elif nivel2 == "mamifero":
#         if nivel3=="onivoro":
#             print("homem")
#         elif nivel3=="herbivoro":
#             print("vaca")
# elif nivel1=="invertebrado":
#     if nivel2 == "inseto":
#         if nivel3=="hematofago":
#             print("pulga")
#         elif nivel3=="herbivoro":
#             print("lagarta")
#     elif nivel2 == "anelideo":
#         if nivel3=="hematofago":
#             print("sanguessuga")
#         elif nivel3=="onivoro":
#             print("minhoca")
# else:
#     print("Opção incorreta")


# valores = input().split()

# A = int(valores[0])
# B = int(valores[1])

# if A < B and ((B % A) / 2) == 0: 
#     print('Sao Multiplos')

# elif A < B and ((B % A) / 2) != 0: 
#     print('Nao sao Multiplos') 

# elif A > B and ((A % B) / 2) == 0: 
#     print('Sao Multiplos') 

# else:
#     print('Nao sao Multiplos')

#Funções
# nome = str(input())

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function(nome)

# n1, n2, n3, n4 = input().split()

# n1 = float(n1) * 2
# n2 = float(n2) * 3
# n3 = float(n3) * 4
# n4 = float(n4) * 1

# total_notas = n1 + n2 + n3 + n4 / 10

# print(f'Media:', total_notas '\n', 'oi')
