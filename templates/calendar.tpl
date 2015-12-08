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
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <p style="text-align:center;"><h2>{% blocktrans %}Calendrier{% endblocktrans %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2><p>
  </div>
</div>
<div id="calendar"></div>

<!-- Modal -->
<div id="bookingslot" class="modal" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="bookingslot_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Book a slot{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        <form name="form_bookingslot" id="form_bookingslot">
          <input id="id_slot" name="slot" type="hidden" value="0">
          <input id="id_patient" name="patient" type="hidden" value="0">
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_date">{% blocktrans %}Date{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_date" name="date" type="text" class="form-control" disabled>
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_start_time">{% blocktrans %}Start time{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_start_time" name="start_time" type="text" class="form-control" disabled>
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_email">{% blocktrans %}Email{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_email" name="email" type="text" class="form-control">
              <span class="input-group-addon"> @ </span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_first_name">{% blocktrans %}First name{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_first_name" name="first_name" type="text" class="form-control">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_last_name">{% blocktrans %}Last name{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_last_name" name="last_name" type="text" class="form-control">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_telephone">{% blocktrans %}Telephone{% endblocktrans %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_telephone" name="telephone" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-phone-alt"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_informations">{% blocktrans %}Informations{% endblocktrans %} :</label>
            <div class="col-md-7 input-group"><textarea class="form-control" rows="3"></textarea></div>
          </div>
        </form>
      </div>
        <div class="modal-footer">
          {% if user.is_authenticated %}
          <p class="pull-left"><button id="bookingslot_remove" type="submit" class="btn btn-danger" data-dismiss="modal">{% blocktrans %}Remove{% endblocktrans %}</button></p>
          {% endif %}
          <button id="bookingslot_submit" type="submit" class="btn btn-primary" data-dismiss="modal">{% blocktrans %}Submit{% endblocktrans %}</button>
          <button id="bookingslot_cancel" type="button" class="btn btn-default" data-dismiss="modal">{% blocktrans %}Cancel{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>


<!-- Modal -->
<div id="confirm" class="modal" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="confirm_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Confirmation{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
      {% blocktrans %}Change applied{% endblocktrans %}
      </div>
        <div class="modal-footer">
          <button id="confirm_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% blocktrans %}Ok{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>

<!-- Modal -->
<div id="confirm2" class="modal" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="confirm2_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Already Booked{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
      {% blocktrans %}This slot is already booked !{% endblocktrans %}
      </div>
        <div class="modal-footer">
          <button id="confirm2_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% blocktrans %}Ok{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>


<script type="text/javascript">
$(document).ready(function() {
  var event;
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
      event = Event.id;
      $('#id_slot').val(calEvent.id);
      var url = '/slot/ajax/s/get/' + calEvent.id + '/';
      $.ajax({
          url: url,
          type: 'GET',
          data: '',
          traditional: true,
          dataType: 'json',
          success: function(result){
            console.log(result['return']);
            if (result['return']){
              $('#id_date').val(result['slot']['date']);
              $('#id_start_time').val(result['slot']['start']);
              $('#bookingslot').show();
            }
            else{
              $('#confirm2').show();
            }
          }
      }); 
    }
  });

  $('#id_email').focusout(function(){
    var url = '/patient/ajax/search/';
    $.ajax({
        url: url,
        type: 'GET',
        data: {'email': $('#id_email').val()},
        traditional: true,
        dataType: 'json',
        success: function(result){
          console.log(result);
          if (result['return']){
            $('#id_patient').val(result['id']);
            $('#id_first_name').val(result['first_name']);
            $('#id_last_name').val(result['last_name']);
            $('#id_telephone').val(result['telephone']);
          }
          else{
            $('#id_patient').val(0);
            $('#id_first_name').val("");
            $('#id_last_name').val("");
            $('#id_telephone').val("");
          }
        }
    });

  });

  function clean_modal(){
    $('#id_slot').val("0");
    $('#id_patient').val("0");
    $('#id_date').val("");
    $('#id_start').val("");
    $('#id_email').val("");
    $('#id_first_name').val("");
    $('#id_last_name').val("");
    $('#id_telephone').val("");
    $('#id_information').val("");
  }
  
  $('#bookingslot_cancel').click(function(){
    $('#bookingslot').hide();
    clean_modal();
  });

  $('#bookingslot_close').click(function(){
    $('#bookingslot').hide();
    clean_modal();
  });

  $('#bookingslot_submit').click(function(){
    var form = $('#form_bookingslot');
    var url = '/slot/ajax/s/book/' + $('#id_slot').val() + '/';
    $.ajax({
        url: url,
        type: 'GET',
        data: form.serialize(),
        traditional: true,
        dataType: 'json',
        success: function(result){
          
          $('#bookingslot').hide();
          clean_modal();
          $('#confirm').show();

        }
    });  
  });
  $('#bookingslot_remove').click(function(){
    var url = '/slot/ajax/s/remove/' + $('#id_slot').val() + '/';
    $.ajax({
        url: url,
        type: 'GET',
        data: '',
        traditional: true,
        dataType: 'json',
        success: function(result){
          $('#bookingslot').hide();
          clean_modal();
          $('#confirm').show();
        }
    });  
  });

  $('#confirm_close').click(function(){
    $('#confirm').hide();
    location.reload();
  });
  $('#confirm_ok').click(function(){
    $('#confirm').hide();
    location.reload();
  });
  $('#confirm2_close').click(function(){
    $('#confirm2').hide();
  });
  $('#confirm2_ok').click(function(){
    $('#confirm2').hide();
  });
});
</script>
{% endblock %}
