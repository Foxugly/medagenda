{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load tools %}
{% load staticfiles %}
{% block js %}
<script>
$(document).ready(function() {
    var myCenter=new google.maps.LatLng(50.5001,4.70055);
    var map;
    var markers = [
    {% for item in list %}{% if not forloop.first %},{% endif %}
      {"doctor": "{{item.TITLE_CHOICES|index:item.title|safe}} {{item.refer_userprofile.user.first_name|capfirst}} {{item.refer_userprofile.user.last_name|capfirst}}", "spec":"{{item.MEDECINE_CHOICES|index:item.speciality|safe}}", "lat": {{item.address.latitude|safe}},"lng": {{item.address.longitude|safe}},  "link": "/doc/{{item.slug}}/"}
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
    $('#label_list').click(function(){
        $('#div_map').hide();
        $('#div_list').show();
    });
    $('#label_map').click(function(){
        $('#div_list').hide();
        $('#div_map').show();
        initialize();
    });
    function search_doctors(){
        var mydata = {text:$('#search').val()}
        var url = '/doc/ajax/search/';
        $.ajax({
            url: url,
            type: 'POST',
            traditional: true,
            data: mydata,
            dataType: 'json',
            success: function(result){
                if (result['return']){
                    markers = result['list'];
                    initialize();
                    $( "#div_list" ).empty();
                    var out = "";
                    for (var i = 0; i < markers.length; ++i){
                        var doc = markers[i];
                        if (i % 4 == 0){
                            out +='<div class="row">';
                        }
                        out += '<div class="col-sm-3"><div class="thumbnail text-center" >';
                        out += '<div style="height: 200px;background:url({{ MEDIA_URL }}pic/profil.jpg) no-repeat center center;"></div>';
                        out += '<p class="text-center">' + doc.doctor +'</p>';
                        out += '<p class="text-center">' + doc.speciality +'</p>';
                        out += '<p class="text-center">' + doc.locality +'</p>';
                        out += '<p class="text-center"><a class="btn btn-info" href="' + doc.link + '" role="button">Plus d\'infos</a></p>';
                        out += '</div></div>';
                        if (i % 4 == 4 || i == markers.length-1){
                            out+='</div>';
                        }
                    }
                    $( "#div_list" ).html(out);
                }
                else{
                    console.log('erreur');
                }
            }
        });
    }
    $('#search').keydown(function(){
        if(event.keyCode == 13) {
            event.preventDefault();
            search_doctors();
            return false;
        }
    });
    $('#btn_search').click(function(){
        search_doctors();
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
      <input type="text" id="search" class="form-control input-lg" placeholder="{% blocktrans %}Looking for a doctor{% endblocktrans %}"><span class="input-group-btn "><button id="btn_search" class="btn btn-default btn-lg" type="button"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button></span>
    </div>
  </div>
  <div class="col-md-2 text-right">
    <div id="btn_view" class="btn-group" data-toggle="buttons">
       <label id="label_list" class="btn btn-default btn-lg active"><input type="radio" id="view_list" name="view" value="list"/><span class="glyphicon glyphicon-th"></span></label>
       <label id="label_map" class="btn btn-default btn-lg"><input type="radio" id="view_map" name="view" value="map"/><span class="glyphicon glyphicon-globe"></span></label>
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
      {% if item.picture %}
      <div style="height: 200px;background:url({{ MEDIA_URL }}{{item.picture}}) no-repeat center center;">
      {% else %}
        <div style="height: 200px;background:url({{ MEDIA_URL }}pic/profil.jpg) no-repeat center center;">
      {% endif %}
      </div>
      <p class="text-center">{{item.TITLE_CHOICES|index:item.title|safe}} {{item.refer_userprofile.user.first_name|capfirst}} {{item.refer_userprofile.user.last_name|capfirst}}</p>
      <p class="text-center">{{item.MEDECINE_CHOICES|index:item.speciality|safe}}</p>
      <p class="text-center">{{item.address.locality.name}}</p>
      <p class="text-center"><a class="btn btn-info" href="/doc/{{item.slug}}/" role="button">Plus d'infos</a></p>
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
