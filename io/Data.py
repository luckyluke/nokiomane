# dati riguardanti le connessioni disponibili in gammu
# info dal file Wammu/Data.py di wammu
# info piu di basso livello su common/gsmstate.c di gammu

Models = [
    'auto',
    'at',
    'alcatel',
    'nauto',
    'obex',
    'seobex',
    ]

Conn_Generic = [
    'at19200',
    'at115200',
    'obex',
    ]
Conn_Cable = [
    'at19200',
    'at115200',
    'fbusdlr3',
    'fbus',
    'mbus',
    'fbuspl2303',
    'phonetblue',
    'fbusblue',
    ]
Conn_IrDA_Win = [
    'irdaphonet',
    'irdaat',
    ]
Conn_IrDA_Other = [
    'irdaphonet',
    'at19200',
    ]
Conn_BlueRF = [
    'at19200',
    ]
Conn_Bluetooth_All = [
    'bluephonet',
    'bluefbus',
    'bluerfgnapbus',
    'blueat',
    'blueobex',
    'bluerfobex',
    'bluerfphonet',
    'bluerffbus',
    'bluerfat',
    ]
Conn_Bluetooth_Nokia = [
    'bluephonet',
    'bluefbus',
    'bluerfgnapbus',
    'bluerfphonet',
    'bluerffbus',
    'blueat',
    'bluerfat',
    'blueobex',
    'bluerfobex',
    ]
Conn_Bluetooth_Standard = [
    'blueat',
    'blueobex',
    'bluerfgnapbus',
    ]
Conn_Bluetooth = {
    'Sony-Ericsson' : Conn_Bluetooth_Standard,
    'Siemens' : Conn_Bluetooth_Standard,
    'BenQ' : Conn_Bluetooth_Standard,
    'Samsung' : Conn_Bluetooth_Standard,
    'LG' : Conn_Bluetooth_Standard,
    'Motorola' : Conn_Bluetooth_Standard,
    'Nokia' : Conn_Bluetooth_Nokia,
    'Alcatel' : Conn_Bluetooth_Standard,
    }

Devices = [
        '/dev/ttyS0',
        '/dev/ttyS1',
        '/dev/ttyUSB0',
        '/dev/ttyUSB1',
        '/dev/ttyACM0',
        '/dev/ttyACM1',
        '/dev/ircomm0',
        '/dev/rfcomm0',
        '/dev/usb/tts/0',
        ]
AllDevices = [
        (Conn_Cable, '/dev/ttyS%d', (0, 3), ['serial']),
        (Conn_Cable, '/dev/ttyUSB%d', (0, 3), ['serial', 'usb']),
        (Conn_Cable, '/dev/ttyACM%d', (0, 3), ['serial', 'usb']),
        (Conn_BlueRF, '/dev/rfrcomm%d', (0, 1), ['bluetooth']),
        (Conn_IrDA_Other, '/dev/ircomm%d', (0, 1), ['irda']),
        (Conn_Cable, '/dev/usb/tts/%d', (0, 3), ['serial', 'usb']),
        ]

ContactMemoryTypes = ['ME', 'SM']

# connessioni da usare, supportate nell'identificazione
class connessioni():
    generic = Conn_Generic
    cable = Conn_Cable
    bluez = Conn_Bluetooth_Nokia
    irda = Conn_IrDA_Other
