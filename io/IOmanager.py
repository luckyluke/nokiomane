import GammuManager
import Data

class IOmanager():
    '''
    gestisce l'IO in maniera sia interattiva, cioe con GUI che non, cioe in modalita testuale di debug
    '''
    def __init__(self, core, conn, proto):
        self.core = core
        self.gammu = GammuManager.NMGammuManager()
        if self.core.text:
            if conn=='usb':
                self.init_usb(proto)
            elif conn == 'irda':
                self.init_irda(proto)
            elif conn == 'bluez':
                self.init_bluez(proto)
            else:
                # non dovrebbe essere mai alzata ma cmq
                raise self.core.err('hahaha hai sbagliato connessione!!!')

    def init_usb(self, proto):
        if self.core.debug:
            print 'inizializzo connessione usb'
        raise self.core.ex()
    def init_irda(self, proto):
        if self.core.debug:
            print 'inizializzo connessione irda'
        raise self.core.ex()
    def init_bluez(self, proto):
        if self.core.debug:
            print 'inizializzo connessione bluex'
        raise self.core.ex()
