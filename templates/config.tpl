{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{%block css %}
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
<link href='/static/bootstrap-datepicker-master/dist/css/datepicker3.css' rel='stylesheet' />
<link href='/static/bootstrap-colorpicker-master/dist/css/bootstrap-colorpicker.min.css' rel='stylesheet' />
<link href='/static/css/perso.css' rel='stylesheet' />
{% endblock %}

{% block js %}
<script type="text/javascript" src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
<script src='/static/bootstrap-datepicker-master/dist/js/bootstrap-datepicker.min.js'></script>
<script src='/static/bootstrap-colorpicker-master/dist/js/bootstrap-colorpicker.min.js'></script>
<!--<script type="text/javascript" src="http://maps.googleapis.com/maps/api/js?libraries=places&amp;sensor=false"></script>
<script type="text/javascript" src="/static/js/jquery.geocomplete.min.js"></script>
<script type="text/javascript" src="/static/address/js/address.js"></script>-->
<script>

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
    $(".clockpicker").parent().clockpicker({
        autoclose: true
    });

    $('.datepicker').datepicker({
        autoclose: true
        //orientation: "bottom left"
    });

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
    }).on('changeColor', function(ev) {
        $(this).css({'background-color' : $(this).val()});
    });

    $('.colorpicker').focusout(function(){
        $(this).css({'background-color' : $(this).val()});
    });

    $('.colorpicker').each(function(){
        $(this).css({'background-color': $(this).val()});
    });


    $('#btn_personal_data').click(function(){
        var form = $('#form_personal_data');
        var url = '/user/ajax/personal_data/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });
    $('#btn_config').click(function(){
        var form = $('#form_config');
        var url = '/user/ajax/config/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });



{% for cform in color_forms %}
    $('#btn_color_{{cform|index:"id"}}').click(function(){
        var form = $('#form_color_{{cform|index:"id"}}');
        var url = '/user/ajax/color/{{cform|index:"id"}}/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });
{% endfor %}


    $('#btn_text').click(function(){
        var form = $('#form_text');
        var url = '/user/ajax/text/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });
});
</script>
{% endblock %}

{% block content %}

<div class="container">
    <h2>{% trans "Configuration and Settings" %}</h2>
    <ul class="nav nav-tabs">
        <li class="active"><a data-toggle="tab" href="#personal_data">{% trans "Personnal Data" %}</a></li>
        <li><a data-toggle="tab" href="#config">{% trans "Settings" %}</a></li>
        <li><a data-toggle="tab" href="#color">{% trans "Colors" %}</a></li>
        <li><a data-toggle="tab" href="#text">{% trans "Text" %}</a></li>
        <li><a data-toggle="tab" href="#operations">{% trans "Operations" %}</a></li>
    </ul>

    <div class="tab-content">
        <div id="personal_data" class="tab-pane in active">
             <div class="row" style="padding: 20px 0px 20px 0px;">
                <form class="form-horizontal" id="form_personal_data" >
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form personal_data_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_personal_data" class="btn btn-primary" layout="horizontal"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div>
        </div>

        <div id="config" class="tab-pane">
            <div class="row" style="padding: 20px 0px 20px 0px;">
                <form class="form-horizontal" id="form_config">
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form settings_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_config" class="btn btn-primary" layout="horizontal"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div>
        </div>
        <div id="color" class="tab-pane">
            <p></p>
            <div class="row" style="padding: 20px 0px 20px 0px;">
                <ul class="nav nav-tabs">
                {% for cform in color_forms %}
                    {% if forloop.first %}
                        <li class="active"><a data-toggle="tab" href="#color_{{cform|index:'id'}}">{{ cform|index:'name' }}</a></li>
                    {% else %}
                        <li><a data-toggle="tab" href="#color_{{cform|index:'id'}}">{{ cform|index:'name' }}</a></li>
                    {% endif %}
                {% endfor %}
                </ul>
                <div class="tab-content">
                {% for cform in color_forms %}
                    {% if forloop.first %}
                    <div id="color_{{cform|index:'id'}}" class="tab-pane in active">
                    {% else %}
                    <div id="color_{{cform|index:'id'}}" class="tab-pane ">
                    {% endif %}
                        <div class="row" style="padding: 20px 0px 20px 0px;">
                            <form class="form-horizontal" id="form_color_{{cform|index:'id'}}">
                                {% csrf_token %}
                                <fieldset>
                                    <div class="row">
                                        {% bootstrap_form cform|index:'form' layout="horizontal"%}
                                    </div>
                                    <div class="row">
                                        <div class="form_group">
                                            <div class="col-md-9 col-md-offset-3">

                                                <a href="#" id="btn_color_{{cform|index:'id'}}" class="btn btn-primary" layout="horizontal"> Submit</a>

                                            </div>
                                        </div>
                                    </div>  
                                </fieldset>
                            </form>
                        </div>
                    </div>
                {% endfor %}
                </div> 
            </div>   
        </div>

        <div id="text" class="tab-pane">
            <div class="row" style="padding: 20px 0px 20px 0px;">
                <form class="form-horizontal" id="form_text">
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form text_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_text" class="btn btn-primary" layout="horizontal"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div> 
        </div>
        <div id="operations" class="tab-pane">
            <div class="row" style="padding: 20px 0px 20px 0px;">
            </div>
        </div>
    </div>
</div>
{% endblock %}


