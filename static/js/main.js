const APP_DOMAIN = "http://localhost:8000";

$(document).ready(function () {
  $(".more-det-btn").click(function () {
    $(".more-det-content").toggleClass("active-det");
    $(".less-con").toggleClass("active");
    $(".more-con").toggleClass("active");
  });
});

// ----------------input type-toggle-----
$(document).ready(function () {
  $(".icon-show").click(function () {
    $("#password").attr("type", "text");
    $(this).css("display", "none");
    $(".icon-hide").css("display", "block");
  });
  $(".icon-hide").click(function () {
    $("#password").attr("type", "password");
    $(this).css("display", "none");
    $(".icon-show").css("display", "block");
  });
});

// ---navbar-mbl------
$(document).ready(function () {
  $(".menu").click(function () {
    var submenu = $(this).find(".submenu");
    var icon = $(this).find("i");
    $(".submenu").not(submenu).slideUp();
    submenu.slideToggle();
    icon.toggleClass("up");
  });

  $(".toggler").click(function () {
    $(".mbl-nav").show();
    $(".toggler").hide();
  });
  $(".close-icon").click(function () {
    $(".mbl-nav").hide();
    $(".toggler").show();
  });
});

// ---card-provider select------
$(document).ready(function () {
  $(".provider").click(function () {
    const currentUrl = window.location.href;
	provider = $(this).val();

    // Create a regular expression to match the "provider" query parameter    
    const regex = /(\?|&)provider=\d+(&|$)/;
    let i = currentUrl.search(regex);
    let newUrl = "";
    if (i < 0) newUrl = currentUrl + "?provider=" + provider;
    // Replace the "provider" query parameter with the new value
    else newUrl = currentUrl.replace(regex, `$1provider=${provider}$2`);
	
    window.location.replace(newUrl);
  });
});
