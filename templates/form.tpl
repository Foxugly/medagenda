{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% block content %}
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <form class="form-horizontal" method="post" action="{{url}}">
      {% csrf_token %}
      <fieldset>
        <!-- Form Name -->
        <legend><h1>{{title}}</h1></legend>
        {% bootstrap_form form %}
        <button type="submit" class="btn btn-primary"> Submit</button>
      </fieldset>
    </form>
  </div>
</div>


{% endblock %}

