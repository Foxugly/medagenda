{% extends "layout.tpl" %}
{% load bootstrap3 %}

{%block css %}
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
{% endblock %}

{% block js %}
<script type="text/javascript" src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
{% endblock %}

{% block content %}

<form class="form-horizontal" method="post" action="{{url}}">
  {% csrf_token %}
  <fieldset>
    <!-- Form Name -->
    <legend><h1>{{title}}</h1></legend>
    <div class="row">
    {% bootstrap_form form layout="horizontal"%}
    </div>
        <button type="submit" class="btn btn-primary" layout="horizontal"> Submit</button>   
  </fieldset>
</form>
<script>
$(document).ready(function(){
  $(".colorfield_field").addClass('form-control');

  $(".clockpicker").parent().clockpicker({
    autoclose: true
  });
});
</script>
{% endblock %}


