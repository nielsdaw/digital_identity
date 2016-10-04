/**
 * Created by nielsdawartz on 03/10/16.
 */
$(document).ready(function () {
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#menu-div").show();
    });
});



$(document).ready(function () {
    $("#menu-toggle-2").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#menu-div").hide();
    });
});


