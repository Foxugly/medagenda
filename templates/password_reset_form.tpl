{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}

{% block content %}
<div class="h1 row_space text-center">{% trans 'Reset Password' %}</div>
<p>{% trans "Please specify your email address to receive instructions for resetting it" %}.</p>
<form action="" method="post">
    <div style="display:none">
        <input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
    </div>
     {{ form.email.errors }}
    <div class="form-group">
        <label class="col-md-4 control-label" for="id_email">{% trans 'E-mail address' %}:</label>
        <div class="col-md-4">
            <input id="id_email" type="email" name="email" maxlength="254" class="form-control input-md">
            <span class="help-block"></span>
        </div>
    </div>
    <div class="form-group">
        <div class="col-md-4 col-md-offset-4">
            <input type="submit" class="btn btn-primary" value="{%  trans 'Reset password' %}" />
        </div>
    </div>
</form>
{% endblock %}