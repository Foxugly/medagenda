{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}

    {% if faq %}
        <ol>
        {%  for f in faq %}
            <li>{{ f.question }}</li>
        {%  endfor %}
        </ol>
        {%  for f in faq %}
            <p>{{ f.question }}</p>
            <p>{{ f.answer }}</p>
        {%  endfor %}
    {%  endif %}
{% endblock %}


