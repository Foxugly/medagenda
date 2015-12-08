{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}

{% block content %}
<div class="row">
  <div class="alert alert-success" role="alert">{% if title %} {{title}} {% else %} Operation Succeed !{% endif %}</div>
  {% if mail %}
  <div class="alert alert-warning" role="alert">Check your mailbox to confirm your email adress ! Your account will be locked until you click on the link you receive</div>
  {% endif %}
</div>
<div class="row">
  <div class="col-md-8 col-md-offset-2 text-center" style="margin-top:20px">
    <a href="/" class="btn btn-success btn-default"><span class="glyphicon glyphicon-home"></span> {% blocktrans %}Home{% endblocktrans %} </a>
    {% if request.user.is_authenticated %}
      <a href="/user/profil/{{user.userprofile.slug}}/calendar/" class="btn btn-default"><span class="glyphicon glyphicon-calendar"></span> {% blocktrans %} Calendar{% endblocktrans %}</a> 
      <a href="/user/profil/{{user.userprofile.slug}}/model/" class="btn btn-default"><span class="glyphicon glyphicon-equalizer"></span> {% blocktrans %} Model{% endblocktrans %}</a>{{ user.userprofile.slug }}
    {% endif %}
  </div>
</div>
{% endblock %}


