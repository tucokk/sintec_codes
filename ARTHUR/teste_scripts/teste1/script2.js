
document.getElementById('button1').addEventListener('click', tema)
x = 0

function tema() {

    if (x == 1) {
        x = 0
        document.body.style.backgroundColor = 'white'
        document.getElementById('texto').innerHTML = 'Light Mode 🌣'
        document.body.style.color = 'black'
        document.getElementById('div2').style.backgroundColor = 'black'

    } else {
        x = 1
        document.body.style.transitionDuration = '0.7s';
        document.body.style.backgroundColor = 'rgb(22, 22, 22)'
        document.getElementById('texto').innerHTML = 'Dark Mode ☽'
        document.body.style.color = 'white'
        document.getElementById('div2').style.transitionDuration = '0.7s'
        document.getElementById('div2').style.backgroundColor = 'white'
    }
}