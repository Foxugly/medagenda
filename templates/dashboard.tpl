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
            <div class="panel-heading">Planning</div>
            <div class="panel-body">
                <div class="panel-group">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse1">9:00 Renaud Vilain</a></h3>
                        </div>
                        <div id="collapse1" class="panel-collapse collapse">
                            <div class="panel-body">body renaud
                            </div>
                        </div>
                    </div>
                    <div class="panel panel-info">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse2">9:30 Claire Gheurs</a></h3>
                        </div>
                        <div id="collapse2" class="panel-collapse collapse">
                            <div class="panel-body">body kiki
                            </div>
                        </div>
                    </div>
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse3">10:00 Alyssia Ferrarese</a></h3>
                        </div>
                        <div id="collapse3" class="panel-collapse collapse">
                            <div class="panel-body">body Alyssia
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-6">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <i class="fa fa-bar-chart-o fa-fw"></i> Donut Chart Example
            </div>
            <div class="panel-body">
                body1
            </div>
        </div>
        <div class="panel panel-primary">
            <div class="panel-heading">
                <i class="fa fa-bar-chart-o fa-fw"></i> Slots scheduled
            </div>
            <div class="panel-body">
                <div class="text-center">You scheduled slots to 20/02/2016 (15 days)</div>
                <div class="text-center row_space_top"><a href="/user/model/" class="btn btn-default"><span class="glyphicon glyphicon-equalizer"></span> {% blocktrans %} Model{% endblocktrans %}</a></div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
