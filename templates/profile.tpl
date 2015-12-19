{% extends "layout.tpl" %}
{% load i18n %}
{% load tools %}
{% block content %}
<div class="jumbotron">
  <div class="row">
    <div class="col-sm-8 col-md-8">
      <h1>{{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h1>
      <h2>{{doctor.MEDECINE_CHOICES|index:doctor.speciality|safe}}</h2>
      <h2>{{doctor.address.locality.name|capfirst}}</h2>
      <p><a class="btn btn-success btn-lg" href="/user/p/calendar/{{doctor.slug}}/" role="button">Réserver</a></p>
    </div>
    <div class="col-sm-4 col-md-4">
    {% if doctor.picture %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}{{doctor.picture}}' alt='img' style="vertical-align: middle;max-height:300px;max-width:300px;" />
      {% else %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}pic/profil.jpg' alt='img' style="vertical-align: middle;max-height:300px;max-width:300px;">
      {% endif %}
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span> Prendre un rendez-vous</div>
      <div class="panel-body">
        <p>{{doctor.text_rdv}}</p>
        <p class='text-center'><a class="btn btn-success" href="/user/p/calendar/{{doctor.slug}}/" role="button">Réserver</a></p>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span> Informations</div>
      <div class="panel-body">
        <p><span class="glyphicon glyphicon-time" aria-hidden="true"></span> <b> Horaires :</b></p>
        <p>{{doctor.text_horaires}}</p>
        <p><span class="glyphicon glyphicon-map-marker" aria-hidden="true"></span> <b> Adresse :</b></p>
        <p><a href="http://maps.google.com/?q={{doctor.address.formatted}}">{{doctor.address.formatted}}</a></p>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span> Me rappeler mes rendez-vous</div>
      <div class="panel-body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget suscipit leo, sit amet aliquam lectus.</p>
        <p class='text-center'><a class="btn btn-info" href="/user/p/reminder/{{doctor.slug}}/" role="button">Voir</a></p>
      </div>
    </div>
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-minus-sign" aria-hidden="true"></span> Annuler un rendez-vous</div>
      <div class="panel-body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget suscipit leo, sit amet aliquam lectus.</p>
        <p class='text-center'><a class="btn btn-danger" href="/user/p/reminder/{{doctor.slug}}/" role="button">Annuler</a></p>
      </div>
    </div>
  </div>
</div>  
{% endblock %}