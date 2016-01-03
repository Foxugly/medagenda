{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
    <div class="h1 row_space text-center">{% trans 'Setting New password' %}</div>
    {% if validlink %}
        <p>{% trans "Please enter your new password twice. So we can verify you typed it in correctly" %}.</p>
        <form action="" method="post" class="form-horizontal">
            <div class="row">
                <div style="display:none">
                    <input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
                </div>
                {% bootstrap_form form layout="horizontal"%}
            </div>
            <div class="row">
                <div class="form_group">
                    <div class="col-md-9 col-md-offset-3">
                        <button type="submit" class="btn btn-primary"> {%  trans "Change my password" %}</button>
                    </div>
                </div>
            </div>
        </form>
    {% else %}
        <h1>{% trans "Password reset unsuccessful" %}</h1>
        <p>{% trans "The password reset link was invalid," %} <br />
        {% trans "possibly because it has already been used" %}. <br />
        {% trans "Please request a new password reset" %}.</p>
    {% endif %}
{% endblock %}