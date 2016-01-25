{% comment %}

# Copyright 2015, Foxugly All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <title>MedAgenda</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <!--  CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet"/>
    <link href='{% static "fullcalendar-2.5.0/fullcalendar.css" %}' rel='stylesheet' />
    <link href='{% static "fullcalendar-2.5.0/fullcalendar.print.css" %}' rel='stylesheet' media='print' />
    <link href='{% static "clockfield/bootstrap-clockpicker.min.css" %}' rel='stylesheet' />
    <link href='{% static "bootstrap-datepicker-master/dist/css/datepicker3.css" %}' rel='stylesheet' />
    <link href='{% static "bootstrap-colorpicker-master/dist/css/bootstrap-colorpicker.min.css" %}' rel='stylesheet' />
    <link href='{% static "bootstrap-fileinput-master/css/fileinput.min.css" %}' rel='stylesheet' />
    <link href='{% static "select2-4.0.1/dist/css/select2.min.css" %}' rel='stylesheet' />
    {% block css %}
    {% endblock %}
    {% get_current_language as LANGUAGE_CODE %}
    <link href='{% static "css/perso.css" %}' rel='stylesheet' />
    <link href='{% static "css/offer.css" %}' rel='stylesheet' />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript" src='{% static "fullcalendar-2.5.0/lib/moment.min.js" %}'></script>
    <script type="text/javascript" src='{% static "fullcalendar-2.5.0/lib/jquery.min.js" %}'></script>
    <script type="text/javascript" src='{% static "fullcalendar-2.5.0/fullcalendar.min.js" %}'></script>
    <script type="text/javascript" src='{% static "fullcalendar-2.5.0/lang-all.js" %}'></script>
    <script type="text/javascript" src='{% static "clockfield/bootstrap-clockpicker.min.js" %}'></script>
    <script type="text/javascript" src='{% static "bootstrap-datepicker-master/dist/js/bootstrap-datepicker.min.js" %}'></script>
    {% if LANGUAGE_CODE != 'en' %}
        {% with 'bootstrap-datepicker-master/dist/locales/bootstrap-datepicker.'|add:LANGUAGE_CODE|add:'.min.js' as datepicker_lang %}
        <script type="text/javascript" src='{% static datepicker_lang %}'></script>
        {% endwith %}
    {%  endif %}
    <script>
        $(document).ready(function() {
            $(".date_format").val($.fn.datepicker.dates["{{ LANGUAGE_CODE }}"]["format"]);
        });
    </script>
    <script type="text/javascript" src='{% static "bootstrap-colorpicker-master/dist/js/bootstrap-colorpicker.min.js" %}'></script>
    <script type="text/javascript" src='{% static "bootstrap-fileinput-master/js/fileinput.min.js" %}'></script>
    {% if LANGUAGE_CODE != 'en' %}
        {% with 'bootstrap-fileinput-master/js/fileinput_locale_'|add:LANGUAGE_CODE|add:'.js' as fileinput_lang %}
        <script type="text/javascript" src='{% static fileinput_lang %}'></script>
        {% endwith %}
    {%  endif  %}
    <script type="text/javascript" src='{% static "select2-4.0.1/dist/js/select2.min.js" %}'></script>
    {% if LANGUAGE_CODE != 'en' %}
        {% with 'select2-4.0.1/dist/js/i18n/'|add:LANGUAGE_CODE|add:'.js' as select2_lang %}
        <script type="text/javascript" src='{% static select2_lang %}'></script>
        {% endwith %}
     {%  endif %}
    <script type="text/javascript" src='http://maps.googleapis.com/maps/api/js?libraries=places'></script>
    <script type="text/javascript" src='{% static "js/jquery.geocomplete.min.js" %}'></script>
    <script type="text/javascript" src='{% static "address/js/address.js" %}'></script>
    {% block js %}
    {% endblock %}
    <script src='{% static "js/perso.js" %}'></script>
    {% block header %}
    {% endblock %}
  </head>
  <body>
    <nav class="navbar navbar-fixed-top navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">MedAgenda</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          {% if user.is_authenticated %}
              <ul class="nav navbar-nav navbar-left">
                  <li>
                    <div class='navbar-form form-group'>
                     <select id="select_doctor" name="select_doctor" class="form-control">
                         {%  for doc in user.userprofile.doctors.all %}
                             {%  if doc == user.userprofile.current_doctor %}
                                <option value="{{ doc.id }}" selected="selected">{{ doc.slug }}</option>
                             {%  else %}
                                <option value="{{ doc.id }}">{{ doc.slug }}</option>
                             {%  endif %}
                         {%  endfor %}
                     </select>
                    </div>
                  </li>
              </ul>
          {%  endif  %}
          <ul class="nav navbar-nav navbar-right">
            <li>
                <div class='navbar-form form-group'>
                    <select id="language" name="language" class="form-control">
                        {% get_current_language as LANGUAGE_CODE %}
                        {% get_available_languages as LANGUAGES %}
                        {% get_language_info_list for LANGUAGES as languages %}
                        {% for language in languages %}
                            <option value="{{ language.code }}"{% if language.code == LANGUAGE_CODE %} selected="selected"{% endif %}>
                                {{ language.name_local|capfirst }} ({{ language.code }})
                            </option>
                        {% endfor %}
                    </select>
                </div>
            </li>
            <li><a href="{%  url 'offer' %}">{% trans "Offer" %} </a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-help"></span> {% trans "Help" %} <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a class="glyphicon glyphicon-question-sign" href="{%  url 'faq' %}"> {% trans "Frequently Asked Question" %} </a></li>
                <li><a class="glyphicon glyphicon-envelope" href="{%  url 'contact' %}"> {% trans "Contact" %}</a></li>
                <li><a class="glyphicon glyphicon-info-sign" href="{%  url 'about' %}"> {% trans "About us" %}</a></li>
                <li><a class="glyphicon glyphicon-list" href="{%  url 'conditions' %}"> {% trans "Terms & Conditions" %}</a></li>
              </ul>
            </li>
            {% if user.is_authenticated %}
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-user"></span> {{user.first_name}} {{user.last_name}} <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a class="glyphicon glyphicon-home" href="{%  url 'home' %}"> {% trans "Home" %} </a></li>
                <li><a class="glyphicon glyphicon-cog" href="{%  url 'settings' %}"> {% trans "Settings" %}</a></li>
                <li><a class="glyphicon glyphicon-duplicate" href="{%  url 'invoice' %}"> {% trans "Invoices" %}</a></li>
                <li class="divider"></li>
                <li><a class="glyphicon glyphicon-calendar" href="{%  url 'calendar' %}"> {% trans "Calendar" %}</a></li>
                <li><a class="glyphicon glyphicon-equalizer" href="{%  url 'model' %}"> {% trans "Model" %}</a></li>
                <li class="divider"></li>
                <li><a class="glyphicon glyphicon-off" href="{%  url 'logout' %}"> {% trans "Déconnexion" %}</a></li>
              </ul>
            </li>
            {% else %}
            <li><a href="{%  url 'login' %}">{% trans "Connexion" %}</a></li>
            {% endif %}
          </ul>
        </div>
      </div>
    </nav>
    <div class="container"><!--<div class="container-fluid">-->
        <!--[if lt IE 9]>
           	<div id="topwarning">
    		{% blocktrans %}
    		Warning ! You are using an outdated version of Internet Explorer !<br>
    		This website will <strong>NOT</strong> work with your version !
    		Please update to <a href="http://www.microsoft.com/france/windows/internet-explorer/telecharger-ie9.aspx#/top"> Internet Explorer 9</a> or to <a href="http://www.mozilla.org/fr/firefox/new/">Firefox</a>
    		or <a href="https://www.google.com/chrome?hl=fr">Chrome</a>
    		{% endblocktrans %}
    		</div>
    	<![endif]-->
      {% block content %}
        {% if not user.is_authenticated %}
          <div class='row'>
          	<div class="col-md-6 col-md-offset-3" style="margin-top:20px">
              <p><img style="display: block; margin-left: auto; margin-right: auto;" src="/media/img.jpg"/></p>
            </div>
            <div class="col-md-6 col-md-offset-3" style="margin-top:20px">
              <p>{% trans "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempus vel leo eu ultrices. Nulla vitae sem mattis, blandit lacus scelerisque, pharetra velit. Sed pellentesque sagittis purus eget vehicula. Mauris vulputate felis non tempus dignissim. Nulla ac arcu quis diam laoreet hendrerit. Nam vel felis lectus. Pellentesque sodales nulla id purus facilisis, id egestas mi pulvinar." %}</p>  
          	</div>
            <div class="col-md-4 col-md-offset-4" style="margin-top:20px">
              <a href="{% url "login" %}" class="btn btn-success btn-lg btn-block">{% trans "Connexion" %}</a>
            </div>
          </div>
        {% endif %}
      {% endblock %}
    </div>

    <!-- Modal -->
    <div class="modal" id="loading" data-keyboard="false" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body">
            <p class="text-center"><img src="/static/loading.gif" alt="loading"></p>
          </div> 
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div id="confirm_yes" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" id="confirm_yes_close" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">{% trans "Confirmation" %}</h4>
          </div>
          <div class="modal-body">
            <div class="alert alert-success text-center" role="alert">{%trans "Changes applied" %}</div>
            <div id="confirm_yes_text">{{ confirm_yes_text }}</div>
          </div>
            <div class="modal-footer">
              <button id="confirm_yes_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% trans "Ok" %}</button>
            </div>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div id="confirm_no" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" id="confirm_no_close" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">{% trans "Confirmation" %}</h4>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger text-center" role="alert">{%trans "Error" %}</div>
            <div id="confirm_no_error"></div>
          </div>
            <div class="modal-footer">
              <button id="confirm_no_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% trans "Ok" %}</button>
            </div>
        </div>
      </div>
    </div>
  </body>
</html>
