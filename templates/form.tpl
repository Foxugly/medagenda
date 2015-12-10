{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{%block css %}
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
<link href='/static/bootstrap-datepicker-master/dist/css/datepicker3.css' rel='stylesheet' />
<link href='/static/bootstrap-colorpicker-master/dist/css/bootstrap-colorpicker.min.css' rel='stylesheet' />
<link href='/static/css/perso.css' rel='stylesheet' />
{% endblock %}

{% block js %}
<script type="text/javascript" src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
<script src='/static/bootstrap-datepicker-master/dist/js/bootstrap-datepicker.min.js'></script>
<script src='/static/bootstrap-colorpicker-master/dist/js/bootstrap-colorpicker.min.js'></script>
<script>
$(document).ready(function() {
    $(".clockpicker").parent().clockpicker({
        autoclose: true
    });

    $('.datepicker').datepicker({
        autoclose: true,
        orientation: "bottom right"
    });

    $('.colorpicker').colorpicker({
        format: 'hex',
        customClass: 'colorpicker-2x',
        sliders: {
            saturation: {
                maxLeft: 200,
                maxTop: 200
            },
            hue: {
                maxTop: 200
            },
            alpha: {
                maxTop: 200
            }
        }
    }).on('changeColor', function(ev) {
        $(this).css({'background-color' : $(this).val()});
    });

    $('.colorpicker').focusout(function(){
        $(this).css({'background-color' : $(this).val()});
    });
});
</script>
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
{% endblock %}


