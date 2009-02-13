from gammu.Worker import GammuWorker

log = []
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
    def __init__(self):
        GammuWorker.__init__(self, self.NMcallback)
    def configure(self, config = None):
        if config == None:
            pass #autorilevamento cell
        else:
            return GammuWorker.configure(self, config)
    def addcommand(self, command, params):
        GammuWorker.enqueue_command(self, command, params)
    def connect(self):
        GammuWorker.initiate(self)
    def disconnect(self, timeout=0):
        GammuWorker.terminate(self, timeout)
    def command_noninteractive(self, config, command, params):
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
