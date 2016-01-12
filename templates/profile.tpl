{% extends "layout.tpl" %}
{% load i18n %}
{% load tools %}

{% block js %}
<script>
$(document).ready(function() {
    $("#button_reminder").click(function(){
        $("#get_mail").show();
    });

    $("#button_remove").click(function(){
        $("#get_mail").show();
    });

    $("#get_mail_close").click(function(){
        $("#get_mail").hide();
        $("#id_email").val("");
    });

    $("#get_mail_ok").click(function(){
        $("#get_mail").hide();
        $("#id_email").val("");
        var url = '/patient/ajax/reminder/' + {{ doctor.slug }} + '/';
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
                    $('#calendar').fullCalendar( 'removeEvents', id ).fullCalendar('addEventSource', [result['slot']]);
                    $('#confirm_yes').show();
                }
                else{
                    $('#confirm2').show();
                }
            }
        });
        $('#confirm_yes').show();
    });
});
</script>
{%  endblock %}

{% block content %}
<div class="jumbotron">
  <div class="row">
    <div class="col-sm-8 col-md-8">
      <h1>{{doctor.refer_userprofile.user.first_name|capfirst}} {{doctor.refer_userprofile.user.last_name|capfirst}}</h1>
      <h2>{{doctor.MEDECINE_CHOICES|index:doctor.speciality|safe}}</h2>
      <h2>{{doctor.address.locality.name|capfirst}}</h2>
      <p><a class="btn btn-success btn-lg" href="/doc/calendar/{{doctor.slug}}/" role="button">Réserver</a></p>
    </div>
    <div class="col-sm-4 col-md-4">
    {% if doctor.picture %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}{{doctor.picture}}' alt='img' style="vertical-align: middle;max-height:300px;max-width:300px;" />
      {% else %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}pic/profil.jpg' alt='img' style="vertical-align: middle;max-height:300px;max-width:300px;">
      {% endif %}
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span> Prendre un rendez-vous</div>
      <div class="panel-body">
        <p>{{doctor.text_rdv}}</p>
        <p class='text-center'><a class="btn btn-success" href="/doc/calendar/{{doctor.slug}}/" role="button">Réserver</a></p>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span> Informations</div>
      <div class="panel-body">
        <p><span class="glyphicon glyphicon-time" aria-hidden="true"></span> <b> Horaires :</b></p>
        <p>{{doctor.text_horaires}}</p>
        <p><span class="glyphicon glyphicon-map-marker" aria-hidden="true"></span> <b> Adresse :</b></p>
        <p><a href="http://maps.google.com/?q={{doctor.address.formatted|cast}}">{{doctor.address.formatted}}</a></p>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-md-4">
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span> Me rappeler mes rendez-vous</div>
      <div class="panel-body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget suscipit leo, sit amet aliquam lectus.</p>
        <p class='text-center'><a id="button_reminder" class="btn btn-info" href="#" role="button">Voir</a></p>
      </div>
    </div>
    <div class="panel panel-primary">
      <div class="panel-heading"><span class="glyphicon glyphicon-minus-sign" aria-hidden="true"></span> Annuler un rendez-vous</div>
      <div class="panel-body">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget suscipit leo, sit amet aliquam lectus.</p>
        <p class='text-center'><a id="button_remove" class="btn btn-danger" href="#" role="button">Annuler</a></p>
      </div>
    </div>
  </div>
</div>

<!-- Modal -->
<div id="get_mail" class="modal" role="dialog" data-keyboard="false" data-backdrop="static">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" id="get_mail_close" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">{% trans "Reminder / Remove" %}</h4>
      </div>
      <div class="modal-body">
          <div class="row form-group">
              <div class="col-md-10 col-md-offset-1">
                  <p>{%  trans "Could you give your email address, we will send you your booking slots by mail." %}</p>
                  <p>{%  trans "You will receive usefull inforamtions to cancel a booking slot." %}</p>
              </div>
          </div>
          <div class="row form-group">
            <label class="col-md-3 col-md-offset-1 control-label" for="id_email">{% trans "Email" %} :</label>
            <div class="col-md-7 input-group">
              <input id="id_email" name="email" type="text" class="form-control">
              <span class="input-group-addon"> @ </span>
            </div>
          </div>
      </div>
        <div class="modal-footer">
          <button id="get_mail_ok" type="submit" class="btn btn-primary" data-dismiss="modal">{% trans "Ok" %}</button>
        </div>
    </div>
  </div>
</div>
{% endblock %}