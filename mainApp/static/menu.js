$(function(){
    $(".menuDiv").each(function(index){
        $(this).bind(click, function() {
            alert("Rol no eprmitido");
        });
    });
    $.ajax({
        method: 'GET',
        url: 'menu/db',
        data: {}
    }).done(function(response){
        if(response.success){
            if (response.role & 16){    //adminPro
                $("#adminPro").bind('click', {param: "adminPro"}, menuClick);
            }else if (response.role & 8){   //adminInv
                $("#adminInv").bind('click', {param: "adminInv"}, menuClick);
            }else if (response.role & 4){   //distribution
                $("#distribution").bind('click', {param: "distribution"}, menuClick);
            }else if (response.role & 2){   //production
                $("#production").bind('click', {param: "production"}, menuClick);
            }else if (response.role & 1){   //report
                $("#report").bind('click', {param: "report"}, menuClick);
            }else{
                alert("Roles no encontrados");
            }                
        } else {
            alert("Usuario no encontrado")
        }
    });
});

function menuClick(id){
    window.location.href = id; 
}