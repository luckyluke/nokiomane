#!/usr/bin/env python
# coding= utf-8

import optparse
from core import NMcore

if __name__=='__main__':
    parser = optparse.OptionParser(version="0.1")
    parser.add_option("-d", "--debug", action="store_true", dest="debug",
                      default=False, help="Modalita' debug")

    parser.add_option("-t", "--text", action="store_true", dest="text",
                      default=False, help="Modalita' testuale")

    parser.add_option("-c", "--config", dest="config",
                      default=None, help="Modello del telefono da collegare")

    parser.add_option("-a", "--azione", dest="action", choices=["NMGetInfo", "NMReadAddressBook"],
                      default=None, help="GammuAction da eseguire")

    parser.add_option("-p", "--parametri", dest="params", choices=["fbus"],
                      default=None, help="Parametri della GammeAcion")

    (option, args) = parser.parse_args()

    core = NMcore(option)
    core.run()

