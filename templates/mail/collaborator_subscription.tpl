{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello{% endblocktrans %},
<br><br>
{% blocktrans %}{{ collaborator.doctor }} or a collaborator asks you to subscript to Medagenda{% endblocktrans %}.
<br><br>
{% trans "Could you click on the link to subscribe :" %}<a href="{{ uri }}{%  url 'collaborator_add' collaborator_id=collaborator.id confirm=collaborator.confirm %}">{{ link }}{% url 'collaborator_add' collaborator_id=collaborator.id confirm=collaborator.confirm %}</a>
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}