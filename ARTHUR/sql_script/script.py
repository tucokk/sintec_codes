import pypyodbc as odbc
import time
import sqlinfo_generator as generator
import sqlinfo_reader as reader
import os

# setting the config.ini data as the connection fields (server, database, login, password)
class Connection:
    def __init__(self, DRIVER, SERVER_NAME, DATABASE_NAME, UID, PSW):
        self.server = SERVER_NAME
        self.database = DATABASE_NAME
        self.uid = UID
        self.psw = PSW
        self.driver = DRIVER
        self.connection_string =f'''
    DRIVER={{{self.driver}}};
    SERVER={self.server};
    DATABASE={self.database};
    Trust_Connection=yes;
    uid={self.uid};
    pws={self.psw};
                    '''
        Connection.cursor = 'none'
        print(f'Connection data informed.\n {self.connection_string}')

    #starting the connection process. limit of 3x is setted 
    def connection_database(self):
        for cont in range(1, 6): 
            msg = f'[{cont}]'
            print('Trying connection... {}'.format(msg if cont > 1 else ''))
            try:
                #connection line
                connection_server = odbc.connect(self.connection_string)
                Connection.cursor = connection_server
                print(f'Connection complete successfuly.\nSys_status: {connection_server}')  
                return Connection.cursor
            #any error during the connection fill fall over here, giving the reconnect option
            except:
                if cont != 5:
                    try_again = input('Something went wrong. Try again? y/n\n')
                    if try_again == 'y':
                        print('\n')
                        continue
                    else:
                        exit()
                elif cont == 5:
                    print('Connection unsuccessful 5 times. Closing the program.')  
                    time.sleep(2)
                    exit()

class Querry(Connection):
    def __init__(self):
        self.cursor = Connection.cursor
    
    def querry(self):
        cursor = self.cursor
        cursor.execute('''
    SELECT
        *
    FROM
        aluno
        ''')
#reading .ini file or creating it
file_exist = os.path.isfile('C:/Users/arthu/Desktop/testescript/script_config.ini')
if file_exist == True:
    pass
else:
    generator.generateIniFile()

#calling the start of connecting process
connection = Connection(reader.readIniFile()[4],reader.readIniFile()[0], reader.readIniFile()[1], reader.readIniFile()[2], reader.readIniFile()[3], )
connection_data = connection.connection_database()
querry = Querry()
executing_querry = querry.querry()



