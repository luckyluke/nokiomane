
class IOmanager():
    def __init__(self, core, conn, proto):
        self.core = core
        # inizializzo una connessione se conn e' diverso da None
        if conn=='usb':
            self.init_usb(proto)   
        elif not self.core.text:
            import NMgammu
    def init_usb(self, proto):
        if self.core.option.debug:
            print 'inizializzo connessione usb'
