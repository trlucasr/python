inicio   = int(input())
fim      = int(input())
contador = 0

def validaprimo(num):
  if num < 2:
    return False 
  elif num == 2:
    print(num)
    return True 
  else:
    for a in range(2, num):
      if num % a == 0:
        return False
    print(num)
    return True

for a in range(inicio, fim + 1):
    if validaprimo(a):
      contador += 1

print('primos:', contador)