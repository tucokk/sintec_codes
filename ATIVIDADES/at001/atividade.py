with open('doc.txt', 'r') as file:
    file = file.readlines()

    key = file[19]
    
    characters = '20: '
    for x in range(len(characters)):
        key = key.replace(characters[x], '')

    print(f'\n\n{key}\n\n')

