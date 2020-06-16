# change_address_PZEM.py
Python3 script for changing the Modbus address of a PZEM-017 or 003
# check_settings_PZEM.py
Python3 script for reading the configuration of PZEM-017 or 003
<pre>
PZEM-003
PEZM-017


Spezifikationen :

Spannung:          0,05V* bis 300V
  Auflösung :                0,01V
  Messgemauigkeit :             1%
* unter 7V muss ein externen Netzteil benutzt werden

Strom : PZEM-003     0,01A bis 10A
        PZEM-017    0,02A bis 300A*
  Auflösung :                0,01A
  Messgemauigkeit :             1%

Leistung :  PZEM-003  0,1kW bis 3kW
            PZEM-017 0,2kW bis 90KW*
  Auflösung :                0,01W
  Messgemauigkeit :             1%           
* abhängig vom verwendem Shunt (50, 100, 200, 300A)

Verbrauchsmessung :        0-9999kWh
  Auflösung :                   1Wh
  Messgemauigkeit :             1%



Für die Spannung kann ein HIGH und ein LOW Alarm definiert werden.
 LOW     1V bis 350V     (in 0,01V Schritten)
 HIGH    5V bis 350V     (in 0,01V Schritten)
 Defaultwert für LOW ist 7V und für HIGH 300V

Die Schnittstelle ist
 RS485 / MODBUS-RTU
 Baudrate :                   9600
 Data Bits :                     8
 Stopbit :                       2
 Parity :                    keine

Die PZEM unterstützen folgene Funktions Codes:
 0x03(3)   Read Holding Register 
 0x04(4)   Read Input Register 
 0x06(6)   Write Single Register 
 0x41(65)  Calibration (nur über Adresse 0xF8 nutzbar) 
 0x42(66)  Reset Verbrauchszähler

Die Adresse kann zwischen 
 0x01(1) und 0xF7(247) festgelegt werden. 
 0x00(0) ist die Broadcastadresse 
 0xF8(248) kann benutzt werden um die PZEM anzuspechen, wenn nur EIN Gerät am Bus hängt. Nützlich 
 um Geräte zu konfigurieren oder wenn sowieso nur ein Gerät vorhanden ist.

Die Register welche mit Funktionscode 0x03 ausgelesen oder mit 0x06 geschrieben werden können:

 Register  |   Beschreibung                 |  Auflösung
 ----------|--------------------------------|----------------------
 0x0000    |   High voltage alarm threshold |  1LSB correspond
           |   (5-350V), default is 300V    |  to 0.01V
 ----------|--------------------------------|----------------------
 0x0001    |   Low voltage alarm threshold  |  1LSB correspond
           |   (1-350V) , defalut is 7V     |  to 0.01V
 ----------|--------------------------------|----------------------
 0x0002    |   ModBus-RTU Address           |  Range is
           |                                |  0x0001 - 0x00F7
 ----------|--------------------------------|----------------------
 0x0003    |   The current range            |  0x0001  100A
           |   (only PZEM-017)              |  0x0002   50A
           |                                |  0x0003  200A
           |                                |  0x0004  300A 
           
Die Register welche mit Funktionscode 0x04 ausgelesen werden können:

 Register  |   Beschreibung                 |  Auflösung
 ----------|--------------------------------|-----------------------------------------
 0x0000    |   Voltage value                |  1LSB correspond to O.O1V
 -------------------------------------------------------------------------------------
 0x0001    |   Current value                |  1LSB correspond to O.O1A
 -------------------------------------------------------------------------------------
 0x0002    |   Power value low 16bits       |  1LSB correspond to O. 1W
 0x0003    |   Power value high 16 bits     |
 -------------------------------------------------------------------------------------
 0x0004    |   Energy value low 16 bits     |  1LSB correspond to 1 Wh
 0x0005    |   Energy value high 16 bits    |
 -------------------------------------------------------------------------------------
 0x0006    |   High voltage alarm status    |  0xFFFF is alarm, 0x0000 is not alarm
 -------------------------------------------------------------------------------------
 0x0007    |   Low voltage alarm status     |  0xFFFF is alarm, 0x0000 is not alarm
</pre>
 
 

