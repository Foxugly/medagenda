{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello {{ patient.first_name }}{% endblocktrans %},
<br><br>
{% trans "You just use Medagenda for the first time." %} {% trans "We thank you for your trust." %}
<br><br>
{% trans "Could you click on the link below to confirm your email address :" %} <a href="{{ uri }}{% url 'patient_confirm_create' patient_id=patient.id text=patient.confirm %}">{{ uri }}{% url 'patient_confirm_create' patient_id=patient.id text=patient.confirm %}</a>
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}