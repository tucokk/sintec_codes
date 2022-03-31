import configparser as cpa

def generateIniFile():
    config=cpa.ConfigParser()
    config.add_section('SQL_INFO')
    config.set('SQL_INFO', 'driver', 'SQL Server')
    config.set('SQL_INFO', 'server', 'DESKTOP-VOSNQS4')
    config.set('SQL_INFO', 'database', 'bancoteste')
    config.set('SQL_INFO', 'trust_connection', 'yes')
    config.set('SQL_INFO', 'uid', '')
    config.set('SQL_INFO', 'pws', '')

    with open(r'C:/configfile/script_config.ini', 'w') as sqlinfo:
        config.write(sqlinfo)
        print('sql_config.ini successfuly generated.\nRun the program again.')
        exit()

    