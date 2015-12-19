{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{% load staticfiles %}
{% block css %}
<style>
.fc-unthemed .fc-today {
  background: transparent;
}
</style>
{% endblock %}
{% get_current_language as LANGUAGE_CODE %}
{% block js %}
<script>
$(document).ready(function() {
    $('#calendar').fullCalendar({
      header: false,
        lang: '{{ LANGUAGE_CODE }}',
        firstDay: 1,
        columnFormat: 'dddd',
        aspectRatio : 2,
        contentHeight: 'auto',
        minTime : '{{doctor.start_time|time_format}}',
        maxTime : '{{doctor.end_time|time_format}}',
        defaultDate : '{{fullcalendar_ref_date}}',
        allDaySlot : false,
        defaultView : 'agendaWeek',
        editable: false,
        //slotLabelFormat : 'H:mm',
        {% if slottemplates %}
        events: {{slottemplates|safe}},
        {% endif %}
        eventClick: function(calEvent) {
            $('#slot').val(calEvent.id);
            $('#removeslot').show();
        },
        eventLimit: false
    });

    $('#removeslot_close').click(function(){
        $('#removeslot').hide();
    });

    $('#removeslot_no').click(function(){
        $('#removeslot').hide();
    });
    $('#removeslot_yes').click(function(){
        var url = '/slot/ajax/st/remove/' + $('#slot').val() + '/';
        $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#calendar').fullCalendar( 'removeEvents' ,$('#slot').val());
                    $('#removeslot').hide();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });  
    });

    var startDate = new Date();
    var FromEndDate = new Date();
    var ToEndDate = new Date();
    ToEndDate.setDate(ToEndDate.getDate()+365);

    $('#start_date').datepicker({
        language: "{{user.userprofile.language}}",
        startDate: startDate,
        autoclose: true
    })
    .on('changeDate', function(selected){
        startDate = new Date(selected.date.valueOf());
        startDate.setDate(startDate.getDate(new Date(selected.date.valueOf())));
        $('#end_date').datepicker('setStartDate', startDate);
    }); 

    $('#end_date').datepicker({
        language: "{{user.userprofile.language}}",
        startDate: startDate,
        endDate: ToEndDate,
        autoclose: true
    })
    .on('changeDate', function(selected){
        FromEndDate = new Date(selected.date.valueOf());
        FromEndDate.setDate(FromEndDate.getDate(new Date(selected.date.valueOf())));
        $('#start_date').datepicker('setEndDate', FromEndDate);
    });

    $('#btn_addslots').on("click", function(){
        $('#loading').show();
        var form = $('#form_addslots');
        var url = '/slot/ajax/st/add/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                $('#calendar').fullCalendar('removeEvents').fullCalendar('addEventSource', result['slottemplates']);
                $('#loading').hide();
                $('#confirm_yes').show();
            }
        });
    });

    $('#btn_removeslots').on("click", function(){
        $('#loading').show();
        var url = '/slot/ajax/st/clean/';
        $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#calendar').fullCalendar('removeEvents');
                    $('#loading').hide();
                    $('#confirm_yes').show();
                }
                else{
                    $('#loading').hide();
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    $('#btn_applyslots').on("click", function(){
        $('#loading').show();
        var form = $('#form_apply').serializeArray();
        {% get_current_language as LANGUAGE_CODE %}
        form.push({name: 'date_format',value:$.fn.datepicker.dates['{{LANGUAGE_CODE}}']['format']});
        var url = '/slot/ajax/st/apply/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form,
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#loading').hide();
                    $('#confirm_yes').show();
                }
                else{
                    $('#loading').hide();
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });
});
</script>
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-12">
    <h2 class="text-center">{% trans "Calendar Model" %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2>
  </div>
</div>
<div class="row form-group">
  <div class="col-md-6">
  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#addslots"><span class="glyphicon glyphicon-plus-sign"></span> {% trans "Add slots" %}</button>
  <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#removeslots"><span class="glyphicon glyphicon glyphicon-trash"></span> {% trans "remove all slots" %}</button>
  </div>
  <div class="col-md-6 text-right">
  <button type="button" class="btn btn-success" data-toggle="modal" data-target="#applyslots"><span class="glyphicon glyphicon-play-circle"></span> {% trans "Apply slots" %}</button>
  </div>
</div>
<div id="calendar"></div>
<div class="row text-center" style="margin-top:20px;">
  <ul class="legend">
  {% for c in user.userprofile.colorslots.all %}
    <li><span style="background-color: {{c.free_slot_color}};"></span> <span style="background-color: {{c.booked_slot_color}};"></span> {{ c.SLOT_TYPE|index:c.slot}}</li>
  {% endfor %}
  </ul>
</div>

<!-- Modal -->
<div id="addslots" class="modal fade" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Add slots" %}</h4>
      </div>
      <div class="modal-body">
        <form name="form_addslots" id="form_addslots">
          <div class="row form-group"><label class="col-md-2 col-md-offset-1 control-label" for="check_monday">{% trans "Days" %}:</label>
            <div class="col-md-8 btn-group" data-toggle="buttons">
              <label class="btn btn-default"><input id="check_monday" name="check_monday" type="checkbox" > {% trans "Monday" %}</label>
              <label class="btn btn-default"><input id="check_tuesday" name="check_tuesday" type="checkbox" > {% trans "Tuesday" %}</label>
              <label class="btn btn-default"><input id="check_wednesday" name="check_wednesday" type="checkbox" > {% trans "Wednesday" %}</label>
              <label class="btn btn-default"><input id="check_thursday" name="check_thursday" type="checkbox" > {% trans "Thursday" %}</label>
              <label class="btn btn-default"><input id="check_friday" name="check_friday" type="checkbox" > {% trans "Friday" %}</label>
              <label class="btn btn-default"><input id="check_saturday" name="check_saturday" type="checkbox" > {% trans "Saturday" %}</label>
              <label class="btn btn-default"><input id="check_sunday" name="check_sunday" type="checkbox" > {% trans "Sunday" %}</label>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label" for="start_time">{% trans "Start Time" %}:</label>
            <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
              <input id="start_time" name="start_time" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
            <script>
              $("#start_time").val("{{doctor.start_time}}");
            </script>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label" for="end_time">{% trans "End Time" %}:</label>
            <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
              <input id="end_time" name="end_time" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
            <script>
              $("#end_time").val("{{doctor.end_time}}");
            </script>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label" for="duration">{% trans "Duration" %}:</label>
            <div class="col-md-2" style="padding-right: 0; padding-left: 0;">
              <select id="duration" name="duration" class="select2-nosearch">
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
            <label class="col-md-2 col-md-offset-1 control-label" for="break_time">{% trans "Break" %}:</label>
            <div class="col-md-2" style="padding-right: 0; padding-left: 0;">
              <select  id="break_time" name="break_time" class="select2-nosearch">
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
            <label class="col-md-2 col-md-offset-1 control-label" for="slot_type">{% trans "Type" %}:</label>
            <div class="col-md-8" style="padding-right: 0; padding-left: 0;">
              <select id="slot_type" name="slot_type" class="select2-nosearch">
              {% for st in slot_type %}
                <option value="{{st.0}}">{{st.1}}</option>
              {% endfor %}
              </select>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label">{% trans "Availability" %}:</label>
            <div class="col-md-4" style="padding-right: 0; padding-left: 0;">
              <div class="btn-group" data-toggle="buttons">
                <label class="btn btn-default active"><input name="booked" value="0" checked="checked" type="radio">{% trans "Free" %}</label>
                <label class="btn btn-default"><input name="booked" value="1" type="radio">{% trans "Booked" %}</label>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button id="btn_addslots" type="submit" class="btn btn-primary" data-submit="true" data-dismiss="modal">{% trans "Submit" %}</button>
        <button type="button" class="btn btn-default" data-submit="false" data-dismiss="modal">{% trans "Close" %}</button>
      </div>
    </div>
  </div>
</div>
<!-- Modal -->
<div id="removeslots" class="modal fade" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Remove all slots" %}</h4>
      </div>
      <div class="modal-body">
        {% trans "Do you really want to remove all slots ?" %}
      </div>
        <div class="modal-footer">
          <button id="btn_removeslots" type="submit" class="btn btn-danger" data-dismiss="modal">{% trans "Yes" %}</button>
          <button type="button" class="btn btn-default" data-dismiss="modal">{% trans "No" %}</button>
        </div>
    </div>
  </div>
</div>

<div id="removeslot" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="removeslot_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Remove a slot" %}</h4>
      </div>
      <div class="modal-body">
        <form id="form_remove_slot" name="form_remove_slot">
        <input id="slot" name="slot" type="hidden"> 
        </form>
        {% trans "Do you really want to remove this slot ?" %}
      </div>
        <div class="modal-footer">
          <button id="removeslot_yes" type="submit" class="btn btn-danger" data-dismiss="modal">{% trans "Yes" %}</button>
          <button id="removeslot_no" type="button" class="btn btn-default" data-dismiss="modal">{% trans "No" %}</button>
        </div>
    </div>
  </div>
</div>


<!-- Modal -->
<div id="applyslots" class="modal fade" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Add slots" %}</h4>
      </div>
      <div class="modal-body">
        <form name="form_apply" id="form_apply">
          <div class="row form-group">
            <label class="col-md-4 col-md-offset-1 control-label" for="start_date">{% trans "Start Date" %}:</label>
            <div class="col-md-4 input-group" data-placement="right" data-align="top" data-autoclose="true">
              <input id="start_date" name="start_date" type="text" class="form-control datepicker">
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-4 col-md-offset-1 control-label" for="end_date">{% trans "End Date" %}:</label>
            <div class="col-md-4 input-group" data-placement="right" data-align="top" data-autoclose="true">
              <input id="end_date" name="end_date" type="text" class="form-control datepicker">
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
        </form>
      </div>
        <div class="modal-footer">
          <button id="btn_applyslots" type="submit" class="btn btn-primary" data-submit="true" data-dismiss="modal">{% trans "Submit" %}</button>
          <button type="button" class="btn btn-default" data-submit="false" data-dismiss="modal">{% trans "Close" %}</button>
        </div>
    </div>
  </div>
</div>

{% endblock %}
