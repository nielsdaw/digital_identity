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


//Start Cookie Consent plugin by Silktide - http://silktide.com/cookieconsent -->
$(document).ready(function () {
    window.cookieconsent_options = {
        "message":"We use cookies",
        "dismiss":"I understand",
        "learnMore":"More info",
        "link":'/privacy_policy',
        "theme":"dark-bottom"
    };
});
