import pypyodbc as odbc
import time
import configparser as cpa

# setting the config.ini data as the connection fields (server, database, login, password)
class Connection:
    def __init__(self, SERVER_NAME, DATABASE_NAME, UID, PSW):
        self.server = SERVER_NAME
        self.database = DATABASE_NAME
        self.uid = UID
        self.psw = PSW
        self.connection_string =f'''
    DRIVER={{SQL Server}};
    SERVER={self.server}
    DATABASE={self.database}
    Trust_Connection=yes;
    uid={self.uid}
    pws={self.psw}
                    '''
        print(f'Connection data informed.\n {self.connection_string}')

    #starting the connection process. limit of 3x is setted 
    def connection_database(self):
        for cont in range(1, 5): 
            print(f'Trying connection... [{cont}]')
            try:
                #connection line
                connection_server = odbc.connect(self.connection_string)
                status = 'connected'
                print(f'Connection complete successfuly. \nStatus: {status}\n Sys_status: {connection_server}')  
                return status
            #any error during the connection fill fall over here, giving the reconnect option
            except:
                if cont != 3:
                    try_again = input('Something went wrong. Try again? y/n\n')
                    if try_again == 'y':
                        print('\n')
                        continue
                    else:
                        exit()
                elif cont == 3:
                    print('Connection unsuccessful 3 times. Closing the program.')  
                    time.sleep(2)
                    exit()

#reading .ini file
config = cpa.ConfigParser()
config.read('sql_config.ini')

SERVER_NAME = config['SQL_INFO']['server']
DATABASE_NAME = config['SQL_INFO']['database']
UID = config['SQL_INFO']['uid']
PSW = config['SQL_INFO']['pws']

#calling the start of connecting process
connection = Connection(SERVER_NAME, DATABASE_NAME, UID, PSW)
connection_data = connection.connection_database()




