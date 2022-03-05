const screen = document.getElementById('screen')
const context = screen.getContext('2d')
const currentPlayerId = 'player1'


const state = {
        players: {
            'player1': {x: 1, y: 1, points: 0},
        },
        fruits: {
            'fruit1': {x: Math.floor(Math.random() * 10), y: Math.floor(Math.random() * 10)}
        }
    }

addEventListener('keydown', handleKeydown)

function handleKeydown(event) {
    const keyPressed = event.key 
    movePlayer(keyPressed)
}

function movePlayer(key) {
    const keyPressed = key
    const player = state.players[currentPlayerId]

    if (keyPressed === 'ArrowUp' && player.y - 1 >=0) {
        player.y = player.y - 1
        eatingFruit()
    } 
    if (keyPressed === 'ArrowDown' && player.y + 1 < screen.height) {
        player.y = player.y + 1
        eatingFruit()
    } 
    if (keyPressed === 'ArrowRight' && player.x + 1 < screen.width) {
        player.x = player.x + 1
        eatingFruit()
    } 
    if (keyPressed === 'ArrowLeft' && player.x - 1 >=0) {
        player.x = player.x - 1
        eatingFruit()
    } 
}

function eatingFruit() {

    const fruit = state.fruits['fruit1']
    const player = state.players[currentPlayerId]

    if (player.x === fruit.x && player.y === fruit.y) {
        state.fruits['fruit1'] = {x: Math.floor(Math.random() * 10), y: Math.floor(Math.random() * 10)}
        return(player.points = player.points + 1)
    }
}

renderScreen()

function renderScreen(fruitEated) {
    context.fillStyle = 'white'
    context.clearRect(0, 0, 10, 10)

    for (const playerId in state.players) {
        const player = state.players[playerId]
        context.fillStyle = 'black'
        context.fillRect(player.x, player.y, 1, 1)
    }

    for (const fruitId in state.fruits) {
        const fruit = state.fruits[fruitId]
        context.fillStyle = 'green'
        context.fillRect(fruit.x, fruit.y, 1, 1)
    }
    
    const playerPoints = document.getElementById('playerPoints')
    playerPoints.innerHTML = state.players[currentPlayerId].points

    const playerSeconds = document.getElementById('playerSeconds')
    const now = new Date()
    playerSeconds.innerHTML = now.getSeconds()

    requestAnimationFrame(renderScreen)

}