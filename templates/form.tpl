{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
<form class="form-horizontal" method="post" action="{{url}}" {% if enctype_form %} {{enctype_form|safe}} {% endif %} >
  {% csrf_token %}
  <fieldset>
    <!-- Form Name -->
    <legend class="h1 row_space">{{title}}</legend>
    <div class="row">
    {% bootstrap_form form layout="horizontal"%}
    </div>
    <div class="row">
      <div class="form_group">
        <div class="col-md-9 col-md-offset-3">
          <button type="submit" class="btn btn-primary"> {%  trans "Submit" %}</button>
        </div>
      </div>
    </div>  
  </fieldset>
</form>
{% endblock %}


