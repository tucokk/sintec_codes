import configparser as cpa

def generateIniFile():
    config=cpa.ConfigParser()
    config.add_section('SQL_INFO')
    config.set('SQL_INFO', 'driver', 'SQL Server')
    config.set('SQL_INFO', 'server', 'servidor_dados')
    config.set('SQL_INFO', 'database', 'bkp_centro_europeu')
    config.set('SQL_INFO', 'trust_connection', 'yes')
    config.set('SQL_INFO', 'uid', 'sa')
    config.set('SQL_INFO', 'pws', 'Mts56')

    with open('C:/Users/arthu/Desktop/testescript/script_config.ini', 'w') as sqlinfo:
        config.write(sqlinfo)
        print('sql_config.ini successfuly generated.\nRun the program again.')
        exit()

    