# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer
# uso del módulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular
# el tiempo que queda de trabajo.

import time
import pprint

hora = time.strftime('%H')
minuto = time.strftime('%M')

INICIO_JORNADA = 10
FINAL_JORNADA = 19

print("Son las {} horas y {} minutos".
      format(hora, minuto))

if int(hora) < INICIO_JORNADA:
    print("Aún no es hora de empezar a trabajar")
elif int(hora) >= FINAL_JORNADA:
    print("Es hora de irse a casa")
else:
    print("Te quedan {} horas y {} minutos para irte a casa\nTu jornada empieza a las {}h y se acaba a las {}h".
          format(FINAL_JORNADA - 1 - int(hora), 59 - int(minuto), INICIO_JORNADA, FINAL_JORNADA))


