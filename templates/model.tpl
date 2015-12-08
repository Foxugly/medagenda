{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}

{% block css %}
<link href='/static/fullcalendar-2.5.0/fullcalendar.css' rel='stylesheet' />
<link href='/static/fullcalendar-2.5.0/fullcalendar.print.css' rel='stylesheet' media='print' />
<link href='/static/clockfield/bootstrap-clockpicker.min.css' rel='stylesheet' />
<link href="/static/datepicker/datepicker3.css" rel="stylesheet">
<link href="/static/datepicker/prettify.css" rel="stylesheet">
<link href="/static/datepicker/docs.css" rel="stylesheet">
<style>
.datepicker { z-index: 1151 !important;  }

  #calendar {
    margin: 0 auto;
  }
  .fc-agendaWeek-view tr {
height: 32px;
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
    <script src="/static/datepicker/prettify.min.js"></script>
    <script src="/static/datepicker/bootstrap-datepicker.js"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ar.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.az.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.bg.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.bs.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ca.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.cs.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.cy.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.da.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.de.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.el.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.en-GB.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.es.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.et.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.eu.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.fa.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.fi.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.fo.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.fr.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.fr-CH.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.gl.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.he.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.hr.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.hu.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.hy.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.id.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.is.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.it.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.it-CH.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ja.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ka.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.kh.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.kk.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.kr.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.lt.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.lv.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.mk.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ms.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.nb.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.nl.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.nl-BE.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.no.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.pl.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.pt-BR.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.pt.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ro.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.rs.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.rs-latin.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.ru.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sk.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sl.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sq.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sr.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sr-latin.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sv.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.sw.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.th.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.tr.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.uk.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.vi.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.zh-CN.js" charset="UTF-8"></script>
    <script src="/static/datepicker/bootstrap-datepicker.zh-TW.js" charset="UTF-8"></script>
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-12">
    <p class="text-center"><h2 class="text-center">{% blocktrans %}Calendar{% endblocktrans %} - {{doctor.TITLE_CHOICES|index:doctor.title|safe}} {{doctor.user.first_name|capfirst}} {{doctor.user.last_name|capfirst}}</h2></p>
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
    <div class="circle" style="background:{{doctor.nhs_price_free_slot_color}}"><span class="info">{% blocktrans %}Tarif conventionné{% endblocktrans %}</span></div>
  </div>
  <div class="col-md-3">
    <div class="circle" style="background:{{doctor.free_price_free_slot_color}}"><span class="info">{% blocktrans %} Tarif libre{% endblocktrans %}</span></div>
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
        <form name="form_addslots" id="form_addslots">
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
              <input id="start_time" name="start_time" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
            <script>
              $("#start_time").val("{{doctor.start_time}}");
            </script>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label" for="end_time">{% blocktrans %}End Time{% endblocktrans %} :</label>
            <div class="col-md-2 input-group clockpicker" data-placement="right" data-align="top" data-autoclose="true">
              <input id="end_time" name="end_time" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
            </div>
            <script>
              $("#end_time").val("{{doctor.end_time}}");
            </script>
          </div>
          <div class="row form-group">
            <label class="col-md-2 col-md-offset-1 control-label" for="duration">{% blocktrans %}Duration{% endblocktrans %} :</label>
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
            <label class="col-md-2 col-md-offset-1 control-label" for="break_time">{% blocktrans %}Break{% endblocktrans %} :</label>
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
            <label class="col-md-2 col-md-offset-1 control-label" for="pricing">{% blocktrans %}Pricing{% endblocktrans %} :</label>
            <div class="col-md-4" style="padding-right: 0px; padding-left: 0px;">
              <select id="pricing" name="pricing" class="form-control">
                <option value="1">{% blocktrans %}Free pricing{% endblocktrans %}</option>
                <option value="2">{% blocktrans %}National health service pricing{% endblocktrans %}</option>
              </select>
            </div>
          </div>
          </form>
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
          <button id="btn_removeslots" type="submit" class="btn btn-danger" data-dismiss="modal">{% blocktrans %}Yes{% endblocktrans %}</button>
          <button type="button" class="btn btn-default" data-dismiss="modal">{% blocktrans %}No{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>

<div id="removeslot" class="modal" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="removeslot_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% blocktrans %}Remove a slot{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        <form id="form_remove_slot" name="form_remove_slot">
        <input id="slot" name="slot" type="hidden"> 
        </form>
        {% blocktrans %}Do you really want to remove this slot ?{% endblocktrans %}
      </div>
        <div class="modal-footer">
          <button id="removeslot_yes" type="submit" class="btn btn-danger" data-dismiss="modal">{% blocktrans %}Yes{% endblocktrans %}</button>
          <button id="removeslot_no" type="button" class="btn btn-default" data-dismiss="modal">{% blocktrans %}No{% endblocktrans %}</button>
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
        <h4 class="modal-title">{% blocktrans %}Add slots{% endblocktrans %}</h4>
      </div>
      <div class="modal-body">
        <form name="form_apply" id="form_apply">
          <div class="row form-group">
            <label class="col-md-4 col-md-offset-1 control-label" for="start_date">{% blocktrans %}Start Date{% endblocktrans %} :</label>
            <div class="col-md-4 input-group" data-placement="right" data-align="top" data-autoclose="true">
              <input id="start_date" name="start_date" type="text" class="form-control">
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
          <div class="row form-group">
            <label class="col-md-4 col-md-offset-1 control-label" for="end_date">{% blocktrans %}End Date{% endblocktrans %} :</label>
            <div class="col-md-4 input-group" data-placement="right" data-align="top" data-autoclose="true">
              <input id="end_date" name="end_date" type="text" class="form-control datepicker">
              <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
            </div>
          </div>
        </form>
      </div>
        <div class="modal-footer">
          <button id="btn_applyslots" type="submit" class="btn btn-primary" data-submit="true" data-dismiss="modal">{% blocktrans %}Submit{% endblocktrans %}</button>
          <button type="button" class="btn btn-default" data-submit="false" data-dismiss="modal">{% blocktrans %}Close{% endblocktrans %}</button>
        </div>
    </div>
  </div>
</div>


<script type="text/javascript">
$(document).ready(function() {
  var event;
  $('#calendar').fullCalendar({
    header: false,
    lang: 'fr',
    columnFormat: 'dddd',
    aspectRatio : 2,
    contentHeight: 'auto',
    minTime : '{{doctor.start_time}}',
    maxTime : '{{doctor.end_time}}',
    defaultDate : '{{fullcalendar_ref_date}}',
    allDaySlot : false,
    defaultView : 'agendaWeek',
    editable: false,
    slotLabelFormat : 'H:mm',
    eventLimit: false, // allow "more" link when too many events
    events:  {{templateslots|safe}},
    eventClick: function(calEvent, jsEvent, view) {
        event = calEvent;
        $('#slot').val(calEvent.id);
        //console.log(calEvent.id);

        $('#removeslot').show();
    }
    
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
      language: "fr",
      startDate: startDate,
      autoclose: true
  })
      .on('changeDate', function(selected){
          startDate = new Date(selected.date.valueOf());
          startDate.setDate(startDate.getDate(new Date(selected.date.valueOf())));
          $('#end_date').datepicker('setStartDate', startDate);
      }); 
  $('#end_date')
      .datepicker({
          language: "fr",
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
    form.push({name: 'format',value:$.fn.datepicker.dates['fr']['format']});
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
