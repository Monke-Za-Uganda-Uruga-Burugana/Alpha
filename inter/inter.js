$(function() {
    $("p").hide();
    $("h2").hide();
    $("ul").hide();
    $( window ).resize(function() {
      var w = $(window).width() / 3.5 + "px";
      $("ul").css("padding-left", w)
    })
    var w = $(window).width() / 3.5 + "px";
    $("ul").css("padding-left", w)
    $("h1").click(function() {
      $("p").show();
      $("p").click(function() {
        $("h2").show();
        $("ul").show();
      })
    })
    
  })