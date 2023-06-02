const APP_DOMAIN = "http://localhost:8000";

$(document).ready(function () {
  $(".more-det-btn").click(function () {
    $(this).siblings(".more-det-content").toggleClass("active-det");
    $(this).find(".less-con").toggleClass("active");
    $(this).find(".more-con").toggleClass("active");
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

// -blog---
$(document).ready(function () {
  $(".sidebox-btn").click(function () {
    $(".sidebox-filter").addClass("show");
    $(".sidebox-btn").hide();
    $(".sidebox-close").show();
  });
  $(".sidebox-close").click(function () {
    $(".sidebox-btn").show();
    $(".sidebox-close").hide();
    $(".sidebox-filter").removeClass("show");
  });
});

// ----------tabs and slider--------
$(function () {
  $(".tab-container").each(function () {
    var $slider = $(this).find(".slider");
    var $tabContent = $(this).find(".tab");

    $slider.tabs();
    $tabContent.hide();
    $tabContent.first().show();
    $slider.find("li").first().addClass("active"); // Add "active" class to the first tab

    $slider.on("click", "li", function () {
      $tabContent.hide();
      var activeTab = $(this).find("a").attr("href");
      $(activeTab).show();
      $(this).addClass("active").siblings().removeClass("active");
    });
  });
});

$(document).ready(function () {
  $(".slider").slick({
    autoplay: false,
    arrows: true,
    infinite: false,
    slidesToShow: 4,
    responsive: [
      {
        breakpoint: 1300,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 1000,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
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
    let j = currentUrl.search(/\?/);
    let newUrl = "";
    if (i < 0)
      if (j < 0) newUrl = currentUrl + "?provider=" + provider;
      else newUrl = currentUrl + "&provider=" + provider;
    // Replace the "provider" query parameter with the new value
    else newUrl = currentUrl.replace(regex, `$1provider=${provider}$2`);

    window.location.replace(newUrl);
  });
  $(".association").click(function () {
    const assoc = [];
    $('input[name="association"]').each(function () {
      if ($(this).is(":checked")) {
        assoc.push($(this).val());
      }
    });
    const currentUrl = window.location.href;
    // Create a regular expression to match the "provider" query parameter
    const regex = /(\?|&)assoc=[\d,]+(&|$)/;
    let i = currentUrl.search("assoc");
    let j = currentUrl.search(/\?/);
    let newUrl = "";
    if (i < 0)
      if (j < 0) newUrl = currentUrl + "?assoc=" + assoc.join(",");
      else newUrl = currentUrl + "&assoc=" + assoc.join(",");
    // Replace the "provider" query parameter with the new value
    else if (assoc.length === 0) newUrl = currentUrl.replace(regex, "");
    else newUrl = currentUrl.replace(regex, `$1assoc=${assoc.join(",")}$2`);
    window.location.replace(newUrl);
  });
});
