{% load i18n %}{% autoescape off %}
<p>{% blocktrans %}Hello {{ slot.patient.first_name }}{% endblocktrans %}</p><p></p>
<p>{% trans "You booked a appointment on Medagenda." %} {% trans "We thank you for your trust." %}</p>
<p></p>
<p>{% trans "We inform you that an appointment is cancelled :" %}</p>
<ul>
<li>{%  trans "Date" %} : {{ slot.date }}</li>
<li>{%  trans "Hour" %} : {{ slot.st.start }}</li>
<li>{%  trans "To" %} : {{ slot.refer_doctor.full_name }}</li>
<li>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</li>
</ul>
<p>{% blocktrans %}We invite you to contact {{ slot.refer_doctor }} for any explanation.{% endblocktrans %}}</p>
<p></p>
<p>{% trans "Thanks for using our site!" %}</p>
<p></p>
<p>{% blocktrans %}The {{ site_name }} team{% endblocktrans %}</p>
{% endautoescape %}