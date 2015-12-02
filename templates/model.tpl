{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}

{% block css %}
<link href='/static/fullcalendar-2.5.0/fullcalendar.css' rel='stylesheet' />
<link href='/static/fullcalendar-2.5.0/fullcalendar.print.css' rel='stylesheet' media='print' />
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
<style>
  #calendar {
    /*max-width: 900px;*/
    margin: 0 auto;
  }
  .fc-agendaWeek-view tr {
height: 30px;
}
.fc-unthemed .fc-today {
  background: transparent;
}
.circle{width:15px;height:15px;border-radius:50px;font-size:20px;color:#ffffff;line-height:10px;text-align:center;}.info{position:absolute;color:#000000;margin-left:20px}
</style>
{% endblock %}

{% block js %}
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/moment.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lib/jquery.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/fullcalendar.min.js"></script>
    <script type="text/javascript" src="/static/fullcalendar-2.5.0/lang-all.js"></script>
    <script type="text/javascript" src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
    <script>
      $(document).ready(function() {
        
        $('#calendar').fullCalendar({
          header: false,
          lang: 'fr',
          /*columnFormat: 'dddd',*/
          aspectRatio : 2,
          minTime : '{{doctor.start_time}}',
          maxTime : '{{doctor.end_time}}',
          defaultDate : '{{fullcalendar_ref_date}}',
          allDaySlot : false,
          defaultView : 'agendaWeek',
          editable: false,
          slotLabelFormat : 'H:mm',
          eventLimit: false, // allow "more" link when too many events
          eventClick: function(calEvent, jsEvent, view) {
              alert('Event: ' + calEvent.id);
          },
          /*events:  [{'color': '#73B5EB', 'start': '2016-02-01T10:00:00', 'end': '2016-02-01T10:30:00', 'id': 1, 'title': 'Libre'}]*/
        });
        var date_min = "{{doctor.start_time}}";
        var date_max = "{{doctor.end_time}}";
        var h_table = $(window).height() - 240;
        var d_min = date_min.split(":");
        var d_max = date_max.split(":");
        var nb_slots = 1+(2*(d_max[0]-d_min[0])) + Math.ceil((d_max[1]-d_min[1])/30);
        var p_size = Math.floor(h_table/nb_slots);
        var ratio = Math.floor($("#calendar").width()*1000/(p_size * nb_slots))/1000;
        $('#calendar').fullCalendar('option', 'aspectRatio', ratio);
        $('.fc-agendaWeek-view tr').css('height', p_size);
      });

    </script>
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-12">
    <p class="text-center"><h2 class="text-center">{% blocktrans %}Calendrier{% endblocktrans %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2></p>
  </div>
</div>
<div class="row form-group">
  <div class="col-md-6">
  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#addslots"><span class="glyphicon glyphicon-plus-sign"></span> {% blocktrans %}Add slots{% endblocktrans %}</button>
  <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#removeslots"><span class="glyphicon glyphicon glyphicon-trash"></span> {% blocktrans %}remove all slots{% endblocktrans %}</button>
  </div>
  <div class="col-md-6 text-right">
  <button type="button" class="btn btn-success" data-toggle="modal" data-target="#applyslots"><span class="glyphicon glyphicon-play-circle"></span> {% blocktrans %}Apply slots{% endblocktrans %}</button>
  </div>
</div>
<div id="calendar"></div>
<div class="row" style="margin-top:20px;">
  <div class="col-md-3 col-md-offset-3">
    <div class="circle" style="background:{{doctor.nhs_price_free_slot_color}}"><span class="info">{% blocktrans %}Tarif conventionné{% endblocktrans %}</div>
  </div>
  <div class="col-md-3">
    <div class="circle" style="background:{{doctor.free_price_free_slot_color}}"><span class="info">{% blocktrans %} Tarif libre{% endblocktrans %}</div>
  </div>
</div>
<!-- Modal -->
<div id="addslots" class="modal fade" role="dialog">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Add slots{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        <form id="form_addslots">
        <div class="row form-group"><label class="col-md-2 col-md-offset-1 control-label" for="check_monday">{% blocktrans %}Days{% endblocktrans %} :</label>
          <div class="col-md-8 btn-group" data-toggle="buttons">
            <label class="btn btn-default"><input id="check_monday" name="check_monday" type="checkbox" autocomplete="off"> {% blocktrans %}Monday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_tuesday" name="check_tuesday" type="checkbox" autocomplete="off"> {% blocktrans %}Tuesday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_wednesday" name="check_wednesday" type="checkbox" autocomplete="off"> {% blocktrans %}Wednesday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_thursday" name="check_thursday" type="checkbox" autocomplete="off"> {% blocktrans %}Thursday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_friday" name="check_friday" type="checkbox" autocomplete="off"> {% blocktrans %}Friday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_saturday" name="check_saturday" type="checkbox" autocomplete="off"> {% blocktrans %}Saturday{% endblocktrans %}</label>
            <label class="btn btn-default"><input id="check_sunday" name="check_sunday" type="checkbox" autocomplete="off"> {% blocktrans %}Sunday{% endblocktrans %}</label>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="start_time">{% blocktrans %}Start Time{% endblocktrans %} :</label>
          <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
            <input id="start_time" name="start_time" type="text" class="form-control" value="{{doctor.start_time}}">
            <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="end_time">{% blocktrans %}End Time{% endblocktrans %} :</label>
          <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
            <input id="end_time" name="end_time" type="text" class="form-control" value="{{doctor.end_time}}">
            <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="duration">{% blocktrans %}Duration{% endblocktrans %} :</label>
          <div class="col-md-2" style="padding-right: 0px; padding-left: 0px;">
            <select id="duration" name="duration">
              <option value="0">0</option>
              <option value="5">5</option>
              <option value="10">10</option>
              <option value="15">15</option>
              <option value="20">20</option>
              <option value="25">25</option>
              <option value="30" selected="selected">30</option>
              <option value="45">45</option>
              <option value="60">60</option>
            </select>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="break_time">{% blocktrans %}Break{% endblocktrans %} :</label>
          <div class="col-md-4" style="padding-right: 0px; padding-left: 0px;">
            <select  id="break_time" name="break_time">
              <option value="0" selected="selected">0</option>
              <option value="5">5</option>
              <option value="10">10</option>
              <option value="15">15</option>
              <option value="20">20</option>
              <option value="25">25</option>
              <option value="30">30</option>
            </select>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="pricing">{% blocktrans %}Pricing{% endblocktrans %} :</label>
          <div class="col-md-4" style="padding-right: 0px; padding-left: 0px;">
            <select id="pricing" name="pricing">
              <option value="1">{% blocktrans %}Free pricing{% endblocktrans %}</option>
              <option value="2">{% blocktrans %}National health service pricing{% endblocktrans %}</option>
            </select>
          </div>
        </div>
        <script type="text/javascript">
          $('.clockpicker').clockpicker();
        </script>
      </div>
        <div class="modal-footer">
          <button id="btn_addslots" type="submit" class="btn btn-primary" data-submit="true" data-dismiss="modal">{% blocktrans %}Submit{% endblocktrans %}</button>
          <button type="button" class="btn btn-default" data-submit="false" data-dismiss="modal">{% blocktrans %}Close{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>
<!-- Modal -->
<div id="removeslots" class="modal fade" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Remove all slots{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        {% blocktrans %}Do you really want to remove all slots ?{% endblocktrans %}
      </div>
        <div class="modal-footer">
          <button id="btn_removeslots" type="submit" class="btn btn-primary" data-dismiss="modal">{% blocktrans %}Yes{% endblocktrans %}</button>
          <button type="button" class="btn btn-default" data-dismiss="modal">{% blocktrans %}No{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>
<!-- Modal -->
<div id="applyslots" class="modal fade" role="dialog">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Apply slots{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        <form id="form_applyslots">
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="start_time">{% blocktrans %}Start Time{% endblocktrans %} :</label>
          <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
            <input id="start_time" name="start_time" type="text" class="form-control" value="{{doctor.start_time}}">
            <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-md-2 col-md-offset-1 control-label" for="end_time">{% blocktrans %}End Time{% endblocktrans %} :</label>
          <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
            <input id="end_time" name="end_time" type="text" class="form-control" value="{{doctor.end_time}}">
            <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
          </div>
        </div>
      </div>
        <div class="modal-footer">
          <button id="btn_applyslots" type="submit" class="btn btn-primary" data-submit="true" data-dismiss="modal">{% blocktrans %}Submit{% endblocktrans %}</button>
          <button type="button" class="btn btn-default" data-submit="false" data-dismiss="modal">{% blocktrans %}Close{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>
<script type="text/javascript">
$('#btn_addslots').on("click", function(){
  console.log('addslots');
  var form = $('#form_addslots');
  var url = '/slot/ajax/{{doctor.slug}}/add/';
  console.log(url);
  $.ajax({
      url: url,
      type: 'GET',
      data: form.serialize(),
      traditional: true,
      dataType: 'json',
      success: function(result){
        console.log(result['slots']);
        //$('#calendar').fullCalendar('options', 'events', result['slots']);
        //$('#calendar').fullCalendar({'events': result['slots']});
        $('#calendar').fullCalendar('renderEvent',
            {
                title: 'title',
                start: '2016-02-02T10:00:00',
                end: '2016-02-02T11:00:00'
            });
        console.log('retour');
      }
  });
});
$('#btn_removeslots').on("click", function(){
  console.log('removeslots');
  $('#calendar').fullCalendar('removeEvents');
  var url = '/slot/ajax/{{doctor.slug}}/remove/';
  console.log(url);
  $.ajax({
      url: url,
      type: 'POST',
      data: form.serialize(),
      traditional: true,
      dataType: 'json',
      success: function(result){
        $('#calendar').fullCalendar('options', 'events', result['slots']);
        console.log('retour');
      }
  });
});
$('#btn_applyslots').on("click", function(){
  console.log('applyslots');
  var form = $('#form_applyslots');
  var url = '/slot/ajax/{{doctor.slug}}/apply/';
  console.log(url);
  $.ajax({
      url: url,
      type: 'POST',
      data: form.serialize(),
      traditional: true,
      dataType: 'json',
      success: function(result){
        $('#calendar').fullCalendar('options', 'events', result['slots']);
        console.log('retour');
      }
  });
});
</script>
{% endblock %}
