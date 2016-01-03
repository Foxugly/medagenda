{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% block content %}
<div class="h1 row_space text-center">{% trans 'Password reset successful' %}</div>
<p>{% trans "We've e-mailed you instructions for setting your password to the e-mail address you submitted" %}.</p>
<p>{% trans "You should be receiving it shortly" %}.</p>
{% endblock %}
