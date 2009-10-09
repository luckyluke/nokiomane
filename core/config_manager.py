
import os
import logging

"""ElementTree independent from the available distribution"""
try:
    from xml.etree.cElementTree import *
except ImportError:
    try:
        from cElementTree import *
    except ImportError:
        from elementtree.ElementTree import *

log = logging.getLogger('config-manager')

class ConfigManager:
    def __init__(self, core):
        if os.name == "posix":
            self.config_dir = os.path.join(os.environ['HOME'], ".nokiomane")
        elif os.name == "nt":
            self.config_dir = os.path.join(os.environ['USERPROFILE'], "nokiomane")
        else:
            self.config_dir = os.path.join(os.curdir, "nokiomane_config")

        try :
            os.makedirs(self.config_dir, 0700)
            # First time, fill with sample config
            self.phones_config = XmlFileDict('PhonesConfig',
                                          os.path.join(self.config_dir, 'phones.xml'),
                                          sample_phones_config)
        except OSError:
            self.phones_config = XmlFileDict('PhonesConfig',
                                          os.path.join(self.config_dir, 'phones.xml'))

        self.phones_config.default = 'E65'

    def updatePhoneDB(self):
        pass

    def getDBPhone(self, name):
        pass

    def getConfig(self, name):
        if name in self.phones_config:
            return self.phones_config[name]
        else:
            return None

    def getDefaultConfig(self):
        if 'default' in self.phones_config:
            return self.phones_config[self.phones_config.default]
        else:
            return None

class XmlFileDict(dict):
    def __init__(self, name, path=None, template=None):
        dict.__init__(self)

        self.__path = path
        self.__name = name

        if template:
            for key in template.keys():
                if type(template[key]) is dict:
                    value = XmlFileDict(key, self.__path, template[key])
                else:
                    value = template[key]
                self[key] = value
            self.write()

        else:
            if self.__path:
                self.read()

    def to_xml_element(self):
        root = Element(self.__name)
        for key in self.keys():
            value = self[key]
            if isinstance(value, XmlFileDict):
                value = value.to_xml_element()
                root.append(value)
            else:
                e = SubElement(root, key)
                if type(value) == type(0):
                    e.set('type', str(type(value)).split("'")[1])
                    e.text = str(value)
                elif type(value) == type(''):
                    e.set('type', str(type(value)).split("'")[1])
                    e.text = value
                elif type(value) == type(None):
                    e.set('type', str(type(value)).split("'")[1])
                    e.text = str(value)
                else:
                    log.error('Non posso serializzare oggetto di tipo %s' %type(value))

        return root

    def write(self):
        if self.__path:
            tree = ElementTree(self.to_xml_element())
            tree.write(self.__path, encoding='utf-8')

    def from_xml_element(self, element):
        for elm in element.getchildren():
            if len(elm) > 0:
                # has subelements
                x = XmlFileDict(elm.tag)
                x.from_xml_element(elm)
                self[elm.tag] = x
            else:
                if elm.get('type') == str(type(0)).split("'")[1]:
                    self[elm.tag] = int(elm.text)
                elif elm.get('type') == str(type('')).split("'")[1]:
                    self[elm.tag] = elm.text
                elif elm.get('type') == str(type(None)).split("'")[1]:
                    self[elm.tag] = None
                else:
                    log.error('Non posso leggere oggetto di tipo %s' %elm['type'])

    def read(self):
        if self.__path:
            elt = ElementTree(file=self.__path)
            self.from_xml_element(elt.getroot())

    def __getattr__(self, item):
        if item[0] == '_':
            return dict.__getattr__(self, item)
        else:
            return self.__getitem__(item)

    def __setattr__(self, item, value):
        if item[0] == '_':
            dict.__setattr__(self, item, value)
        else:
            self.__setitem__(item, value)

#config6230 = { 'port':'dev/ttyACM0'}
config6230 = {
            'StartInfo': 'yes',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'at115200',
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '/dev/ttyACM0',
            'Localize': None,  # Set automatically by python-gammu
            'Model': '6230',
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

config1200 = {
            'StartInfo': 'no',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'fbus',
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '/dev/ttyUSB0',
            'Localize': None,  # Set automatically by python-gammu
            'Model': 'auto',
            }

configN73 = {
            'StartInfo': 'no',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'at', #dku2phonet
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '/dev/ttyACM0',
            'Localize': None,  # Set automatically by python-gammu
            'Model': 'auto',
            }

configE65 = {
            'StartInfo': 'no',
            'UseGlobalDebugFile': 1,
            'DebugFile': None, # Set on other place
            'SyncTime': 'yes',
            'Connection': 'at115200', #dku2phonet
            'LockDevice': 'no',
            'DebugLevel': 'textalldate', # Set on other place
            'Device': '/dev/ttyACM0',
            'Localize': None,  # Set automatically by python-gammu
            'Model': 'auto',
            }

sample_phones_config = {
    'n6230':config6230,
    'E65':configE65,
    'n1200':config1200,
    'N73':configN73,
    'n5200':config5200
}

