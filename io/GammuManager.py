from gammu.Worker import GammuWorker

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
    log = []
    def __init__(self, core):
        GammuWorker.__init__(self, self.NMcallback)
        self._status = GammuStatus.DISCONNECTED
        self._em = core._event_manager

        self._em.register(self._em.events.CONNECT, self._connect)
        self._em.register(self._em.events.DISCONNECT, self._disconnect)

    def execAction(self, action):
        # TODO: check for state machine status
        for cmd_ in action.cmds:
            self.enqueue_command(cmd_[0], cmd_[1])
            self.addCB(cmd_[0], cmd_[2], cmd_[3])
        result = action.process()

    # add cbs to the pending cbs
    def addCB(self, cmd, cbs, fundamental):
        pass

    def configure(self, config = None):
        if config == None:
            pass #autorilevamento cell
        else:
            return GammuWorker.configure(self, config)

    def _addcommand(self, command, params):
        self.enqueue_command(self, command, params)

    def _connect(self):
        self._status = GammuStatus.CONNECTING
        self.initiate(self)
        # FIXME: wait for the response?
        self._status = GammuStatus.CONNECTED

    def _disconnect(self, timeout=0):
        self.terminate(self, timeout)
        self._status = GammuStatus.DISCONNECT

    def _command_noninteractive(self, config, command, params):
        self.configure(config)
        self.addcommand(command, params)
        self.connect()
        self.disconnect()

    @staticmethod
    def NMcallback(op, result, error, percent):
        '''
        Funzione richiamata alla fine dell'esecuzione di ogni operazione
        puo registrare log delle operazioni e valutarne il risultato
        parametri:
            op - nome dell'operazione appena eseguita
            result - risultato dell'operazione, penso tipo valore di ritorno
            error - codice di errore in caso
            percent - % sul totale delle operazioni??????
        '''
        log.append((op, result, error))
        print str(log)
