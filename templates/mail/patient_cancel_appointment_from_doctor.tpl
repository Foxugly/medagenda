{% load i18n %}{% autoescape off %}
{% blocktrans %}Hello {{ slot.patient.first_name }}{% endblocktrans %},
<br><br>
{% trans "You booked a appointment on Medagenda." %} {% trans "We thank you for your trust." %}
<br><br>
{% trans "We inform you that an appointment is cancelled :" %}
<ul>
<li>{%  trans "Date" %} : {{ slot.date }}</li>
<li>{%  trans "Hour" %} : {{ slot.st.start }}</li>
<li>{%  trans "To" %} : {{ slot.refer_doctor.full_name }}</li>
<li>{%  trans "Address" %} : {{ slot.refer_doctor.address }}</li>
</ul>
{% blocktrans %}We invite you to contact {{ slot.refer_doctor.full_name }} for any explanation.{% endblocktrans %}
<br><br>
{% trans "Thanks for using our site!" %}
<br><br>
{% blocktrans %}The {{ site_name }} team{% endblocktrans %}
{% endautoescape %}