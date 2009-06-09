
__all__ = ''

class GammuAction:
    # vari comandi da eseguire:
    # [ NOMECOMANDO PARAMETRI MEMORIZZAZIONERISULTATI SESIPUOANDAREAVANTIINCASODIERRORE ]
    # [{'string',  'parameters',    'callbacks',               fundamental}]
    def __init__(self):
        pass

class NMGetInfo(GammuAction):
    def __init__(self):
        GammuAction.__init__(self)
        self.cmds = [['GetBatteryCharge', [], self._battery, False],
                     ['GetManufacturer', [], self._manufacturer, False],
                     ['GetModel', [], self._model, False],
                     ['GetIMEI', [], self._imei, False],
                     ['GetFirmware', [], self._firmware, False]] 

    def _battery(self, status):
        for x in status:
            if status[x] != -1:
                print "%-15s: %s" % (x, status[x])

    def _manufacturer(self, manufacturer):
        print '%-15s: %s' % (('Manufacturer'), manufacturer)

    def _model(self, model):
        print '%-15s: %s (%s)' % (('Model'), model[0], model[1])

    def _imei(self, imei):
        print '%-15s: %s' % (('IMEI'), imei)

    def _firmware(self, firmware):
        print '%-15s: %s' % (('Firmware'), firmware[0])

    def process(self):
        pass

class NMReadAddressBook(GammuAction):
    SCANSIONE_MEMORIA = 0
    LETTURA_MEMORIA = 1
    ELABORAZIONE_RUBRICA = 2
    def __init__(self):
        GammuAction.__init__(self)
        self.callbacks = [self.scan, self.mem, self.elab]

    def scan(self):
        pass

    def mem(self):
        pass

    def elab(self):
        pass


