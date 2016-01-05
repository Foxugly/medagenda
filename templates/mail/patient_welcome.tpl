{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello{% endblocktrans %} {{ patient.first_name }}</p><p></p>
<p>{% trans "You just use Medagenda for the first time." %} {% trans "We thank you for your trust." %}</p>
<p>{% trans "Could you click on the link below to confirm your email address :" %}</p>
{{ protocol }}://{{ domain }}{% url 'patient_confirm_create' patient_id=patient.id text=patient.confirm %}
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}