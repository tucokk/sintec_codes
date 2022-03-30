import pypyodbc as odbc
import time

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'servidor_dados'
DATABASE_NAME = 'bkp_centro_europeu'

#uid=sa;
#pws=Mts56;

connection_string = f'''
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid=sa;
    pws=Mts56;
'''

def checkConnectionData():
    print(connection_string)

def connection():
    for cont in range(1, 5): 
        print(f'Trying connection... [{cont}]')
        try:
            connection_server = odbc.connect(connection_string)
            status = 'connected'
            print(f'Connection complete successfuly. \nStatus: {status}\n Sys_status: {connection_server}')  
            return status
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

    
checkConnectionData()
connection()

