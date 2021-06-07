$(function () {
  var dark = 0; var count = 0;
  $("span").click(function () {
    dark++;
    if (dark % 2 === 1) {
      $("body").css("background-color", "white")
      $("span").css("color", "black")
      $("h1").css("color", "black")
      $("h2").css("color", "black")
      $("p").css("color", "black")
      $("a").css("color", "black")
      $("li").css("color", "black")
    } else {
      $("body").css("background-color", "black")
      $("span").css("color", "white")
      $("h1").css("color", "white")
      $("h2").css("color", "white")
      $("p").css("color", "white")
      $("a").css("color", "white")
      $("li").css("color", "white")
    }
    $("span").toggle()
  })
  $("span").click(function () {
    count++;
    $("#total").html("Total clicks: " + count)
    if (count === 69) {
      $("p").show();
    } else {
      $("p").hide();
    }
  })
  $("p").hide();
  $(window).resize(function () {
    var w = $(window).width() / 3 + "px";
    $("ul").css("padding-left", w)
  })
  var w = $(window).width() / 3 + "px";
  $("ul").css("padding-left", w)
})
