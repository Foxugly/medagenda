{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello {{ userprofile.user.first_name }},{% endblocktrans %}
<br><br>
{% trans "You just create an account to Medagenda." %} {% trans "We thank you for your trust." %}
<br><br>
{% if b_link %}
{% trans "Could you click on the link below to confirm your email address :" %}
<a href="{{ uri }}{% url 'confirm_user' user_id=userprofile.user.id text=userprofile.confirm  %}">{{ uri }}{% url 'confirm_user' user_id=userprofile.user.id text=userprofile.confirm  %}</a>
<br><br>
{%  endif %}
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}