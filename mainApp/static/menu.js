$(function(){
    $(".menuDiv").each(function(index){
        $(this).bind(click, function() {
            alert("Rol no permitido");
        });
    });
    $.ajax({
        method: 'GET',
        url: 'menu/db',
        data: {}
    }).done(function(response){
        if(response.success){
            flags = parseInt(response.role);
            alert(flags);
            alert(flags & 8);
            if (flags & 16){    //adminPro
                //$("#adminPro").bind('click', {param: "adminPro"}, menuClick);
                pass;
            }else if (flags & 8){   //adminInv
                $("#adminInv").bind('click', {param: "adminInv"}, menuClick);
            }else if (flags & 4){   //distribution
                $("#distribution").bind('click', {param: "distribution"}, menuClick);
            }else if (flags & 2){   //production
                $("#production").bind('click', {param: "production"}, menuClick);
            }else if (flags & 1){   //report
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