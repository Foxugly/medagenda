/**
 * Created by renaud on 19/12/15.
 */

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


$(document).ready(function() {
    $('#confirm_yes_close').click(function(){
        $('#confirm_yes').hide();
    });

    $('#confirm_yes_ok').click(function(){
        $('#confirm_yes').hide();
    });

    $('#confirm_no_close').click(function(){
        $('#confirm_no').hide();
    });

    $('#confirm_no_ok').click(function(){
        $('#confirm_no').hide();
    });

    $('#language').change(function() {
        var select = $(this);
        var mydata = {lang:select.val()};
        var url = '/lang/';
        $.ajax({
            url: url,
            type: 'POST',
            data: mydata,
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    location.reload();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    $('#select_doctor').change(function() {
        var select = $(this);
        var mydata = {doc:select.val()};
        console.log(mydata);
        var url = '/doc/ajax/change/';
        $.ajax({
            url: url,
            type: 'POST',
            data: mydata,
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    location.reload();
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    $(".clockpicker").parent().clockpicker({
        autoclose: true
    });


    $('.datepicker').datepicker({
        autoclose: true,
        language: "{{ LANGUAGE_CODE }}"
    });

    $('.select2').select2();

    $('.select2-nosearch').select2({minimumResultsForSearch: -1});

    $('.colorpicker').colorpicker({
        format: 'hex',
        customClass: 'colorpicker-2x',
        sliders: {
            saturation: {
                maxLeft: 200,
                maxTop: 200
            },
            hue: {
                maxTop: 200
            },
            alpha: {
                maxTop: 200
            }
        }
    }).on('changeColor', function() {
        $(this).css({'background-color' : $(this).val()});
    }).focusout(function(){
        $(this).css({'background-color' : $(this).val()});
    }).each(function(){
        $(this).css({'background-color': $(this).val()});
    });
});
