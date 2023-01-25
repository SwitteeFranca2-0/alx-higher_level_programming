#!/usr/bin/node


$('document').ready(function(){
    const url = 'https://www.fourtonfish.com/hellosalut/?'
    $('INPUT#btn_translate').click(function(){
        let code =  $('INPUT#language_code').val()
        $.get(url + $.param({lang: code}), function (data){
            $('DIV#hello').html(data.hello)
        })
    })
    $('INPUT#btn_translate').focus(function() {
        $('INPUT#language_code').keypress(function(event){
            if (event.keyCode === 13) {
                let code =  $('INPUT#language_code').val()
                $.get(url + $.param({lang: code}), function (data){
                    $('DIV#hello').html(data.hello)
                })  
            }
        })

    })
})
