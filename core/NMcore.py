
from io import *
from graphic import *
from NMError import *

from event_manager import NMEventManager

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
                pass
            #self.gammu.configure(GammuManager.config6230)
            #self.gammu.addcommand('GetModel',None)
            #self.gammu.addcommand('GetMemoryStatus',('DC',))
            #self.gammu.addcommand('GetMemoryStatus',('MC',))
            #self.gammu.addcommand('GetMemoryStatus',('RC',))
            #self.gammu.addcommand('GetMemoryStatus',('MT',))
            #self.gammu.addcommand('GetMemoryStatus',('FD',))
            #self.gammu.addcommand('GetMemoryStatus',('VM',))
            #self.gammu.addcommand('GetMemoryStatus',('SL',))
            #self.gammu.connect()
            #self.gammu.disconnect()
        # se in modalita grafica qua non ritorna finche non chiudo
        if not self.text:
            self.app.MainLoop()
