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
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script type="text/javascript" src="/static/js/jquery.min.js"></script>
    <script type="text/javascript" src="/static/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="http://maps.googleapis.com/maps/api/js?libraries=places&amp;sensor=false"></script>
    <script type="text/javascript" src="/static/js/jquery.geocomplete.min.js"></script>
    <script type="text/javascript" src="/static/address/js/address.js"></script>
    <script type="text/javascript" src="/static/colorfield/jscolor/jscolor.js"></script>
    <style>
      body {
        padding-top: 60px;
      }
      /*div[class="row"] {
          border: 1px dotted rgba(0, 0, 0, 0.5);
      }

      div[class^="col-"] {
          background-color: rgba(255, 0, 0, 0.2);
      }*/
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
          <a class="navbar-brand" href="#">MedAgenda</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">{% blocktrans %} Help{% endblocktrans %} </a></li>
            {% if userprofile.user.is_authenticated %}
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> {{userprofile.user.first_name}} {{userprofile.user.last_name}} <span class="caret"></span></a>
              <ul class="dropdown-menu" style='background:black;color:white;'>
                <li><a class="glyphicon glyphicon-cog" href="/user/settings/">{% blocktrans %} Profil{% endblocktrans %} </a></li>
                <li><a class="glyphicon glyphicon-off" href="/user/logout/">{% blocktrans %} Déconnexion{% endblocktrans %} </a></li>
              </ul>
            </li>
            {% else %}
            <li><a href="/user/login/">{% blocktrans %} Connexion{% endblocktrans %} </a></li>
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
      <div class='row'>
        
          {% if not userprofile.user.is_authenticated %}
          	  <div class="col-md-6 col-md-offset-3" style="margin-top:20px"><p><img style="display: block; margin-left: auto; margin-right: auto;" src="http://ltmhs.ca/files/calendar.jpg"/></p></div>
              <div class="col-md-6 col-md-offset-3" style="margin-top:20px">
                {% blocktrans %}
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempus vel leo eu ultrices. Nulla vitae sem mattis, blandit lacus scelerisque, pharetra velit. Sed pellentesque sagittis purus eget vehicula. Mauris vulputate felis non tempus dignissim. Nulla ac arcu quis diam laoreet hendrerit. Nam vel felis lectus. Pellentesque sodales nulla id purus facilisis, id egestas mi pulvinar.</p>
                {% endblocktrans %}   
          	  </div>
              <div class="col-md-4 col-md-offset-4" style="margin-top:20px">
                <a href="/user/login" class="btn btn-success btn-lg btn-block">{% blocktrans %}Connexion{% endblocktrans %} </a>
              </div>
  	        </div>
          {% endif %}
        
      </div>
      {% endblock %}
      <!--<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
      <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>-->
      {% block js %}
      {% endblock %}
    </div>
  </body>
</html>
