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
        initialPreviewConfig: [{
            caption: '{{avatar|filename}}',
            width: '120px'
        }],
        {% endif %}
        allowedFileExtensions: ["jpg", "png", "gif"]
    });

    $('#btn_personal_data').click(function(){
        var form = $('#form_personal_data');
        var url = '/doc/ajax/personal_data/';
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
        var url = '/doc/ajax/config/';
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
        var url = '/doc/ajax/avatar/';
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
            var url = '/doc/ajax/color/{{cform|index:"id"}}/';
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
        var url = '/doc/ajax/text/';
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
        var url = '/doc/ajax/invoice/add/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form,
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    var tr = "<tr><td>" + result['id'] + "</td><td>" + result['type_price'] + "</td>";
                    tr += "<td class='text-center'>" + result['date_start'] + "</td><td class='text-center'>" +  result['date_end'] + "</td><td></td>";
                    tr += "<td class='text-center'><a href='#' class='btn btn-xs btn-danger invoice_del' role='button'>" ;
                    tr += "<span class='glyphicon glyphicon-remove'></span></a></td>";
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

    $('#btn_add_collaborators').click(function(){
        var form = $('#form_collaborator');
        var url = '/doc/ajax/collaborator/add/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    var tr = "<tr><td class='text-center'>" + result['id'] + "</td>";
                    if (result['type'] == 1){
                        tr += "<td class='text-center'>" + result['firstname'] + "</td>";
                        tr += "<td class='text-center'>" +  result['lastname'] + "</td>";
                        tr += "<td class='text-center'>" +  result['email'] + "</td>";
                        tr += "<td class='text-center'><a href='#' class='btn btn-xs btn-danger collaborator_del' role='button'>" ;
                        tr += "<span class='glyphicon glyphicon-remove'></span></a></td>";
                        $('#table_permission').append(tr);
                    }
                    else if (result['type'] == 2){
                        tr += "<td class='text-center'></td><td class='text-center'></td>";
                        tr += "<td class='text-center'>" +  result['email'] + "</td>";
                        tr += "<td class='text-center'><a href='#' class='btn btn-xs btn-danger collaborator2_del' role='button'>" ;
                        tr += "<span class='glyphicon glyphicon-remove'></span></a></td>";
                        $('#table_permission').append(tr);
                    }
                    $('#id_email_col').val('');
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    $("table").on("click", ".invoice_del", function() {
        var killrow = $(this).closest("tr");
        var myid = killrow.find("td:first").html();
        var url = '/doc/ajax/invoice/remove/' + myid + '/';
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

    $("table").on("click", ".collaborator_del", function() {
        var killrow = $(this).closest("tr");
        var myid = killrow.find("td:first").html();
        var url = '/doc/ajax/collaborator/remove/' + myid + '/';
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
    $("table").on("click", ".collaborator2_del", function() {
        var killrow = $(this).closest("tr");
        var myid = killrow.find("td:first").html();
        var url = '/doc/ajax/collaborator/remove2/' + myid + '/';
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
        <li><a data-toggle="tab" href="#div_permissions">{% trans "Permissions" %}</a></li>
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
                                    <th class="text-center">{%  trans "ID" %}</th>
                                    <th class="text-center">{%  trans "Type" %}</th>
                                    <th class="text-center">{%  trans "Start Date" %}</th>
                                    <th class="text-center">{%  trans "End Date" %}</th>
                                    <th class="text-center">{%  trans "Invoice" %}</th>
                                    <th class="text-center">{%  trans "Remove" %}</th>
                                </tr>
                                </thead>
                                <tbody>
                            {% for i in user.userprofile.current_doctor.invoices.all %}
                                {% if i.active %}<tr class="success">{% else %}<tr>{%  endif  %}
                                <td>{{ i.id }}</td>
                                <td>{{ i.type_price }}</td>
                                <td  class="text-center">{{ i.date_start | date_format}}</td>
                                <td  class="text-center">{{ i.date_end | date_format}}</td>
                                <td  class="text-center">
                                {%  if i.path %}
                                    <a href="{{ MEDIA_URL }}{{ i.path }}">pdf</a>
                                {%  endif %}
                                </td>
                                {% if not i.active or i.date_begin|after_today %}
                                    <td class='text-center'>
                                        <a href='#' class='btn btn-xs btn-danger invoice_del' role='button'>
                                            <span class='glyphicon glyphicon-remove'></span>
                                        </a>
                                    </td>
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

        <div id="div_permissions" class="tab-pane">
            <div class="row row_space_top">
                <div class="col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">{%  trans "List of collaborators" %}</div>
                        <div class="panel-body">
                            <table id="table_permission" class="table table-bordered">
                                <thead>
                                <tr>
                                    <th class="text-center">{%  trans "ID" %}</th>
                                    <th class="text-center">{%  trans "first name" %}</th>
                                    <th class="text-center">{%  trans "last name" %}</th>
                                    <th class="text-center">{%  trans "Email address" %}</th>
                                    <th class="text-center"></th>
                                </tr>
                                </thead>
                                <tbody>
                                {%  for c in collaborators1 %}
                                    <tr>
                                    <td class="text-center">{{ c.id }}</td>
                                    <td class="text-center">{{ c.user.first_name }}</td>
                                    <td class="text-center">{{ c.user.last_name }}</td>
                                    <td class="text-center">{{ c.user.email }}</td>
                                    <td class="text-center"><a href='#' class='btn btn-xs btn-danger collaborator_del' role='button'><span class='glyphicon glyphicon-remove'></span></a></td>
                                    </tr>
                                {%  endfor  %}
                                {%  for c in collaborators2 %}
                                    <tr>
                                    <td class="text-center">{{ c.id }}</td>
                                    <td class="text-center"></td>
                                    <td class="text-center"></td>
                                    <td class="text-center">{{ c.email_col }}</td>
                                    <td class="text-center"><a href='#' class='btn btn-xs btn-danger collaborator2_del' role='button'><span class='glyphicon glyphicon-remove'></span></a></td>
                                    </tr>
                                {%  endfor  %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row row_space_top">
                <div class="col-xs-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">{%  trans "Add collaborators" %}</div>
                        <div class="panel-body">
                            <form class="form-horizontal" id="form_collaborator">
                                {% csrf_token %}
                                {% bootstrap_form collaborator_form layout="horizontal" %}
                                <div class="form_group">
                                    <div class="col-xs-9 col-xs-offset-3" style="margin-top: 10px;">
                                        <a href="#" id="btn_add_collaborators" class="btn btn-primary">Add</a>
                                    </div>
                                 </div>
                            </form>
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