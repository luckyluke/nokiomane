#!/usr/bin/env python
# coding= utf-8

#from optparse import OptionParser
import optparse
from core import NMcore

if __name__=='__main__':
    parser = optparse.OptionParser(version="0.1")
    parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False, help="Modalita' debug")
    parser.add_option("-c", "--connessione", dest="conn", choices=["usb"], default=None, help="Modalita' fisica di connessione al telefono")
    parser.add_option("-p", "--protocollo", dest="proto", choices=["fbus"], default=None, help="Protocollo di connessione al telefono")
    parser.add_option("-t", "--text", action="store_true", dest="text", default=False, help="Modalita' testuale")
    (option, args) = parser.parse_args()
    core = NMcore(option)
    core.run()
