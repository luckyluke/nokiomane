class NMEvents:
    CONNECT = 0
    DISCONNECT = 1

# grazie ad amsn2
class NMEventManager:
    def __init__(self, core):
        self._core = core
        self.events = NMEvents()
        self._cbs = [[] for e in dir(self.events) if e.isupper()]

    def emit(self, event, *args):
        """ emit the event """
        for cb in self._cbs[event]:
            #TODO: try except
            cb(*args)

    # maybe create a default set of priority, like PLUGIN, CORE...
    def register(self, event, callback, type='ro', priority = 0):
        """ register a callback for an event """
        #TODO: try except
        if type is 'ro':
            self._cbs[event].append(callback)
        elif type is 'rw':
            # TODO: insertion depends on priority
            bck_cbs = [].extend(self._events_cbs)
            self._cbs[event] = [callback]
            self._cbs[event].extend(bck_cbs)

    def unregister(self, event, callback):
        """ unregister a callback for an event """
        #TODO: try except
        self._cbs[event].remove(callback)

