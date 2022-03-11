# Variaveis
numero = int(input())
alfabeto = []
contador = 0

if numero <= 26:
    # Popula lista de alfabeto
    for a in range(ord('a'), ord('z')+1):
        alfabeto.append(chr(a))

    # Realiza impressão da Sequencia 
    for b in alfabeto:
        contador += 1
        if contador <= numero:
            print((b * contador).upper(), end ="\n")

