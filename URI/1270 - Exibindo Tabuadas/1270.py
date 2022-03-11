A = int(input())
B = int(input())

if (A > B):
  print('Nenhuma tabuada no intervalo!')
else:
  for posicao in range(A, B + 1):
    for a in range(1, 11):
      print(posicao,"x",a,"=",posicao * a)
    print('----------')