#!/usr/bin/python3

# Register  |       Descriptoin              |  Resoulution
# ----------|--------------------------------|----------------------
# 0x0000    |   High voltage alarm threshold |  1LSB correspond
#           |   (5-350V), default is 300V    |  to 0.01V
#-----------|--------------------------------|----------------------
# 0x0001    |   Low voltage alarm threshold  |  1LSB correspond
#           |   (1-350V) , defalut is 7V     |  to 0.01V
#-----------|--------------------------------|----------------------
# 0x0002    |   ModBus-RTU Address           |  Range is
#           |                                |  0x0001 - 0x00F7
#-----------|--------------------------------|----------------------
# 0x0003    |   The current range            |  0x0001  100A
#           |   (only PZEM-017)              |  0x0002   50A
#           |                                |  0x0003  200A
#           |                                |  0x0004  300A
#           |                                | 


import minimalmodbus
from time import sleep
                                                                  
pz                  =   minimalmodbus.Instrument('/dev/ttyUSB0', 248, debug=0)
pz.serial.baudrate  =   9600                                 #    ^--- Modbus RTU address 1 - 247, if only one device on the bus, also works 248.
pz.serial.timeout   =   1
pz.serial.bytesize  =   8
pz.serial.parity    =   minimalmodbus.serial.PARITY_NONE
pz.serial.stopbits  =   2

x                   =   0

while 1:
    try:
        Shunts      =   ["100 A"," 50 A","200 A","300 A"]
        data        =   pz.read_registers(0,4,3)

        print("\n High Voltage alarm  : ","{:8.2f}".format(float((data[0] * 0.01))), "V\n",
              "Low Voltage alarm   : ",   "{:8.2f}".format(float((data[1] * 0.01))), "V\n",
              "Modbus-RTU Address  : ",   "{:8.0f}".format(data[2]),                  "\n",
              "Current Range (017) :      ",                        Shunts[data[3]],  "\n")
        
        print('Erfog.')
        break
    except:
        x = x + 1
        sleep(1)
        if x >= 5:
           print('Scotty, we have a problem ... :( ')
           break


