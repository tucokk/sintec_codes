import configparser as cpa

def readIniFile():
    config = cpa.ConfigParser()
    config.read(r'C:/configfile/script_config.ini')
    SERVER_NAME = config['SQL_INFO']['server']
    DATABASE_NAME = config['SQL_INFO']['database']
    UID = config['SQL_INFO']['uid']
    PSW = config['SQL_INFO']['pws']
    DRIVER = config['SQL_INFO']['driver']

    return (SERVER_NAME, DATABASE_NAME, UID, PSW, DRIVER)
