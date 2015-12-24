{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
    <div class="row row_space" >
        <div class="col-md-12 text-center"><h1>{%  trans "Frequently Asked Questions" %}</h1></div>
    </div>
    {% if faq %}
     <div class="row">
        <div class="col-md-12">
            <div class="panel-group" id="accordion">
                {%  for f in faq %}
                <div class="panel panel-default" id="panel{{ f.id }}">
                    <div class="panel-heading">
                        <h4 class="panel-title">
                            <a data-toggle="collapse" data-target="#collapse{{ f.id }}" href="#collapse{{ f.id }}" class="collapsed">{{ f.question }}</a>
                        </h4>
                    </div>
                    <div id="collapse{{ f.id }}" class="panel-collapse collapse">
                        <div class="panel-body">{{ f.answer }}</div>
                    </div>
                </div>
                {%  endfor %}
            </div>
        </div>
    </div>
    {%  endif %}
{% endblock %}


