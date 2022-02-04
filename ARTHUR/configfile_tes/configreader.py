
config = dict({'gameId': '000-1', 'gameIp': '192.168.0.1'})
charConfig = dict({'playerName': 'Player'})

def GameSettingsConfig():

    with open('config.txt', 'r') as file:
        lines = file.readlines()

        onlineMode = lines[22]
        if 'true' in onlineMode:
            onlineMode = 'True'
        elif 'false' in onlineMode:
            onlineMode = 'False'
        config['onlineMode'] = onlineMode

        gameId = lines[23]
        if 'standardId' in gameId:
            pass
        elif 'standardId' not in gameId:
            characters = 'game-id=; \n'
            for x in range(len(characters)):
                gameId = gameId.replace(characters[x],'')
            config.update({'gameId': gameId})

        gameIp = lines[24]
        if 'standardIp' in gameIp:
            pass
        elif 'standardIp' not in gameIp:
            characters = 'game-ip=; \n'
            for x in range(len(characters)):
                gameIp = gameIp.replace(characters[x],'')
            config.update({'gameIp': gameIp})

        levelSeed = lines[25]
        if 'null' in levelSeed:
            pass
        elif 'null' not in levelSeed:
            characters = 'level-seed=; \n'
            for x in range(len(characters)):
                levelSeed = levelSeed.replace(characters[x],'')
            config['levelSeed'] = levelSeed

def CharSettingsConfig():
    
    with open('config.txt', 'r') as file:
        lines = file.readlines()

        playerName = lines[2]
        if 'null' in playerName:
            pass
        if 'null' not in playerName:
            playerName = playerName.replace('player-name = ', '')
            playerName = playerName.replace('; \n', '').title()
            if playerName == '':
                print('Something went wrong. > "player-name" cannot be empty. > Empty must be "null"')
                exit()
            charConfig.update({'playerName': playerName})
        
        playerAge = lines[5]
        if 'null' in playerAge:
            print('Something went wrong. > "player-age" cannot be empty.')
            exit()
        if 'null' not in playerAge:
            playerAge = playerAge.replace('player-age = ', '')
            playerAge = playerAge.replace(';\n', '')
            if playerAge == '':
                print('Something went wrong. > "player-age" cannot be empty. > Empty must be "null"')
                exit()
            charConfig['playerAge'] = playerAge
        
        playerBackground = lines[8]
        if 'null' in playerBackground:
            print('Something went wrong. > "player-background" cannot be empty.')
            exit()
        if 'null' not in playerBackground:
            playerBackground = playerBackground.replace('player-background = ', '')
            playerBackground = playerBackground.replace(';\n', '')
            if playerBackground == '':
                print('Something went wrong. > "player-background" cannot be empty. > Empty must be "null"')
                exit()
            charConfig['playerBackground'] = playerBackground

        playerStrength = lines[11]
        if 'null' in playerStrength:
            print('Something went wrong. > "player-strength" cannot be empty.')
            exit()
        if 'null' not in playerStrength:
            playerStrength = playerStrength.replace('player-strength = ', '')
            try:
                playerStrength = int(playerStrength.replace('; \n', ''))
                if playerStrength not in range(1, 11):
                    print('Something went wrong. > "player-strength" must be between 1 - 10.')
                    exit()
            except ValueError:
                print('Something went wrong. > "player-strength" cannot be empty. > Empty must be "null"')
                exit()
            charConfig['playerStrength'] = playerStrength

        playerIntelligence = lines[14]
        if 'null' in playerIntelligence:
            print('Something went wrong. > "player-intelligence" cannot be empty.')
            exit()
        if 'null' not in playerIntelligence:
            playerIntelligence = playerIntelligence.replace('player-intelligence = ', '')
            try:
                playerIntelligence = int(playerIntelligence.replace('; \n', ''))
                if playerIntelligence not in range(1, 11):
                    print('Something went wrong. > "player-intelligence" must be between 1 - 10.')
                    exit()
            except ValueError:
                print('Something went wrong. > "player-intelligence" cannot be empty. > Empty must be "null"')
                exit()
            charConfig['playerIntelligence'] = playerIntelligence

        playerMagic = lines[17]
        if 'null' in playerMagic:
            print('Something went wrong. > "player-magic" cannot be empty.')
            exit()
        if 'null' not in playerMagic:
            playerMagic = playerMagic.replace('player-magic = ', '')
            try:
                playerMagic = int(playerMagic.replace('; \n', ''))
                if playerMagic not in range(1, 11):
                    print('Something went wrong. > "player-magic" must be between 1 - 10.')
                    exit()
            except ValueError:
                print('Something went wrong. > "player-magic" cannot be empty. > Empty must be "null"')
                exit()
            charConfig['playerMagic'] = playerMagic


GameSettingsConfig()
CharSettingsConfig()

print(config)
print(charConfig)

        

    
    