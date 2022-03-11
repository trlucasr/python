# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: lucas.2103070@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    qtd_divisores = 0  
    candidato = 1
    while candidato <= n:
        if n % candidato == 0: 
            qtd_divisores += 1
        candidato += 1
    if qtd_divisores == 2:
        return True
    else:
        return False

def lista_primos(n):
    lista = []
    for i in range(2, n):  
        if eh_primo(i):    
            lista.append(i)
    return lista

def conta_primos(s):    
    dicionario = {}
    for item in s:
        if eh_primo(item):
            if item in dicionario:
                dicionario[item] += 1
            else:
                dicionario[item] = 1
    return dicionario


def eh_armstrong(n): 
    n = str(n)
    soma = 0
    for i in range(len(n)):
        soma += int(n[i])**len(n)
    if soma == int(n):
        return True
    else:
        return False


def eh_quase_armstrong(n): 
    n = str(n)
    soma = 0
    for i in range(len(n)):
        soma += int(n[i])**len(n)
    if soma == int(n) + 1 or soma == int(n)-1: 
        return True
    else:
        return False


def lista_armstrong(n):
    lista = []
    for i in range(0, n):
        if eh_armstrong(i):
            lista.append(i)
    return lista


def eh_perfeito(n):
    soma = 0
    for i in range (1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(1,n):
        if eh_perfeito(i):
            lista.append(i)
    return lista



