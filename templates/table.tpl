{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
<div class='row row_space'>
    <div class="col-xs-12 text-center h1">{{ title }}</div>
</div>
<div class='row'>
    <div class="col-xs-12">
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    {%  for t in table.titles %}
                        <th>{{ t }}</th>
                    {%  endfor %}
                </tr>
            </thead>
            <tbody>
                {%  for data in table.data %}
                    <tr>
                        {%  for td in data %}
                            <td>{{ td|safe }}</td>
                        {%  endfor %}
                    </tr>
                {%  endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}
