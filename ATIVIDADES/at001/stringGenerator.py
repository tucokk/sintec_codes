import random
import string

with open('doc.txt', 'w') as file:
    numberStrings = 30
    lengthString = 20

    counter = 0
    

    for x in range(numberStrings):
        for y in range(1, 31):
            if counter == 30:
                break
            stringGenerator = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(lengthString)))
            if counter >= 1:
                file.write(f'\n{y}: {stringGenerator}') 
                continue
            file.write(f'{y}: {stringGenerator}')   
            counter = counter + 1
            

    print('ready')
    exit()


