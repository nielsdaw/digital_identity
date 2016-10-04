/**
 * Created by nielsdawartz on 03/10/16.
 */

// open sidebar - copied from simple-side-bar-stuff
$(document).ready(function () {
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#menu-div").show();
    });
});


// close the sidebar and hide the menu-bar-button
$(document).ready(function () {
    $("#menu-toggle-2").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#menu-div").hide();
    });
});


