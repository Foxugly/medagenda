{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}

{% block content %}
<div class="h1 row_space text-center">{% trans 'Password reset complete' %}</div>
<div class="row_space text-center">{% trans "Your password has been set.  You may go ahead and log in now" %}.</p>
<div  class="row_space_top text-center"><a href="{{ login_url }}" class="btn btn-primary" role="button">{% trans "Log in" %}</a></div>
{% endblock %}