total = int(input())
valormensal = int(input())
contador = 0

while total > 0 :
    saldo = total
    total = saldo - valormensal
    contador += 1

    if total < 0:
        total = 0

    print('pagamento:', contador)
    print('antes =', saldo)
    print('depois =', total)
    print('-----')
