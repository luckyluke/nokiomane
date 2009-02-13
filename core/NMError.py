class NMError(StandardError):
    def __init__(self, s=''):
        self.s = s

# per segnalare quello che ancora non e implementato
class DaFare(NMError):
    def __init__(self, s='hhhhhhh'):
        NMError.__init__(self)
    def __str__(self):
        return 'Da Fare: %s' %(self.s)

# per segnalare errori di funzionamento
class Oops(NMError):
    def __init__(self, s):
        NMError.__init__(self)
    def __str__(self):
        return 'Errore: %s' %(self.s)
