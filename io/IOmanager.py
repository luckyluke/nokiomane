from GammuManager import NMGammuManager
import Data

class IOmanager():
    '''
    gestisce l'IO in maniera sia interattiva, cioe con GUI che non, cioe in modalita testuale di debug
    '''
    def __init__(self, core, conn, proto):
        self.core = core
        self.gammu = NMGammuManager(self.core)

    ''' monta il conteuto del telefono come un filesystem '''
    def crea_fs(self):
        pass

    def monta_fs(self):
        pass

    def smonta_fs(self):
        pass


