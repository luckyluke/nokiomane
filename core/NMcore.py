
from io import *
from graphic import *
from event_manager import NMEventManager
from config_manager import ConfigManager

import logging
log = logging.getLogger('core')

class NMcore():
    def __init__(self, options):
        self.options = options
        self.fs = NMFileSystemManager(self)
        self.config = ConfigManager(self)
        self.gammu = GammuManager.NMGammuManager(self, self.config)
        self._event_manager = NMEventManager(self)

        if options.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.WARNING)

        if self.options.text:
            log.info('Starting Nokiomane in text mode...')

        else:
            log.info('Starting Nokiomane in graphic mode...')
            self.app = NMApp()
            self.app.core = self

    def run(self):
        if not self.options.text:
            self.app.MainLoop()
        else:
            #
            self.options.action = GammuManager.NMGetInfo()
            #
            self.gammu.eseguiGammuAction(self.options.action)


