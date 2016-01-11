{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
    <div class="row row_space" >
        <div class="col-md-12 text-center"><h1>{{title}}</h1></div>
    </div>
<form class="form-horizontal" method="post" action="{{url}}" {% if enctype_form %} {{enctype_form|safe}} {% endif %} >
  {% csrf_token %}
    <div class="row">
        {% for f in form %}
            {% bootstrap_form f layout="horizontal"%}
        {%  endfor %}
    </div>
    <div class="row">
      <div class="form_group">
        <div class="col-md-9 col-md-offset-3">
          <button type="submit" class="btn btn-primary"> {%  trans "Submit" %}</button>
        </div>
      </div>
    </div>
</form>
{% endblock %}
