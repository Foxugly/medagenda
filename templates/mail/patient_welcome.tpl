{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello {{ patient.first_name }}{% endblocktrans %},
<br><br>
{% trans "You just use Medagenda for the first time." %} {% trans "We thank you for your trust." %}
<br><br>
{%  with link=protocol |add:'://'|add: domain | add: url 'patient_confirm_create' patient_id=patient.id text=patient.confirm %}
{% trans "Could you click on the link below to confirm your email address :" %}<a href="{{ link }}">{{ link }}</a>
{%  endwith %}
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}