from distutils.log import info
import time
import datetime

#Função que calcula hora atual
def calcHora(hora, horaAtual):
    hora = time.strptime(hora,"%H:%M:%S")
    horaAtual = time.strptime(horaAtual,"%H:%M:%S")

    hora = datetime.timedelta(days=0 , hours=hora.tm_hour, minutes=hora.tm_min, seconds=hora.tm_sec)
    horaAtual = datetime.timedelta(days=0 , hours=horaAtual.tm_hour, minutes=horaAtual.tm_min, seconds=horaAtual.tm_sec)    

    return hora.seconds - horaAtual.seconds

#Traz a hora atual atualizada
def horaNow():
    #Verifico se a hora já chegou no atual
    infoTime  = time.ctime()
    infoTime  = infoTime.split()
    horaAtual = infoTime[3][0:8]

    return horaAtual

#Programar hora para despertar
hora = input('Qual o horario que você deseja que o despertador te acione?')
hora = hora+":00"

intervalo = calcHora(hora, horaNow())

while intervalo > 0:    
    print(intervalo)
    intervalo = calcHora(hora, horaNow())

if intervalo == 0:
    print("hora de acordar preguiçoso")
    
    

#toco alarme se chegar


#Soneca


#Cancelar

