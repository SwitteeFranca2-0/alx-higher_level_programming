#!/usr/bin/node

$('document').ready(function(){
    const url = 'https://www.fourtonfish.com/hellosalut/?'
    $('INPUT#btn_translate').click(function(){
        let code =  $('INPUT#language_code').val()
        $.get(url + $.param({lang: code}), function (data){
            $('DIV#hello').html(data.hello)
        })
    })
})
