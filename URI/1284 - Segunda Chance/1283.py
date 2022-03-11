N = int(input())

def obtemnotas_finais(notasiniciais, newnotas):
  qtdnotasalteradas = 0

  for i in range(len(notasiniciais)):
    if (newnotas[i] == 10 and notasiniciais[i] < 10):
      newnotas[i] = min(notasiniciais[i] + 2, 10)
      qtdnotasalteradas += 1
    else:
      newnotas[i] = notasiniciais[i]

  return qtdnotasalteradas

def shownotasalteradas(notasiniciais, notas_finais, qtdnotasalteradas):
  print(f'NOTAS ALTERADAS: {qtdnotasalteradas}')
  for i in range(N):
    nota_alterada = ('*' if notasiniciais[i] != notas_finais[i] else '-')
    print(f'{nota_alterada}({i+1:03}) original: {notasiniciais[i]:05.2f} | final: {notas_finais[i]:05.2f}')

def obtemnotas():
  notas = []

  for _ in range(N):
    notas.append(float(input()))

  return notas

if (1 <= N <= 999):
  notasiniciais = obtemnotas()
  newnotas = obtemnotas()
  qtdnotasalteradas = obtemnotas_finais(notasiniciais, newnotas)
  shownotasalteradas(notasiniciais, newnotas, qtdnotasalteradas)