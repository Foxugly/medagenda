{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
<div class='row row_space'>
    <div class="col-xs-12 text-center h1">Dashboard</div>
</div>
<div class='row'>
    <div class="col-xs-6">
        <div class="panel panel-primary">
            <div class="panel-heading">Planning du jour</div>
            <div class="panel-body">
                <div class="panel-group">
                    {%  for p in plan %}
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse{{ p.id }}">{{ p.st.start }} {% if p.patient  %}{{ p.patient.first_name }} {{ p.patient.last_name }}{% endif %}</a></h3>
                        </div>
                        <div id="collapse{{ p.id }}" class="panel-collapse collapse">
                            <div class="panel-body">{% if p.informations %}{{ p.informations }}{%  endif %}
                            </div>
                        </div>
                    </div>
                    {%  endfor %}
                </div>
                <div class="text-center row_space_top"><a href="{%  url 'calendar' %}" class="btn btn-default"><span class="glyphicon glyphicon-calendar"></span> {% blocktrans %} Calendar{% endblocktrans %}</a></div>

            </div>
        </div>
    </div>
    <div class="col-xs-6">
        <div class="panel panel-primary">
            <div class="panel-heading">Abonnement</div>
            <div class="panel-body">
                <p>{% trans "Type" %} : {{ invoice.type_price }}</p>
                <p>{% trans "Start date" %} : {{ invoice.date_start }}</p>
                <p>{% trans "End date" %} : {{ invoice.date_end }}</p>
                <div class="text-center row_space_top"><a href="{%  url 'settings' %}" class="btn btn-default"><span class="glyphicon glyphicon-cog"></span> {% blocktrans %} Settings{% endblocktrans %}</a></div>
            </div>
        </div>
        <div class="panel panel-primary">
            <div class="panel-heading">
                <i class="fa fa-bar-chart-o fa-fw"></i> Slots scheduled
            </div>
            <div class="panel-body">
                {%  if date_max %}
                    <div class="text-center">You scheduled slots to {{ date_max }}</div>
                {%  else  %}
                    <div class="text-center">There is no slots</div>
                {%  endif %}
                <div class="text-center row_space_top"><a href="{%  url 'model' %}" class="btn btn-default"><span class="glyphicon glyphicon-equalizer"></span> {% blocktrans %} Model{% endblocktrans %}</a></div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
