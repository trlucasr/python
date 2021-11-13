valor = 0
soma = 0
unid = 2.50
valores = []

while valor == 0:
    valor = float(input())
    if valor > 0:
        valores.append(valor) 
        valor = 0 
  
for x in valores:
    soma += x

print('VC$', "{:.2f}".format(soma))
print('R$', "{:.2f}".format(soma * unid))
