{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{% load staticfiles %}

{% get_current_language as LANGUAGE_CODE %}
{% block js %}
<script>
$(document).ready(function() {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        views: {
            month: {
                timeFormat: 'H:mm'
            }
        },
        lang: '{{ LANGUAGE_CODE }}',
        firstDay: 1,
        editable: false,
        defaultView : 'agendaWeek',
        allDaySlot : false,
        aspectRatio : 2,
        contentHeight: 'auto',
        minTime : '{{doctor.start_time|time_format}}',
        maxTime : '{{doctor.end_time|time_format}}',
        eventLimit: false,
        {% if slots %}
            events: {{slots|safe}},
        {% endif %}
        eventClick: function (calEvent) {
            $('#id_slot').val(calEvent.id);
            var url = '/slot/ajax/s/get/' + calEvent.id + '/';
            $.ajax({
                url: url,
                type: 'POST',
                traditional: true,
                dataType: 'json',
                success: function(result){
                    if (result['return']){
                        $('#id_date').val(result['slot']['date']);
                        $('#id_start_time').val(result['slot']['start']);
                        if (result['slot']['booked'] ){
                          $('#id_last_name').val(result['slot']['last_name']);
                          $('#id_first_name').val(result['slot']['first_name']);
                          $('#id_email').val(result['slot']['email']);
                          $('#id_telephone').val(result['slot']['telephone']);
                          $('#id_informations').val(result['slot']['informations']);
                        }
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
                if (result['return']){
                    $('#id_patient').val(result['patient']['id']);
                    $('#id_first_name').val(result['patient']['first_name']);
                    $('#id_last_name').val(result['patient']['last_name']);
                    $('#id_telephone').val(result['patient']['telephone']);
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
        $('#id_informations').val("");
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
        var id = $('#id_slot').val();
        var url = '/slot/ajax/s/book/' + id + '/';
        $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                $('#bookingslot').hide();
                clean_modal();
                if (result['return']){
                    $('#calendar').fullCalendar( 'removeEvents', id );
                    $('#calendar').fullCalendar('addEventSource', [result['slot']]);
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm2').show();
                }
            }
        });
    });
    $('#bookingslot_remove').click(function(){
        var id = $('#id_slot').val();
        var url = '/slot/ajax/s/remove/' + id + '/';
        $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#calendar').fullCalendar( 'removeEvents', id );
                    $('#bookingslot').hide();
                    clean_modal();
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
    });

    $('#bookingslot_clean').click(function(){
        var id = $('#id_slot').val();
        var url = '/slot/ajax/s/clean/' + id + '/';
        $.ajax({
            url: url,
            type: 'POST',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    $('#calendar').fullCalendar( 'removeEvents', id );
                    $('#calendar').fullCalendar('addEventSource', [result['slot']]);
                    $('#bookingslot').hide();
                    clean_modal();
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm_no_error').val(result['errors']);
                    $('#confirm_no').show();
                }
            }
        });
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

{% block content %}
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <p style="text-align:center;"><h2>{% trans "Calendar" %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.refer_userprofile.user.first_name|capfirst}} {{doctor.refer_userprofile.user.last_name|capfirst}}</h2><p>
  </div>
</div>
<div id="calendar"></div>
<div class="row text-center" style="margin-top:20px;">
    <ul class="legend">
    {% for c in doctor.colorslots.all %}
        <li><span style="background-color: {{c.free_slot_color}};"></span>
            {% if user.userprofile == doctor %}
                <span style="background-color: {{c.booked_slot_color}};"></span>
            {% else %}
                {% if doctor.view_busy_slot %}
                    <span style="background-color: {{c.booked_slot_color}};"></span>
                {% endif %}
            {% endif %}
            {{ c.SLOT_TYPE|index:c.slot}}</li>
     {% endfor %}
     </ul>
</div>
<!-- Modal -->
<div id="bookingslot" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="bookingslot_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Book a slot" %}</h4>
      </div>
      <div class="modal-body">
        <form name="form_bookingslot" id="form_bookingslot">
          <input id="id_slot" name="slot" type="hidden" value="0">
          <input id="id_patient" name="patient" type="hidden" value="0">
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_date">{% trans "Date" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_date" name="date" type="text" class="form-control" disabled>
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_start_time">{% trans "Start time" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_start_time" name="start_time" type="text" class="form-control" disabled>
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_email">{% trans "Email" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_email" name="email" type="text" class="form-control">
              <span class="input-group-addon"> @ </span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_first_name">{% trans "First name" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_first_name" name="first_name" type="text" class="form-control">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_last_name">{% trans "Last name" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_last_name" name="last_name" type="text" class="form-control">
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_telephone">{% trans "Telephone" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_telephone" name="telephone" type="text" class="form-control" placeholder="+475123456">
              <span class="input-group-addon"><span class="glyphicon glyphicon-phone"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_informations">{% trans "Informations" %} :</label>
            <div class="col-md-7 input-group"><textarea id="id_informations" name="informations" class="form-control" rows="3"></textarea></div>
          </div>
        </form>
      </div>
        <div class="modal-footer">
          {% if user.is_authenticated %}
          <span class="pull-left">
            <button id="bookingslot_remove" type="submit" class="btn btn-danger" data-dismiss="modal">{% trans "Remove" %}</button>
            <button id="bookingslot_clean" type="submit" class="btn btn-danger" data-dismiss="modal">{% trans "Clean" %}</button>
          </span>
          {% endif %}
          <button id="bookingslot_submit" type="submit" class="btn btn-primary" data-dismiss="modal">{% trans "Submit" %}</button>
          <button id="bookingslot_cancel" type="button" class="btn btn-default" data-dismiss="modal">{% trans "Cancel" %}</button>
        </div>
    </div>
  </div>
</div>

<!-- Modal -->
<div id="confirm2" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="confirm2_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Already Booked" %}</h4>
      </div>
      <div class="modal-body">
      {% trans "This slot is already booked !" %}
      </div>
        <div class="modal-footer">
          <button id="confirm2_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% trans "Ok" %}</button>
        </div>
    </div>
  </div>
</div>
{% endblock %}