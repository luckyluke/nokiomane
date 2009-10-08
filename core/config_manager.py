
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

class ConfigManager:
    def __init__(self, core):
        pass

    def updatePhoneDB(self):
        pass

    def getDBPhone(self, name):
        pass

    def getConfig(self, name):
        return configE65

    def getDefaultConfig(self):
        return configE65

