with open('doc.txt', 'r') as file:
    file = file.readlines()

    code = file[19]
    
    characters = '20: '
    for x in range(len(characters)):
        code = code.replace(characters[x], '')

    print(code)