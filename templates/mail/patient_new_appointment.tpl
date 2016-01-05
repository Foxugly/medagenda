{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello {{ slot.patient.first_name }},{% endblocktrans %}
<br><br>
{% trans "You just book a appointment on Medagenda." %} {% trans "We thank you for your trust." %}
<br><br>
{% trans "We confirm your appointment :" %}
<ul>
<li>{%  trans "Date" %} : {{ slot.date }}</li>
<li>{%  trans "Hours" %} : {{ slot.st.start }}</li>
<li>{%  trans "To" %} : {{ slot.refer_doctor.full_name }}</li>
<li>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</li>
</ul>
<br>
{% trans "You will find in attachment an ical file to add the appointment to your calendar." %}
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}