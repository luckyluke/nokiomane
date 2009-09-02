
from io import *
from graphic import *
from event_manager import NMEventManager
from io import GammuActions

class NMcore():
    def __init__(self, options):
        self.options = options
        ####inizializzo core
            #leggo configurazione
        ####inizializzo io
        # inizializzo (io ah hoc) e quello supportato da gammu
        self.io = IOmanager.IOmanager(self, options.config)
        self._event_manager = NMEventManager(self)

        if not self.options.text:
            self.app = NMApp()
            self.app.core = self

    def run(self):
        #if(self.debug):
        #    print 'avvio del core'
        if not self.options.text:
            self.app.MainLoop()
        else:
            self.io.eseguiGammuAction(self.options.action, self.options.params)


