$(document).ready(function() {
    x = 0
    $('#button1').click(function() {
        if (x==1) {
            document.body.style.backgroundColor = 'white';
            $('#texto').html('Modo claro')
            document.body.style.color = 'black';
            x = 0
        } else {
            x = 1
            document.body.style.transitionDuration = '0.7s';
            document.body.style.backgroundColor = 'rgb(22, 22, 22)';
            $('#texto').html('Modo escuro')
            document.body.style.color = 'white';
        }
    })

})

