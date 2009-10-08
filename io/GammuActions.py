
__all__ = ['NMConnect', 'NMDisconnect', 'NMGetInfo', 'NMReadAddressBook']

class GammuAction(object):
    # sintassi di un comando:
    # [ NOMECOMANDO PARAMETRI MEMORIZZAZIONERISULTATI SESIPUOANDAREAVANTIINCASODIERRORE ]
    # [{'string',  'parameters',    'callbacks',               fundamental}]
    # ogni GammuAction deve avevrer un attributo self.cmds, una lista dei comandi da eseguire in ordine
    # al completamento della GammuAction il GammuManager deve richiamare una callback per dare i risultati
    def __init__(self, name):
        self.name = name

    def process(self):
        raise NotImplementedError

class NMConnect(GammuAction):
    def __init__(self):
        GammuAction.__init__(self, 'Connect')
        self.cmds = [['Init', [], self._init, True]]

    def _init(self, *params):
        print '%s' %str(params)

    def process(self):
        pass

class NMDisconnect(GammuAction):
    def __init__(self):
        GammuAction.__init__(self, 'Disconnect')
        self.cmds = [['Terminate', [], self._terminate, True]]

    def _terminate(self, *params):
        print '%s' %str(params)

    def process(self):
        pass

class NMGetInfo(GammuAction):
    def __init__(self):
        GammuAction.__init__(self, 'GetInfo')
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
        print 'okkk'

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

