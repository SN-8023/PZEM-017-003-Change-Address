#!/usr/bin/python3

# Ändert die ModBus-Adresse von PZEM-017 (...) Messgeräten

import minimalmodbus
from time import sleep 

CHANGE_TO_ADDRESS   =   3                   # Die zukünftige Adresse
NODE                =   248                 # Die derzeitige Adresse, alternativ 248 falls unbekannt. (Wenn 248 darf nur die Node am Bus hängen, deren Adresse geändert werden soll)
DEVICE              =   '/dev/ttyUSB0'      # Muss gegebenenfalls angepasst werden

# Konfiguration PZEM
PZ                  =   minimalmodbus.Instrument(DEVICE, NODE)
PZ.serial.baudrate  =   9600
PZ.serial.timeout   =   0.5
PZ.serial.bytesize  =   8
PZ.serial.parity    =   minimalmodbus.serial.PARITY_NONE
PZ.serial.stopbits  =   2

PZ2                 =   minimalmodbus.Instrument(DEVICE, CHANGE_TO_ADDRESS)

print('Adresse',NODE ,'wird geändert auf',CHANGE_TO_ADDRESS,'.' )

PZ.write_register(2,CHANGE_TO_ADDRESS,0,6)
sleep(1)

while 1:
    x = 0
    try:
        print(PZ2.read_registers(0,7,4))
        print('Erfogreich umgestellt.')
        break
    except:
        x = x + 1
        if x >= 5:
           print('Gerät antwortet nicht. :( ')
           break
