/**
 * Created by nielsdaw on 15/11/2016.
 */

var mymap = L.map('mapid').setView([40.423775571194, -3.7021841036754], 13);
var currentLocation;
var id = "nillernoels.24baa0ml";
var access_token = "pk.eyJ1IjoibmlsbGVybm9lbHMiLCJhIjoiY2l2am50dmFhMDBiNzJ1cGd0bzVsY3VjMSJ9.Hr1EeBRdOpIOTYHxmXtZSA";
var markers = [
    [40.423775571194, -3.7021841036754, "<b>La Bicicletta</b><br>You've been here for a coffee"],
    [40.42299018029149, -3.702220219708498, "<b>Demode</b><br>You've been here too party"],
    [40.4239493, -3.7007546, "<b>Cafe bueno</b><br>You've been drinking tea here "],
    [40.4156747, -3.6952896000000237, "<b>Mondo Disko</b><br>You've been partying here"],
    [40.4223334, -3.706136600000036, "<b>Vega</b><br>You've been eating healthy here"]
]

$(document).ready(function () {
    createMap(mymap);
    // setAllMarkers(markers);
});


// Loop through optional list of markers
// and bind it to my map
function setAllMarkers(list1, list2, list3){
    list1 = list1 || 0;
    list2 = list2 || 0;
    list3 = list3 || 0;

    if (list1){
        for (i = 0; i < list1.length; i++) {
            marker = L.marker([list1[i][0], list1[i][1]]).addTo(mymap);
            marker.bindPopup(list1[i][2]);
        }
    }

    if (list2){
        for (i = 0; i < list2.length; i++) {
            marker = L.marker([list2[i][0], list2[i][1]]).addTo(mymap);
            marker.bindPopup(list2[i][2]);
        }
    }

    if (list3){
        for (i = 0; i < list3.length; i++) {
            marker = L.marker([list3[i][0], list3[i][1]]).addTo(mymap);
            marker.bindPopup(list3[i][2]);
        }
    }

}

// create the map
function createMap(map){
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + access_token, {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: id,
        accessToken: access_token
    }).addTo(map);
}

// Ask client for current position
function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            alert(position.coords.latitude + ","+ position.coords.longitude);
        })
    }
    else {
        alert("Geolocation is not supported by this browser.");
    }
}
