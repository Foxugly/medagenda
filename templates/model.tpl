{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}

{% block css %}
<link href='/static/fullcalendar-2.5.0/fullcalendar.css' rel='stylesheet' />
<link href='/static/fullcalendar-2.5.0/fullcalendar.print.css' rel='stylesheet' media='print' />
<link href='/static/bootstrap-datepicker-master/dist/css/datepicker3.css' rel='stylesheet' />
<link href='/static/bootstrap-colorpicker-master/dist/css/bootstrap-colorpicker.min.css' rel='stylesheet' />
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
<link href='/static/css/perso.css' rel='stylesheet' />
<style>
.fc-unthemed .fc-today {
  background: transparent;
}

.circle{width:15px;height:15px;border-radius:50px;font-size:20px;color:#ffffff;line-height:10px;text-align:center;}.info{position:absolute;color:#000000;margin-left:20px}
</style>
{% endblock %}

{% block js %}
<script src='/static/fullcalendar-2.5.0/lib/moment.min.js'></script>
<script src='/static/fullcalendar-2.5.0/lib/jquery.min.js'></script>
<script src='/static/fullcalendar-2.5.0/fullcalendar.min.js'></script>
<script src='/static/fullcalendar-2.5.0/lang-all.js'></script>
<script src='/static/bootstrap-datepicker-master/dist/js/bootstrap-datepicker.min.js'></script>
{% if user.userprofile.language != 'en' %}
<script src='/static/bootstrap-datepicker-master/dist/locales/bootstrap-datepicker.{{user.userprofile.language}}.min.js'></script>
{% endif %}
<script src='/static/bootstrap-colorpicker-master/dist/js/bootstrap-colorpicker.min.js'></script>
<script src="/static/clockfield/bootstrap-clockpicker.min.js"></script>
<script>
$(document).ready(function() {
    /*$('.datepicker').datepicker({
        autoclose: true,
        orientation: "bottom right",
        language: "{{user.userprofile.language}}",
    });*/

    $('.colorpicker').colorpicker({
        format: 'hex',
        customClass: 'colorpicker-2x',
        sliders: {
            saturation: {
                maxLeft: 200,
                maxTop: 200
            },
            hue: {
                maxTop: 200
            },
            alpha: {
                maxTop: 200
            }
        }
    }).on('changeColor', function(ev) {
        $(this).css({'background-color' : $(this).val()});
    });

    $('.colorpicker').focusout(function(){
        $(this).css({'background-color' : $(this).val()});
    });

    $('#calendar').fullCalendar({
      header: false,
        lang: '{{user.userprofile.language}}',
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
        slotLabelFormat : 'H:mm',
        {% if slottemplates %}
        events: {{slottemplates|safe}},
        {% endif %}
        eventClick: function(calEvent, jsEvent, view) {
            event = calEvent;
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
            type: 'GET',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                $('#calendar').fullCalendar( 'removeEvents' ,$('#slot').val());
                $('#removeslot').hide();
            }
        });  
    });

    $('.clockpicker').clockpicker();

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
        var form = $('#form_addslots');
        var url = '/slot/ajax/st/add/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form.serialize(),
            traditional: true,
            dataType: 'json',
            success: function(result){
                for (var i=0; i < result['slottemplates'].length; i++){
                    $('#calendar').fullCalendar('renderEvent',result['slottemplates'][0]);
                }
                location.reload();
            }
        });
    });

    $('#btn_removeslots').on("click", function(){
        var url = '/slot/ajax/st/clean/';
        $.ajax({
            url: url,
            type: 'GET',
            data: '',
            traditional: true,
            dataType: 'json',
            success: function(result){
                $('#calendar').fullCalendar('removeEvents');
            }
        });
    });

    $('#btn_applyslots').on("click", function(){
        var form = $('#form_apply').serializeArray();
        form.push({name: 'format',value:$.fn.datepicker.dates['{{user.userprofile.language}}']['format']});
        var url = '/slot/ajax/st/apply/';
        $.ajax({
            url: url,
            type: 'GET',
            data: form,
            traditional: true,
            dataType: 'json',
            success: function(result){
                console.log('retour');
            }
        });
    });
});
</script>
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-12">
    <p class="text-center"><h2 class="text-center">{% trans "Calendar Model" %}- {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2></p>
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
<div class="row" style="margin-top:20px;">
  <div class="col-md-4 col-md-offset-2 text-center">
    <div class="circle" style="background:{{doctor.nhs_price_free_slot_color}}"><span class="info">{% trans "National Health Service Pricing" %}</span></div>
  </div>
  <div class="col-md-4 text-center">
    <div class="circle" style="background:{{doctor.free_price_free_slot_color}}"><span class="info">{% trans "Free Pricing" %}</span></div>
  </div>
</div>

<!-- Modal -->
<div id="addslots" class="modal fade" role="dialog">
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
              <label class="btn btn-default"><input id="check_monday" name="check_monday" type="checkbox" autocomplete="off"> {% trans "Monday" %}</label>
              <label class="btn btn-default"><input id="check_tuesday" name="check_tuesday" type="checkbox" autocomplete="off"> {% trans "Tuesday" %}</label>
              <label class="btn btn-default"><input id="check_wednesday" name="check_wednesday" type="checkbox" autocomplete="off"> {% trans "Wednesday" %}</label>
              <label class="btn btn-default"><input id="check_thursday" name="check_thursday" type="checkbox" autocomplete="off"> {% trans "Thursday" %}</label>
              <label class="btn btn-default"><input id="check_friday" name="check_friday" type="checkbox" autocomplete="off"> {% trans "Friday" %}</label>
              <label class="btn btn-default"><input id="check_saturday" name="check_saturday" type="checkbox" autocomplete="off"> {% trans "Saturday" %}</label>
              <label class="btn btn-default"><input id="check_sunday" name="check_sunday" type="checkbox" autocomplete="off"> {% trans "Sunday" %}</label>
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
            <div class="col-md-2" style="padding-right: 0px; padding-left: 0px;">
              <select id="duration" name="duration" class="form-control">
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
            <div class="col-md-2" style="padding-right: 0px; padding-left: 0px;">
              <select  id="break_time" name="break_time" class="form-control">
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
            <label class="col-md-2 col-md-offset-1 control-label" for="pricing">{% trans "Pricing" %}:</label>
            <div class="col-md-4" style="padding-right: 0px; padding-left: 0px;">
              <select id="pricing" name="pricing" class="form-control">
                <option value="1">{% trans "Free pricing" %}</option>
                <option value="2">{% trans "National health service pricing" %}</option>
              </select>
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
<div id="removeslots" class="modal fade" role="dialog">
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

<div id="removeslot" class="modal" role="dialog">
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
<div id="applyslots" class="modal fade" role="dialog">
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
