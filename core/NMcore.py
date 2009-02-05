
from io import *
#from graphic import *

class NMcore():
    def __init__(self, option):
        self.debug = option.debug
        self.text = option.text
        ####inizializzo core
            #leggo configurazione
        ####inizializzo io
        # inizializzo io ah hoc e quello supportato da gammu
        #self.io = IOmanager.IOmanager(self, option.conn, option.proto)
        self.gammu = GammuManager.NMGammuManager()
        ####inizializzo grafica
        #if not self.text:
         #   self.app = NMApp()
          #  self.app.core = self
        #self.app.MainLoop()
        if(self.debug):
            print 'inizializzazione del core ok'
    def run(self):
        if(self.debug):
            print 'avvio del core'
        self.gammu.configure(GammuManager.config6230)
        self.gammu.addcommand('GetModel',None)
        #self.gammu.addcommand('GetMemoryStatus',('DC',))
        #self.gammu.addcommand('GetMemoryStatus',('MC',))
        #self.gammu.addcommand('GetMemoryStatus',('RC',))
        #self.gammu.addcommand('GetMemoryStatus',('MT',))
        #self.gammu.addcommand('GetMemoryStatus',('FD',))
        #self.gammu.addcommand('GetMemoryStatus',('VM',))
        #self.gammu.addcommand('GetMemoryStatus',('SL',))
        self.gammu.connect()
        self.gammu.disconnect()
        # se in modalita grafica qua non ritorna finche non chiudo
        if not self.text:
           pass# self.app.MainLoop()
