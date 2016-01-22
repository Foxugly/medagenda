{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello{% endblocktrans %},
<br><br>
{% blocktrans %}{{ collaborator.doctor }} or a collaborator asks you to subscript to Medagenda{% endblocktrans %}.
<br><br>
{%  with link=protocol |add:'://'|add: domain | add: url 'collaborator_add' collaborator_id=collaborator.id confirm=collaborator.confirm %}
{% trans "Could you click on the link to subscribe :" %}<a href="{{ link }}">{{ link }}</a>
{%  endwith %}
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}