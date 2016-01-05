{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello{% endblocktrans %} {{ userprofile.user.first_name }}</p><p></p>
<p>{% trans "You just create an account to Medagenda." %} {% trans "We thank you for your trust." %}</p>
{% if b_link %}
<p>{% trans "Could you click on the link below to confirm your email address :" %}</p>
{{ protocol }}://{{ domain }}{% url 'confirm_user' user_id=userprofile.user.id text=userprofile.confirm  %}
{%  endif %}
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}