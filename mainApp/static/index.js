/*function onSignIn(googleUser) {
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
}*/

function login(){
    name = $("#txtName").val();
    pass = $("#txtPass").val();
    $.ajax({
        method: 'POST',
        url: 'index/login',
        data: {'name':name, 'pasw':pass}
    }).done(function(response){
        if(response.success){
            window.location.href = 'menu',
            /*
            switch(response.role){
                case 'adminPro':
                    window.location.href = 'adminPro';
                    break;
                case 'admin':
                    window.location.href = 'adminInv';
                    break;
                case 'distribution':
                    window.location.href = 'distribution';
                    break;
                case 'production':
                    window.location.href = 'production';
                    break;
                case 'report':
                    window.location.href = 'report';
                    break;
                default:
                    alert('Role error');
            }
            */
        }
        else if(!(response.success)){
            alert('Login no encontrado');
        }
    });
}