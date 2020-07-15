#!/usr/bin/python3

# Ändert die ModBus-Adresse von PZEM-017 (...) Messgeräten

import minimalmodbus
from time import sleep 

# ANPASSEN !
CHANGE_TO_ADDRESS   =   3                   # Die zukünftige Adresse
NODE                =   248                 # Die derzeitige Adresse, alternativ 248 falls unbekannt. (Wenn 248 darf nur die Node am Bus hängen, deren Adresse geändert werden soll)
DEVICE              =   '/dev/ttyUSB0'      # Muss gegebenenfalls angepasst werden ( '/dev/ttyS0' )
TYPE                =   '017'               # 017 oder 003

# Konfiguration PZEM, so lassen
PZ                  =   minimalmodbus.Instrument(DEVICE, NODE,debug=1)
PZ.serial.baudrate  =   9600
PZ.serial.timeout   =   1
PZ.serial.bytesize  =   8
PZ.serial.parity    =   minimalmodbus.serial.PARITY_NONE
PZ.serial.stopbits  =   2

PZ2                 =   minimalmodbus.Instrument(DEVICE, CHANGE_TO_ADDRESS)

print('Adresse',NODE ,'wird geändert auf',CHANGE_TO_ADDRESS,'.' )

PZ.write_register(2,CHANGE_TO_ADDRESS,0,6)
sleep(2)
x = 0
while 1:
    try:
        Shunts      =   ["100 A","50 A","200 A","300 A"]
        data        =   PZ2.read_registers(0,4 if TYPE is '017' else 3,3)
        print("\n High Voltage alarm  : ",(data[0] * 0.01), "V\n",
              "Low Voltage alarm   : ",   (data[1] * 0.01), "V\n",
              "Modbus-RTU Address  : ",   data[2],           "\n")
        if TYPE is "017":
           print("Current Range (017) : ",   Shunts[data[3]],   "\n")
        
        print('Erfogreich umgestellt.')
        break
    except:
        x = x + 1
        sleep(1)
        if x >= 5:
           print('Gerät antwortet nicht. :( ')
           break

# def FZEM_reset():
#    PZ._performCommand(66, '')             # Setzt den Energiezähler zurück
