{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello{% endblocktrans %} {{ slot.patient.first_name }}</p><p></p>
<p>{% trans "You just book a appointment on Medagenda." %} {% trans "We thank you for your trust." %}</p>
<p></p>
<p>{% trans "We confirm your appointment :" %}</p>
<ul>
<li>{%  trans "Date" %} : {{ slot.date }}</li>
<li>{%  trans "Hours" %} : {{ slot.st.start }}</li>
<li>{%  trans "To" %} : {{ slot.refer_doctor.full_name }}</li>
<li>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</li>
</ul>
<p>{% trans "You will find in attachment an ical file to add the appointment to your calendar." %}</p>
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}