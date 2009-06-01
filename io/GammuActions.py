class GammuAction:
    # vari comandi da eseguire:
    # [ NOMECOMANDO PARAMETRI MEMORIZZAZIONERISULTATI SESIPUOANDAREAVANTIINCASODIERRORE ]
    # [{'string',  'parameters',    'callbacks',               fundamental}]
    def __init__(self):
        pass

class NMGetInfo(GammuAction):
    cmds = [['GetBatteryCharge', [], self._battery, False],
            ['GetManufacturer', [], self._manufacturer, False]
            ['GetModel', [], self._model, False]
            ['GetIMEI', [], self._imei, False]
            ['GetFirmware', [], self._firmware, False]]
    def __init__(self):
        GammuAction.__init__(self)

    def _battery(self, status):
        for x in status:
            if status[x] != -1:
                print "%20s: %s" % (x, status[x])

    def _manufacturer(self, manufacturer):
        print '%-15s: %s' % (_('Manufacturer'), manufacturer)

    def _model(self, model):
        print '%-15s: %s (%s)' % (_('Model'), model[0], model[1])

    def _imei(self, imei):
        print '%-15s: %s' % (_('IMEI'), imei)

    def _firmware(self, firmware):
        print '%-15s: %s' % (_('Firmware'), firmware[0])

    def process(self):

class NMReadAddressBook(GammuAction):
    SCANSIONE_MEMORIA = 0
    LETTURA_MEMORIA = 1
    ELABORAZIONE_RUBRICA = 2
    callbacks = [self.scan, self.mem, self.elab]
    def __init__(self):
        GammuAction.__init__(self)

    def scan(self):
        pass

    def mem(self):
        pass

    def elab(self):
        pass


