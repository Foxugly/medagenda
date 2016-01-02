{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load l10n %}
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

    $('#btn_new_invoice').click(function(){
        var form = $('#form_invoice').serializeArray();
        var url = '/user/ajax/invoice/add/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form,
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#confirm_yes').show();
                    var tr = "<tr><td>" + result['id'] + "</td><td>" + result['type_price'] + "</td>";
                    tr += "<td>" + result['date_start'] + "</td><td>" +  result['date_end'] + "</td>";
                    tr += "<td class='text-center'><div class='glyphicon glyphicon-remove ibtnDel'></div></td>";
                    $('#table_invoice').append(tr);
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });


    $('#btn_password').click(function(){
        var form = $('#form_password');
        var url = '/user/ajax/password/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#id_old_password').val('');
                    $('#id_new_password1').val('');
                    $('#id_new_password2').val('');
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    /*$(".btn_del").click(function () {
        var killrow = $(this).parent('tr');
        var myid = killrow.find("td:first").html();
        var url = '/user/ajax/invoice/remove/' + myid + '/';
        $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    killrow.fadeOut(100, function(){
                        $(this).remove();
                    });
                }
            }
        });
    });*/

     $("table").on("click", ".ibtnDel", function (event) {
         var killrow = $(this).closest("tr");
         console.log(killrow);
         var myid = killrow.find("td:first").html();
         console.log(myid);
         var url = '/user/ajax/invoice/remove/' + myid + '/';
         console.log(url);
         $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    killrow.remove();
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
        <li><a data-toggle="tab" href="#div_account">{% trans "Account" %}</a></li>
        <li><a data-toggle="tab" href="#div_password">{% trans "Password" %}</a></li>
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
        <div id="div_account" class="tab-pane">
            <div class="row row_space_top">
                <div class="col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">{%  trans "Current account" %}</div>
                        <div class="panel-body">
                            <p>{% trans "Type" %} : {{ invoice.type_price }}</p>
                            <p>{% trans "Start date" %} : {{ invoice.date_start }}</p>
                            <p>{% trans "End date" %} : {{ invoice.date_end }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">{%  trans "Change account" %}</div>
                        <div class="panel-body">
                            <form class="form-horizontal" id="form_invoice">
                                {% csrf_token %}
                                {% bootstrap_form new_invoice layout="horizontal" %}
                                <div class="form_group">
                                    <div class="col-xs-9 col-xs-offset-3" style="margin-top: 10px;">
                                        <a href="#" id="btn_new_invoice" class="btn btn-primary"> Submit</a>
                                    </div>
                                 </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">{%  trans "History" %}</div>
                        <div class="panel-body">
                            <table id="table_invoice" class="table table-bordered">
                                <thead>
                                <tr>
                                    <th>ID</th><th>Type</th><th>Start Date</th><th>End Date</th><th>Remove</th>
                                </tr>
                                </thead>
                                <tbody>
                            {% for i in user.userprofile.invoices.all %}
                                {% if i.active %}<tr class="success">{% else %}<tr>{%  endif  %}
                                <td>{{ i.id }}</td>
                                <td>{{ i.type_price }}</td>
                                <td>{{ i.date_start}}</td>
                                <td>{{ i.date_end}}</td>
                                {% if not i.active or i.date_begin|after_today %}
                                    <td class='text-center'><div class='glyphicon glyphicon-remove ibtnDel'></div></td>
                                {%  else %}
                                    <td></td>
                                {% endif %}
                                </tr>
                            {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div id="div_password" class="tab-pane">
            <div class="row row_space">
                <form class="form-horizontal" id="form_password">
                    {% csrf_token %}
                    <fieldset>
                        <div class="row">
                            {% bootstrap_form password_change_form layout="horizontal"%}
                        </div>
                        <div class="row">
                            <div class="form_group">
                                <div class="col-md-9 col-md-offset-3">
                                    <a href="#" id="btn_password" class="btn btn-primary"> Submit</a>
                                </div>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}