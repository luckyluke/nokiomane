
from io import *
from graphic import *
from NMError import *
from event_manager import NMEventManager
from io import GammuActions

class NMcore():
    def __init__(self, option):
        self.debug = option.debug
        self.text = option.text
        self._event_manager = NMEventManager(self)
        # per sviluppo, sollevare questa eccezione per indicare una caratteristica non ancora implementata
        self.ex = DaFare
        # errore interno di funzionamento, sollevato manualmente
        self.err = Oops
        ####inizializzo core
            #leggo configurazione
        ####inizializzo io
        # inizializzo io ah hoc e quello supportato da gammu
        self.io = IOmanager.IOmanager(self, option.conn, option.proto)
        self.gammu = self.io.gammu
        ####inizializzo grafica
        if not self.text:
            self.app = NMApp()
            self.app.core = self
        if(self.debug):
            print 'inizializzazione del core ok'
    def run(self):
        if(self.debug):
            print 'avvio del core'
	    if self.text:
	        self.gammu.configure(GammuManager.config5200)
            self.gammu._connect()
            self.gammu.execAction(GammuActions.NMGetInfo())
            self.gammu._disconnect()
        # se in modalita grafica qua non ritorna finche non chiudo
#        if not self.text:
#            self.app.MainLoop()
