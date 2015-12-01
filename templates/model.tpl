{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{% block js %}
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/moment.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/jquery.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/fullcalendar.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lang-all.js"></script>
    <script>
      $(document).ready(function() {

        $('#calendar').fullCalendar({
          header: {
            left: '',
            center: '',
            right: ''
          },
          views: {
            month: { // name of view
                timeFormat: 'H:mm'
            }
          },
          lang: 'fr',
          columnFormat: 'dddd',
          aspectRatio : 2,
          minTime : '10:00:00',
          maxTime : '17:00:00',
          allDaySlot : false,
          defaultView : 'agendaWeek',
          editable: false,
          slotLabelFormat : 'H:mm',
          eventLimit: false, // allow "more" link when too many events
          eventClick: function(calEvent, jsEvent, view) {
              alert('Event: ' + calEvent.id);
          },
          /*events: {{slots|safe}}*/
        });
        
      });

    </script>
{% endblock %}
{% block css %}
<link href='/static/fullcalendar-2.5.0/fullcalendar.css' rel='stylesheet' />
<link href='/static/fullcalendar-2.5.0/fullcalendar.print.css' rel='stylesheet' media='print' />
<style>
  #calendar {
    /*max-width: 900px;*/
    margin: 0 auto;
  }
  .fc-agendaWeek-view tr {
height: 35px;
}

.fc-agendaDay-view tr {
height: 35px;
}
.fc-unthemed .fc-today {
  background: transparent;
}
</style>
{% endblock %}


{% block content %}
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <p style="text-align:center;"><h2>{% blocktrans %}Calendrier{% endblocktrans %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2><p>
  </div>
</div>
<div id="calendar"></div>
{% endblock %}
