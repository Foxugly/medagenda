{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello {{ slot.patient.firstname }}{% endblocktrans %}</p><p></p>
<p>{% trans "You booked a appointment on Medagenda." %} {% trans "We thank you for your trust." %}</p>
<p></p>
<p>{% trans "We inform you that an appointment is cancelled :" %}</p>
<p>{%  trans "Date" %} : {{ slot.date }}</p>
<p>{%  trans "Hour" %} : {{ slot.st.start }}</p>
<p>{%  trans "To" %} : {{ slot.refer_doctor }}</p>
<p>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</p>
<p></p>
<p>{% blocktrans %}We invite you to contact {{ slot.refer_doctor }} for any explanation.{% endblocktrans %}}</p>
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}