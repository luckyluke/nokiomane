
__all__ = ['GetInfo', 'ReadAddressBook']

class GammuAction:
    # sintassi di un comando:
    # [ NOMECOMANDO PARAMETRI MEMORIZZAZIONERISULTATI SESIPUOANDAREAVANTIINCASODIERRORE ]
    # [{'string',  'parameters',    'callbacks',               fundamental}]
    # ogni GammuAction deve avevrer un attributo self.cmds, una lista dei comandi da eseguire in ordine
    # al completamento della GammuAction il GammuManager deve richiamare una callback per dare i risultati
    def __init__(self):
        pass

class GetInfo(GammuAction):
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

class ReadAddressBook(GammuAction):
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


