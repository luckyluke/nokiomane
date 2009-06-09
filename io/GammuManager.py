import gammu
from gammu.Worker import GammuWorker
from GammuActions import *

#log = []
#config6230 = {'name':'Nokia6230', 'model':'auto', 'connection':'dku5', 'port':'dev/ttyACM0'}
#config6230 = { 'port':'dev/ttyACM0'}
config6230 = {
            'StartInfo': 'no',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'at115200',
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '/dev/ttyACM0',
            'Localize': None,  # Set automatically by python-gammu
            'Model': '',
            }

config5200 = {
            'StartInfo': 'no',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'bluerfphonet',
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '00:1E:3A:B4:9B:47',
            'Localize': None,  # Set automatically by python-gammu
            'Model': 'auto',
            }

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
        (accodamento comandi)
        inizio connessione
        (eventuale accodamento comandi)
        termine connessione
    per l'uso interattivo si usa il metodo addcommand per far eseguire un comando
    addcommand esegue il comando se si e connessi, senno lo accoda in attesa di connessione
    '''
    def __init__(self, core):
        def callback(op, result, error, percent):
            self.NMCallback(op, result, error, percent)
        GammuWorker.__init__(self, callback)
        self._status = GammuStatus.DISCONNECTED
        self.config  = None
        # [nome, callback, fondamentale]
        self.callbacks = []

    def execAction(self, action):
        # TODO: check for state machine status
        cmds = [[cmd[0], cmd[1]] for cmd in action.cmds]
        cbs = [[cmd[0], cmd[2], cmd[3]] for cmd in action.cmds]
        self.addCBs(cbs)
        for cmd_ in action.cmds:
            # TODO: use tasks
            self.enqueue_command(cmd_[0], cmd_[1])

    # add cbs to the pending cbs
    def addCBs(self, cbs):
        self.callbacks.extend(cbs)

    def configure(self, config = None):
        if config == None:
            pass #autorilevamento cell
        else:
            self.config = config
            return GammuWorker.configure(self, config)

    def _addcommand(self, command, params):
        self.enqueue_command(self, command, params)

    def _connect(self):
        if not self.config:
            # still to configure
            pass
        self._status = GammuStatus.CONNECTING
        self.initiate()
        # FIXME: wait for the response?
        self._status = GammuStatus.CONNECTED

    def _disconnect(self, timeout=0):
        self.terminate(timeout)
        self._status = GammuStatus.DISCONNECTED

    def _command_noninteractive(self, config, command, params):
        self.configure(config)
        self.addcommand(command, params)
        self.connect()
        self.disconnect()

    def NMCallback(self, op, result, error, percent):
        '''
        Funzione richiamata alla fine dell'esecuzione di ogni operazione
        puo registrare log delle operazioni e valutarne il risultato
        parametri:
            op - nome dell'operazione appena eseguita
            result - risultato dell'operazione, penso tipo valore di ritorno
            error - codice di errore in caso
            percent - % sul totale delle operazioni??????
        '''
        if op == 'Init' or op == 'Terminate':
            return
        cmd = self.callbacks[0]
        if cmd[0] != op:
            return
        # FIXME
        if error != gammu.Core.ERR_NONE:
            if cmd[2]:
                # errore, interrompere l'azione
                pass
            else: pass
        callback = cmd[1]
        callback(result)
        self.callbacks = self.callbacks[1:]

