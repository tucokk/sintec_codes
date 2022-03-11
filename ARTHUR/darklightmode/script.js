$(document).ready(function() {
            
    var button = $('#slidebutton')
    var counter = 0

    button.click(function() {
        var button = document.getElementById('slide')
        

        if (counter == 0) {
            button.style.transform = 'translate(215%, -50%)'
            button.style.transitionDuration = '0.7s'
            counter++ 
            var theme = 'dark'
        } else if (counter == 1) {
            button.style.transform = 'translate(10%, -50%)'
            button.style.transitionDuration = '0.7s'
            counter--
            var theme = 'light'
        }

        // changing theme

        if (theme == 'dark') {
            var buttontheme = document.getElementById('div1')
            var buttontheme2 = document.getElementById('container')
            var text = document.getElementById('themetext')
            var text2 = document.getElementById('ptext')
            document.body.style.transitionDuration = '0.7s'
            text.innerHTML = 'Dark Mode ☽'
            text, text2.style.transitionDuration = '0.7s'
            text.style.color = 'white'
            text2.style.color = 'white'
            buttontheme2.style.color = 'white'
            buttontheme.style.transitionDuration = '0.7s'
            buttontheme.style.backgroundColor = 'white'
            document.body.style.backgroundColor = 'rgb(20, 23, 36)'
        }
        if (theme == 'light') {
            var buttontheme = document.getElementById('div1')
            var buttontheme2 = document.getElementById('container')
            var text = document.getElementById('themetext')
            var text2 = document.getElementById('ptext')
            document.body.style.transitionDuration = '0.7s'
            text.innerHTML = 'Light Mode 🌣'
            text.style.color = 'black'
            text2.style.color = 'black'
            buttontheme2.style.color = 'black'
            buttontheme.style.backgroundColor = 'black'
            document.body.style.backgroundColor = 'rgb(238, 236, 236)'
        }
    })
})