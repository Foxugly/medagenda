{% extends "layout.tpl" %}
{% load i18n %}
{% block content %}
{% if userprofile.user.is_authenticated %}
  {% if userprofile.user.is_superuser %}
<div class="row">
  <div class="col-md-3">
    <a href="/user/adduser/" class="btn btn-lg btn-primary"><span class="glyphicon glyphicon-plus"></span> {% blocktrans %}Ajouter un medecin{% endblocktrans %}</a>
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
      <input type="text" class="form-control input-lg" placeholder="Chercher votre médecin"><span class="input-group-btn "><button class="btn btn-default btn-lg" type="button"><span class="glyphicon glyphicon-search" aria-hidden="true"></button></span>
    </div>
  </div>
</div>
{% endif %}
<p></p>
<div class="row">
  <div class="col-sm-3">
    <div class="thumbnail">
      <p style="text-align:center;"><img src="/media/pic/profil.jpg"></p>
      <p style="text-align:center;">Docteur Julie Tricot</p>
      <p style="text-align:center;">Médecine générale</p>
      <p  style="text-align:center;">Lesve</p>
      <p style="text-align:center;"><a class="btn btn-info" href="#" role="button">Plus d'infos</a></p>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="thumbnail">
      <p style="text-align:center;"><img src="/media/pic/profil.jpg"></p>
      <p style="text-align:center;">Docteur Alyssia Ferraresse</p>
      <p style="text-align:center;">Médecine générale</p>
      <p style="text-align:center;">Ixelles</p>
      <p style="text-align:center;"><a class="btn btn-info" href="#" role="button">Plus d'infos</a></p>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="thumbnail">
      <p style="text-align:center;"><img src="/media/pic/profil.jpg"></p>
      <p style="text-align:center;">Docteur Claire Gheurs</p>
      <p style="text-align:center;">Médecine générale</p>
      <p style="text-align:center;">Woluwé-Saint-Etienne</p>
      <p style="text-align:center;"><a class="btn btn-info" href="#" role="button">Plus d'infos</a></p>
    </div>
  </div>
  <div class="col-sm-3">
    <div class="thumbnail">
      <p style="text-align:center;"><img src="/media/pic/profil.jpg"></p>
      <p style="text-align:center;">Docteur Céline bombeck</p>
      <p style="text-align:center;">Médecine d'urgence</p>
      <p style="text-align:center;">La Louvière</p>
      <p style="text-align:center;"><a class="btn btn-info" href="#" role="button">Plus d'infos</a></p>
    </div>
  </div>
</div>
{% endblock %}