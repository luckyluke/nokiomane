#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Luca Dariz <luca.dariz@gmail.com>
#                    Luigi Scagnet <skagngh@msn.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import optparse
from core import NMcore

__version__ = "0.1"
__author__ = "Luca Dariz <luca.dariz@gmail.com>"
__url__ = "http://github.com/luckyluke/nokiomane/tree/master"
__license__ = "GNU GPL"

if __name__=='__main__':
    parser = optparse.OptionParser(version=__version__)
    parser.add_option("-d", "--debug", action="store_true", dest="debug",
                      default=False, help="Modalita' debug")

    parser.add_option("-t", "--text", action="store_true", dest="text",
                      default=False, help="Modalita' testuale")

    parser.add_option("-c", "--config", dest="config",
                      default=None, help="Modello del telefono da collegare")

    parser.add_option("-a", "--azione", dest="action", choices=["GetInfo", "ReadAddressBook"],
                      default=None, help="GammuAction da eseguire")

    parser.add_option("-p", "--parametri", dest="params", choices=["fbus"],
                      default=None, help="Parametri della GammeAcion")

    (option, args) = parser.parse_args()

    core = NMcore(option)
    core.run()

