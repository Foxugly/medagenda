{% comment %}

# Copyright 2015, Foxugly All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
{% load i18n %}

<!DOCTYPE HTML>
<html lang="en">
  <head>
    <title>MedAgenda</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <!--  CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" integrity="sha256-7s5uDGW3AHqw6xtJmNNtr+OBRJUlgkNJEo78P4b0yRw= sha512-nNo+yCHEyn0smMxSswnf/OnX6/KwJuZTlNZBjauKhTK0c+zT+q5JOCx0UFhXQ6rJR9jg6Es8gPuD2uZcYDLqSw==" crossorigin="anonymous"/>
    {% block css %}
    {% endblock %}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha256-KXn5puMvxCw+dAYznun+drMdG1IFl3agK0p/pqT9KAo= sha512-2e8qq0ETcfWRI4HJBzQiA3UoyFk6tbNyG+qSaIBZLyW9Xf3sWZHN/lxe9fTh1U45DpPf07yj94KsUHHWe4Yk1A==" crossorigin="anonymous"></script>
    {% block js %}
    {% endblock %}
    <script>
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
      });
    </script>
    <style>
      body {
        padding-top: 60px;
      }
    </style>

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
          <ul class="nav navbar-nav navbar-right">
            <li><div class='navbar-form form-group'>
              <select class="form-control" >
                <option>Français</option>
                <option>Nederlands</option>
                <option>English</option>
              </select>
            </div>
            </li>
            <li><a href="#">{% trans "Help" %} </a></li>
            {% if user.is_authenticated %}
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-user"></span> {{user.first_name}} {{user.last_name}} <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a class="glyphicon glyphicon-home" href="/"> {% trans "Home" %} </a></li>
                <li><a class="glyphicon glyphicon-cog" href="/user/update_user/"> {% trans "Change Settings" %}</a></li>
                <li><a class="glyphicon glyphicon-lock" href="/user/password_change/"> {% trans "Change Password" %}</a></li>
                <li class="divider"></li>
                <li><a class="glyphicon glyphicon-calendar" href="/user/profil/{{user.userprofile.slug}}/calendar/"> {% trans "Calendar" %}</a></li>
                <li><a class="glyphicon glyphicon-equalizer" href="/user/profil/{{user.userprofile.slug}}/model/"> {% trans "Model" %}</a></li>
                <li class="divider"></li>
                <li><a class="glyphicon glyphicon-off" href="/user/logout/"> {% trans "Déconnexion" %}</a></li>
              </ul>
            </li>
            {% else %}
            <li><a href="/user/login/">{% trans "Connexion" %}</a></li>
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
              <a href="/user/login" class="btn btn-success btn-lg btn-block">{% trans "Connexion" %}</a>
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
