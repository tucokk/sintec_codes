
$(document).ready(function() {
    
    $('#reloading_game').click(function() {
        location.reload()
    })
    $('#starting_game').click(function() {
        var player1Name = $('#player1').val()
        var player2Name = $('#player2').val()
        
        if (player1Name.length > 0 && player2Name.length > 0) {
            $('.msg').html('')
            document.querySelector('table').style.marginTop = '64px'
            StartGame()
        } else {
            $('.msg').html('Nome(s) preenchido(s) de forma inválida. Tente novamente.!')
        }
    })

    function StartGame() {
        var clickCounter = 0
        var gameStart = null
        var interval = setInterval(Time, 500)

        function Time() {
            
            if (gameStart == null) {
                gameStart = new Date()
            }
            var currentDate = new Date()
            var startSecond = gameStart.getSeconds()
            var currentSecond = currentDate.getSeconds()
            var gameTime = currentSecond-startSecond
            $('.time').text(gameTime+' segundo(s) decorridos!')
            document.querySelector('table').style.marginTop = '1px'
        }
        $('table td').click(function() {
            clickCounter++

            if (clickCounter <= 9) {

                if (clickCounter % 2 == 0 ) {
                    //par
                    if ($(this).text() == '') {
                        $(this).text('O')
                        VerifyWinner()
                    }
                } else {
                    //impar
                    if ($(this).text() == '') {
                        $(this).text('X')
                        VerifyWinner()
                    }
                }
                
                if (VerifyWinner() == true) {
                    clearInterval(interval)
                }
                if (clickCounter == 9) {
                    document.querySelector('table').style.marginTop = '15px'
                    $('.msg').html('Jogo encerrado!') 


                }
            }   
            
                function VerifyWinner() {

                    var winner = [

                        [0, 1, 2], //linhas
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6], //colunas
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8], //diagonais
                        [2, 4, 6]
                    ]
                    
                    var X = new Array(9)
                    var O = new Array(9)

                    $('table td').each(function(key, value) {
                        if ($(this).text() == 'X') {
                            X[key] = key
                        }
                        if ($(this).text() == 'O') {
                            O[key] = key
                        }
                    })
                    return WinnerDefiner(X, O, winner)
                    
                    
                    function WinnerDefiner(X, O, winner) {

                        //percorre as linhas
                        for (i = 0; i < winner.length; i++) {
                            counterX = 0;
                            counterO = 0;
    
                            //percorre as colunas de uma linha
                            for (var y = 0; y < winner[i].length; y++) {
                                if (X[winner[i][y]] == winner[i][y]) {
                                    counterX++
                                }
    
                                if (O[winner[i][y]] == winner[i][y]) {
                                    counterO++
                                }
                                
                                winner[i][y]
                            }
    
                            if (counterX == 3) {
                                var playerName = $('#player1').val()
                                document.querySelector('table').style.marginTop = '15px'
                                $('.msg').html('Jogo encerrado - '+ playerName + ' venceu!')
                                return true
                            }
    
                            if (counterO == 3) {
                                var playerName = $('#player2').val()
                                document.querySelector('table').style.marginTop = '15px'
                                $('.msg').html('Jogo encerrado - <br>'+ playerName + ' venceu!')                              
                                return true
                            }
                        }
                    }

                }
         })
    }
})