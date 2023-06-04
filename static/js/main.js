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
// ------accordian----
$(document).ready(function () {
  $(".accordion-list > li > .answer").hide();

  $(".accordion-list > li").click(function () {
    if ($(this).hasClass("active")) {
      $(this).removeClass("active").find(".answer").slideUp();
    } else {
      $(".accordion-list > li.active .answer").slideUp();
      $(".accordion-list > li.active").removeClass("active");
      $(this).addClass("active").find(".answer").slideDown();
    }
    return false;
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
    let currentUrl = window.location.href;
    provider = $(this).val();
    let regex = /(\?|&)end=\d+(&|$)/;
    currentUrl = currentUrl.replace(regex, "");
    // Create a regular expression to match the "provider" query parameter
    regex = /(\?|&)provider=\d+(&|$)/;
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
    let currentUrl = window.location.href;
    let regex = /(\?|&)end=\d+(&|$)/;
    currentUrl = currentUrl.replace(regex, "");

    // Create a regular expression to match the "provider" query parameter
    regex = /(\?|&)assoc=[\d,]+(&|$)/;
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

// --- load more result button click ----
$(document).ready(function () {
  const currentUrl = window.location.href;
  let data_num = $("#data_number").attr("data-my-variable");
  let data_limit = $("#data_end").attr("data-my-variable");

  if (parseInt(data_num) < parseInt(data_limit)) $("#loadMore_btn").hide();
  $("#loadMore_btn").click(function (e) {
    e.preventDefault();
    if (data_num < data_limit) $(this).hide();
    data_limit = parseInt(data_limit) + 20;
    // Create a regular expression to match the "provider" query parameter
    const regex = /(\?|&)end=\d+(&|$)/;
    let i = currentUrl.search(regex);
    let j = currentUrl.search(/\?/);
    let newUrl = "";
    if (i < 0)
      if (j < 0) newUrl = currentUrl + "?end=" + data_limit;
      else newUrl = currentUrl + "&end=" + data_limit;
    // Replace the "provider" query parameter with the new value
    else newUrl = currentUrl.replace(regex, `$1end=${data_limit}$2`);

    window.location.replace(newUrl);
  });
});
