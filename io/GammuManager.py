
#from gammu.Worker import GammuWorker
from mybindings.Worker import GammuWorker
from GammuActions import *

import gammu
import logging
import sys

log = logging.getLogger('gammu-manager')

#esempio di uso
'''
# Global debug level
gammu.SetDebugFile(sys.stderr)
gammu.SetDebugLevel('textall')

sm = gammu.StateMachine()
sm.ReadConfig()
sm.setConfig()

# Use global debug stub regardless configuration
#c = sm.GetConfig(0)
#c['UseGlobalDebugFile'] = True
#sm.SetConfig(0, c)

sm.Init()
'''

class GammuStatus:
    DISCONNECTED = 0
    CONNECTING = 1
    CONNECTED = 2
    EXECUTING = 3

class NMGammuManager(GammuWorker):
    '''
    Classe che gestisce le azioni di comunicazione del telefono tramite Gammu
    uso :
        settaggio configurazione
        inizio connessione
        esecuzione GammuActions
        termine connessione
    per l'uso interattivo si usa il metodo eseguiGammuAction per eseguire una GammuAction
    '''
    def __init__(self, core, config_manager, config=None):
        def callback(op, result, error, percent):
            self.NMCallback(op, result, error, percent)
        GammuWorker.__init__(self, callback)
        self._config_manager = config_manager
        #gammu.SetDebugFile(sys.stderr)
        gammu.SetDebugLevel('textall')

        # TODO:leggi configurazioni
        #########
        if not config:
            self.configure(self._config_manager.getConfig('E65'))
        #########

        # [nome, callback, fondamentale]
        self.status = GammuStatus.DISCONNECTED
        self.callbacks = []
        #self.actionCallback = None

    def execAction(self, gaction):
        self.status = GammuStatus.EXECUTING
        cmds = [(cmd[0], cmd[1]) for cmd in gaction.cmds]
        cbs = [(cmd[0], cmd[2], cmd[3]) for cmd in gaction.cmds]
        self.addCBs(cbs)
        self.enqueue_task(gaction.name, cmds)
        #self.actionCallback = lambda c: c.status = GammuStatus.CONNECTED; gaction.process()

    def eseguiGammuAction(self, gaction):
        if not self.config:
            log.error('Gammu non configurato!')

        self.connect()
        self.execAction(gaction)
        self.disconnect()

    # add cbs to the pending cbs
    def addCBs(self, cbs):
        self.callbacks.extend(cbs)

    def configure(self, config = None):
        if config == None:
            pass #autorilevamento cell
        else:
            self.config = config
            return GammuWorker.configure(self, config)

    def connect(self):
        if not self.config:
            # still to configure
            pass
        if self.status != GammuStatus.CONNECTED:
            self.status = GammuStatus.CONNECTING
            self.addCBs([['Init', lambda a: log.info('Connected!'), True]])
            self.initiate()
            # lock

    def disconnect(self, timeout=0):
        if self.status != GammuStatus.DISCONNECTED:
            self.addCBs([['Terminate', lambda a: log.info('Disconnectd!'), True]])
            self.terminate(timeout)
            # unlock

    def _abortAction(self):
        # ferma la GammuAction, il worker o il thread o quello che e
        self.callbacks = []
        self._thread.kill()
        #self.abort()
        

    def NMCallback(self, op, result, error, percent):
        '''
        Funzione richiamata alla fine dell'esecuzione di ogni operazione
        puo registrare log delle operazioni e valutarne il risultato
        parametri:
            op - nome dell'operazione appena eseguita
            result - risultato dell'operazione
            error - codice di errore
            percent - % sul totale delle operazioni della GammuAction
        '''

        #log.debug('%s %s %s %s' %(op, result, error, percent))

        if self.callbacks:
            cmd = self.callbacks[0]
            if cmd[0] != op:
                log.error('Errore nel flusso delle operazioni: aspettavo %s avuto %s. \n' %(cmd[0], op)+
                             'CBs: %s' %self.callbacks)
                self._abortAction()
                return

            if error != 'ERR_NONE':
                log.warning('Errore %s durante l\'esecuzione di %s' %(error, op))
                if cmd[2]:
                    log.error('Errore durante l\'esecuzione di un comando necessario,'+
                                 ' interrompo l\' azione')
                    self._abortAction()
                    return

                self.callbacks = self.callbacks[1:]
                return
                
            callback = cmd[1]
            callback(result)
            self.callbacks = self.callbacks[1:]
            log.debug('Operazione %s completata\nrisultato %s\nerrore %s' % (op, result, error))

        else:
            log.critical('Callback ricevuta dopo l\'abort di una gammuaction')

