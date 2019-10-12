/** UI Methods */

/** How JSON message response shows in the UI*/
function message(status, shake=false, id="") {
  if (shake) {
    $("#"+id).effect("shake", {direction: "right", times: 2, distance: 8}, 250)
  }
  document.getElementById('feedback').innerHTML = status
  $("#feedback").show().delay(2000).fadeOut()
}

/** Behavior for error, such as a wrong password, the form board becomes red */
function error(type) {
  $("."+type).css("border-color", "#E14448")
}

/** Behavior for login*/
var login = function() {
  $.post({
    type: "POST",
    url: "/",
    data: {"username": $("#login-user").val(),
           "password": $("#login-pass").val()},
    success: function(response){
      var status = JSON.parse(response)['status']
      if (status === 'Login successful') {location.reload()}
      else {error('login-input')}}
  })
}

/** Behavior for sign up, including the several JSON response form app.py*/
$(document).ready(function() {

  $(document).on("click", "#login-button", login)
  $(document).keypress(function(e) {if(e.which === 13) {login()}})

  $(document).on("click", "#signup-button", function() {
    $.post({
      type: "POST",
      url: "/signup",
      data: {"username": $("#signup-user").val(),
             "password": $("#signup-pass").val(),
             "email": $("#signup-mail").val()},
      success: function(response) {
        var status = JSON.parse(response)['status']
        if (status === 'Signup successful') {location.reload()}
        else {message(status, shake=true, id="signup-box")}
      }
    })
  })

})