total = []
tempo = int(input())

def exibe(media):
  print(f'MEDIA: {media:.2f}')

def tempo_abaixo(media):
  if(tempo < media):
    print(tempo)

def add_lista():
  total.append(tempo)

while (tempo >= 0):
  add_lista()
  tempo = int(input())

def calcula():
  media = sum(total) / len(total)
  return media

exibe(calcula())

for tempo in total:
  if ( tempo >= 0 ):
    tempo_abaixo(calcula())