{% extends "layout.tpl" %}
{% load i18n %}
{% load tools %}

{% block js %}
<script src="http://maps.googleapis.com/maps/api/js"></script>
<script>
$(document).ready(function() {
    var myCenter=new google.maps.LatLng(50.5001,4.70055);
    var map;
    var markers = [
    {% for item in list %}{% if not forloop.first %},{% endif %}
      {"doctor": "{{item.TITLE_CHOICES|index:item.title|safe}} {{item.user.first_name|capfirst}} {{item.user.last_name|capfirst}}", "spec":"{{item.MEDECINE_CHOICES|index:item.speciality|safe}}", "lat": {{item.address.latitude|safe}},"lng": {{item.address.longitude|safe}},  "link": "/user/p/{{item.slug}}/"}
    {% endfor %}];

    function initialize(){
        var options = {
            center:myCenter,
            zoom:8,
            mapTypeId:google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById("googleMap"),options);

        function addmarker(pos,text,spec, link){
            var marker = new google.maps.Marker({position:pos});
            marker.setMap(map);
            var infowindow = new google.maps.InfoWindow({content:'<a href="' + link + '">' + text + '</a><br>' + spec});
            google.maps.event.addListener(marker, 'click', function() {
                infowindow.open(map,marker);
            });
        }

        for (index = 0; index < markers.length; ++index) {
            addmarker(new google.maps.LatLng(markers[index]["lat"],markers[index]["lng"]),markers[index]["doctor"],markers[index]["spec"],markers[index]["link"]);
        }
    }
    $('#div_map').hide();

    $("#btn_view").find("input[name='view']").on("change", function () {
        if($('#btn_view').find('input:radio[name=view]:checked').val() == "map"){
            $('#div_list').hide();
            $('#div_map').show();
            initialize();
        }
        else{
            $('#div_map').hide();
            $('#div_list').show();
        }
    });
});
</script>
{% endblock %}

{% block content %}
<div class="row row_space">
  <div class="col-md-2">
    {% if user.is_authenticated %}
      {% if user.is_superuser %}
    <a href="/user/add_user/" class="btn btn-lg btn-primary"><span class="glyphicon glyphicon-plus"></span> {% blocktrans %}Create a doctor{% endblocktrans %}</a>
      {% endif %}
    {% endif %}
  </div>
  <div class="col-md-8">
    <div class="input-group">
      <input type="text" class="form-control input-lg" placeholder="{% blocktrans %}Looking for a doctor{% endblocktrans %}"><span class="input-group-btn "><button class="btn btn-default btn-lg" type="button"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button></span>
    </div>
  </div>
  <div class="col-md-2 text-right">
    <div id="btn_view" class="btn-group" data-toggle="buttons">
       <label class="btn btn-default btn-lg active"><input type="radio" id="view_list" name="view" value="list"/><span class="glyphicon glyphicon-th"></span></label>
       <label class="btn btn-default btn-lg"><input type="radio" id="view_map" name="view" value="map"/><span class="glyphicon glyphicon-map-marker"></span></label>
    </div>
  </div>
</div>
<div id="div_list">
{% for item in list %}
{% if forloop.counter0|divisibleby:"4" %}
<div class="row">
{% endif %}
  <div class="col-sm-3">
    <div class="thumbnail text-center" >
      <div style="height: 200px;">
      {% if item.picture %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}{{item.picture}}' style="vertical-align: middle;max-height:200px;max-width:200px;">
      {% else %}
        <span style="display: inline-block; height: 100%;vertical-align: middle;"></span><img src='{{ MEDIA_URL }}pic/profil.jpg' style="vertical-align: middle;max-height:200px;max-width:200px;">
      {% endif %}
      </div>
      <p style="text-align:center;">{{item.TITLE_CHOICES|index:item.title|safe}} {{item.user.first_name|capfirst}} {{item.user.last_name|capfirst}}</p>
      <p style="text-align:center;">{{item.MEDECINE_CHOICES|index:item.speciality|safe}}</p>
      <p  style="text-align:center;">{{item.address.locality.name}}</p>
      <p style="text-align:center;"><a class="btn btn-info" href="/user/p/{{item.slug}}/" role="button">Plus d'infos</a></p>
    </div>
  </div>
{% if forloop.last or forloop.counter|divisibleby:4 %}</div>{% endif %}
{% endfor %}
</div>
<div id="div_map">
    <div class="row">
      <div class="col-md-12">
          <div id="googleMap" class="text-center" style="width:100%;height:600px;"></div>
      </div>
    </div>
</div>
{% endblock %}
