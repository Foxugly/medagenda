{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{%block css %}
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
{% endblock %}

{% block js %}
<script type="text/javascript" src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
{% endblock %}

{% block content %}
<form class="form-horizontal" method="post" action="{{url}}" {% if enctype_form %} {{enctype_form|safe}} {% endif %} >
  {% csrf_token %}
  <fieldset>
    <!-- Form Name -->
    <legend><h1>{{title}}</h1></legend>
    <div class="row">
    {% bootstrap_form form layout="horizontal"%}
    </div>
    <div class="row">
      <div class="form_group">
        <div class="col-md-9 col-md-offset-3">
          <button type="submit" class="btn btn-primary" layout="horizontal"> Submit</button>
        </div>
      </div>
    </div>  
  </fieldset>
</form>
<script type="text/javascript">
$(".colorfield_field").addClass('form-control');

  $(".clockpicker").parent().clockpicker({
    autoclose: true
  });
</script>
{% endblock %}


