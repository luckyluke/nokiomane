
import GammuManager
import Data

class IOmanager():
    '''
    gestisce l'IO in maniera sia interattiva, cioe con GUI che non, cioe in modalita testuale di debug
    '''
    def __init__(self, core, config):
        self.core = core
        self.gammu = GammuManager.NMGammuManager(self.core)

        # leggi configurazioni
        if not config:
            self.gammu.configure(GammuManager.config5200)

    def eseguiGammuAction(self, gaction, gparams):
        if not self.gammu.config:
            print 'error: gammu not configured'
            # temp
            self.gammu.configure(GammuManager.config5200)
        self.gammu.connect()

    ''' monta il conteuto del telefono come un filesystem '''
    def crea_fs(self):
        pass

    def monta_fs(self):
        pass

    def smonta_fs(self):
        pass


