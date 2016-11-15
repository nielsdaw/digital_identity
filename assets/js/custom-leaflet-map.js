/**
 * Created by nielsdaw on 15/11/2016.
 */

var mymap = L.map('mapid').setView([40.423775571194, -3.7021841036754], 13);

var id = "nillernoels.24baa0ml";
var access_token = "pk.eyJ1IjoibmlsbGVybm9lbHMiLCJhIjoiY2l2am50dmFhMDBiNzJ1cGd0bzVsY3VjMSJ9.Hr1EeBRdOpIOTYHxmXtZSA";


$(document).ready(function () {
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + access_token, {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: id,
        accessToken: access_token
    }).addTo(mymap);

    var marker = L.marker([40.423775571194, -3.7021841036754]).addTo(mymap);
    marker.bindPopup("<b>La Bicicletta</b><br>You've been here, Yay").openPopup();

});


function setAllMarkers(list){


}


