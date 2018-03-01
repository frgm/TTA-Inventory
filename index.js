function onSignIn(googleUser) {
  var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '');  //CHANGE THIS
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      response = xhr.responseText.split(" ");  //User name, user type
      console.log(response)
      //load page according to response[1] 
    };
    xhr.send('idtoken=' + id_token);
}
