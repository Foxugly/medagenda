{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}

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
</style>
{% endblock %}


{% block js %}
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/moment.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/jquery.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/fullcalendar.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lang-all.js"></script>
    <script>
      $(document).ready(function() {

        $('#calendar').fullCalendar({
          header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
          },
          views: {
            month: { // name of view
                timeFormat: 'H:mm'
            }
          },
          lang: 'fr',
          aspectRatio : 2,
          contentHeight: 'auto',
          minTime : '{{doctor.start_time}}',
          maxTime : '{{doctor.end_time}}',
          allDaySlot : false,
          defaultView : 'agendaWeek',
          editable: false,
          slotLabelFormat : 'H:mm',
          eventLimit: false, // allow "more" link when too many events
          {% if slots %}
          events:  {{slots|safe}},
          {% endif %}
          eventClick: function(calEvent, jsEvent, view) {
              alert('Event: ' + calEvent.id);
          }
          
        });
        
      });

    </script>
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <p style="text-align:center;"><h2>{% blocktrans %}Calendrier{% endblocktrans %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2><p>
  </div>
</div>
<div id="calendar"></div>
{% endblock %}
