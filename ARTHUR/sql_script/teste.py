import pypyodbc as odbc
import time
import sqlinfo_generator as generator
import sqlinfo_reader as reader
import os

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
        Connection.cursor = 'teste'
        print(f'Connection data informed.\n {self.connection_string}')

    #starting the connection process. limit of 3x is setted 
    def connection_database(self):
        for cont in range(1, 5): 
            print(f'Trying connection... [{cont}]')
            try:
                #connection line
                connection_server = 'tst'
                Connection.cursor = connection_server
                print(f'Connection complete successfuly.\nSys_status: {connection_server}')  
                return Connection.cursor
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

class Querry(Connection):
    def __init__(self):
        print(Connection.cursor)
#reading .ini file or creating it
file_exist = os.path.isfile('C:/Users/arthu/Desktop/testescript/script_config.ini')
if file_exist == True:
    pass
else:
    generator.generateIniFile()

#calling the start of connecting process
connection = Connection(reader.readIniFile()[0], reader.readIniFile()[1], reader.readIniFile()[2], reader.readIniFile()[3], )
connection_data = connection.connection_database()
querry = Querry()




