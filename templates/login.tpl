{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% block content %}
{% if next %}
    {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
    {% else %}
    {% endif %}
{% endif %}

<div class="row">
  <div class="col-sm-6 col-md-4 col-md-offset-4">
    <h1 class="text-center login-title">Authentification</h1>
    <div class="form-group text-center">
        <img class="profile-img" src="/media/img.jpg" width="80%" alt="img">
    </div>
    <form method="post" action="{% url 'django.contrib.auth.views.login' %}">
      {% csrf_token %}
      {% if form.errors %}
        <div class="alert alert-danger" role="alert">Your username and password didn't match. Please try again</div>
      {% endif %}
      <div class="form-group">
          <input id="id_username" name="username" type="text" class="form-control" placeholder="Username" autofocus>
      </div>
      <div class="form-group">    
          <input id="id_password" name="password" type="password" class="form-control" placeholder="Password">
      </div>
      {% if next %}
        <input type="hidden" name="next" value="{{ next }}" />
      {% else %}
        <input type="hidden" name="next" value="/" />
      {% endif %}
      <div class="form-group">  
          <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </div>
    </form>
    <div class="form-group">  
      <a href="/user/create_user/" class="pull-left new-account">Create an account </a>
      <a href="/user/password/reset/" class="pull-right need-help">Forgot Password</a><span class="clearfix"></span>
    </div>    
  </div>
</div>

{% endblock %}

