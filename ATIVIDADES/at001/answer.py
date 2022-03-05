with open('doc.txt', 'r') as file:
    file = file.readlines()

    key = file[0]
    print(key)

    chars = list()
    counter = 0
    for x in range(len(key)):
        if counter == 3:
            break
        chars.extend(key[x])
        counter = counter + 1

    for x in range(1, 401):
        chars = ''.join(chars)
        characters = f'{x}:'
        print(characters)
        if characters == chars:
            print('teste')
            
        


