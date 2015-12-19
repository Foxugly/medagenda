{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{% load staticfiles %}
{% block js %}
<script>
$(document).ready(function() {
    $("#id_picture").fileinput({
        overwriteInitial: true,
        showCaption: false,
        initialPreviewShowDelete: false,
        showUpload: false,
        maxFileSize: 1500,
        defaultPreviewContent: '<img src="/media/pic/profil.jpg" alt="Your Avatar" style="width:160px">',
        layoutTemplates: {main2: '{preview} {remove} {browse}'},
        {% if avatar %}
        initialPreview: ["<img src='{{ MEDIA_URL }}{{avatar}}' class='file-preview-image' alt='alt' title='title.jpg'>"],
        initialPreviewConfig: [
        {
            caption: '{{avatar|filename}}',
            width: '120px'
        }],
        {% endif %}
        allowedFileExtensions: ["jpg", "png", "gif"]
    });

    $('#btn_personal_data').click(function(){
        var form = $('#form_personal_data');
        var url = '/user/ajax/personal_data/';
        $.ajax({
            url: url,
            type: 'POST',
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
            type: 'POST',
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

    $('#btn_avatar').click(function(){
        var input = $('#form_avatar').find('input#id_picture');
        var formdata = new FormData();
        var file = input[0].files[0];
        /*console.log(input[0].id);*/
        formdata.append(input[0].id, file);
        var url = '/user/ajax/avatar/';
        $.ajax({
            url: url,
            type: 'POST',
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
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
                type: 'POST',
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
            type: 'POST',
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
        <li class="active"><a data-toggle="tab" href="#div_personal_data">{% trans "Personal Data" %}</a></li>
        <li><a data-toggle="tab" href="#div_config">{% trans "Settings" %}</a></li>
        <li><a data-toggle="tab" href="#div_avatar">{% trans "Avatar" %}</a></li>
        <li><a data-toggle="tab" href="#div_color">{% trans "Colors" %}</a></li>
        <li><a data-toggle="tab" href="#div_text">{% trans "Text" %}</a></li>
        <li><a data-toggle="tab" href="#div_operations">{% trans "Operations" %}</a></li>
    </ul>

    <div class="tab-content">
        <div id="div_personal_data" class="tab-pane in active">
             <div class="row row_space">
                <form class="form-horizontal" id="form_personal_data" >
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form personal_data_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_personal_data" class="btn btn-primary"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div>
        </div>

        <div id="div_config" class="tab-pane">
            <div class="row row_space">
                <form class="form-horizontal" id="form_config">
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form settings_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_config" class="btn btn-primary"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div>
        </div>

        <div id="div_avatar" class="tab-pane">
            <div class="row row_space">
                <form class="form-horizontal" id="form_avatar" enctype="multipart/form-data">
                    {% csrf_token %}
                    <fieldset>
                         <div class="row" style="margin-bottom: 15px;">
                             <div class="form_group">
                                 <label class="col-md-3 control-label" for="id_picture">{% trans "Picture" %}</label>
                                 <div class="col-md-9">
                                      <input id="id_picture" name="id_picture" type="file">
                                 </div>
                             </div>
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_avatar" class="btn btn-primary"> Submit</a>
                                </div>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>

        <div id="div_color" class="tab-pane">
            <div class="row row_space">
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
                        <div class="row row_space">
                            <form class="form-horizontal" id="form_color_{{cform|index:'id'}}">
                                {% csrf_token %}
                                <fieldset>
                                    <div class="row">
                                        {% bootstrap_form cform|index:'form' layout="horizontal"%}
                                    </div>
                                    <div class="row">
                                        <div class="form_group">
                                            <div class="col-md-9 col-md-offset-3">

                                                <a href="#" id="btn_color_{{cform|index:'id'}}" class="btn btn-primary"> Submit</a>

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

        <div id="div_text" class="tab-pane">
            <div class="row row_space">
                <form class="form-horizontal" id="form_text">
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form text_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_text" class="btn btn-primary"> Submit</a>
                                </div>
                            </div>
                        </div>  
                    </fieldset>
                </form>
            </div> 
        </div>
        <div id="div_operations" class="tab-pane">
            <div class="row row_space">
            </div>
        </div>
    </div>
</div>
{% endblock %}