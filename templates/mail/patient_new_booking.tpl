{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello{% endblocktrans %} {{ slot.patient.firstname }}</p><p></p>
<p>{% trans "You just book a appointment on Medagenda." %} {% trans "We thank you for your trust." %}</p>
<p></p>
<p>{% trans "We confirm your appointment :" %}</p>
<p>{%  trans "Date" %} : {{ slot.date }}</p>
<p>{%  trans "Hours" %} : {{ slot.st.start }}</p>
<p>{%  trans "To" %} : {{ slot.refer_doctor }}</p>
<p>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</p>
<p></p>
<p>{% trans "You will find in attachment an ical folder to add the appointment to your calendar." %}</p>
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}