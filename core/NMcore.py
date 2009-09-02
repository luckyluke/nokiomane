
from io import *
from graphic import *
from event_manager import NMEventManager

import logging

class NMcore():
    def __init__(self, options):
        self.options = options
        ####inizializzo core
            #leggo configurazione
        ####inizializzo io
        # inizializzo (io ah hoc) e quello supportato da gammu
        self.fs = NMFileSystemManager(self)
        self.gammu = GammuManager.NMGammuManager(self)
        self._event_manager = NMEventManager(self)

        if options.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.WARNING)

        if not self.options.text:
            self.app = NMApp()
            self.app.core = self

    def run(self):
        #if(self.debug):
        #    print 'avvio del core'
        if not self.options.text:
            self.app.MainLoop()
        else:
            #
            self.options.action = GammuManager.GetInfo()
            #
            self.gammu.eseguiGammuAction(self.options.action, self.options.params)


