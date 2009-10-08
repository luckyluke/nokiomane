
from GammuActions import *

import gammu
import logging
import sys
import threading

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

class NMGammuManager:
    def __init__(self, core, config_manager):
        self._sm = gammu.Core.StateMachine()
        self._thread = GammuThread(self._sm)
        self._config_manager = config_manager
        #gammu.SetDebugFile(sys.stderr)
        gammu.SetDebugLevel('textall')

        # TODO:leggi configurazioni
        self.configure(self._config_manager.getDefaultConfig())

    def configure(self, config, pos=None):
        self._sm.SetConfig(0, config)

    def connect(self):
        self._thread.add(NMConnect())
        self._thread.start()

    def disconnect(self):
        self._thread.add(NMDisconnect())
        self._thread.stop()

    def eseguiGammuAction(self, gaction):
        self.connect()
        self._thread.add(gaction)
        self.disconnect()

class GammuThread(threading.Thread):
    def __init__(self, sm):
        threading.Thread.__init__(self)
        self._sm = sm
        self._running = True
        self.actions = []

    def add(self, gaction):
        self.actions.append(gaction)

    def run(self):
        while self._running or len(self.actions) > 0:
            if len(self.actions) > 0:
                gaction = self.actions[0]
                for cmd in gaction.cmds:
                    name, params, callback, essential = cmd
                    func = getattr(self._sm, name)
                    try:
                        can_process = True
                        if params is None:
                            result = func()
                        elif type(params) is dict:
                            result = func(**params)
                        else:
                            result = func(*params)

                        callback(result)

                    except gammu.Core.GSMError, info:
                        errcode = info[0]['Code']
                        error = gammu.Core.ErrorNumbers[errcode]
                        log.error('Errore %s in %s - %s' %(info[0]['Code'], info[0]['Where'], info[0]['Text']))

                        if essential:
                            can_process = False
                            log.error('Errore grave, blocco l\'azione %s' %(gaction.name))
                            break

                if can_process:
                    gaction.process()
                self.actions = self.actions[1:]

            else:
                pass

    def stop(self):
        self._running = False
        #self._sm.ReadDevice()
        self.join()

