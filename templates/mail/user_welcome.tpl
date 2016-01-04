{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello{% endblocktrans %} {{ user.firstname }}</p><p></p>
<p>{% trans "You just create an account to Medagenda." %} {% trans "We thank you for your trust." %}</p>
<p>{% trans "Could you click on the link below to confirm your email address :" %}</p>
{{ protocol }}://{{ domain }}{% url 'confirm_user' user_id=user.id text=user.confirm %}
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}