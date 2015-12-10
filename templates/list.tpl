{% extends "layout.tpl" %}
{% load i18n %}
{% load tools %}
{% block content %}
{% if user.is_authenticated %}
  {% if user.is_superuser %}
<div class="row">
  <div class="col-md-3">
    <a href="/user/add_user/" class="btn btn-lg btn-primary"><span class="glyphicon glyphicon-plus"></span> {% blocktrans %}Create a doctor{% endblocktrans %}</a>
  </div>
  <div class="col-md-8">
    <div class="input-group">
      <input type="text" class="form-control input-lg" placeholder="Chercher votre médecin"><span class="input-group-btn "><button class="btn btn-default btn-lg" type="button"><span class="glyphicon glyphicon-search" aria-hidden="true"></button></span>
    </div>
  </div>
</div>
  {% endif %}
{% else %}
<div class="row">
  <div class="col-md-8 col-md-offset-2">
    <div class="input-group">
      <input type="text" class="form-control input-lg" placeholder="{% blocktrans %}Looking for a doctor{% endblocktrans %}"><span class="input-group-btn "><button class="btn btn-default btn-lg" type="button"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button>
    </div>
  </div>
</div>
{% endif %}
<p></p>
{% for item in list %}
{% if forloop.counter0|divisibleby:"4" %}
<div class="row">
{% endif %}
  <div class="col-sm-3">
    <div class="thumbnail">
      <p style="text-align:center;"><img src="/media/pic/profil.jpg"></p>
      <p style="text-align:center;">{{item.TITLE_CHOICES|index:item.title|safe}} {{item.user.first_name|capfirst}} {{item.user.last_name|capfirst}}</p>
      <p style="text-align:center;">{{item.MEDECINE_CHOICES|index:item.speciality|safe}}</p>
      <p  style="text-align:center;">{{item.address.locality.name}}</p>
      <p style="text-align:center;"><a class="btn btn-info" href="/user/profil/{{item.slug}}/" role="button">Plus d'infos</a></p>
    </div>
  </div>
{% if forloop.last or forloop.counter|divisibleby:4 %}</div>{% endif %}
{% endfor %}
{% endblock %}
