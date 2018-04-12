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
            flags = parseInt(response.role,2);
            alert(flags);
            alert(flags & 8);
            if (flags & 16){    //adminPro
                //$("#adminPro").bind('click', {param: "adminPro"}, menuClick);
                ;
            }
            if (flags & 8){   //adminInv
                $("#adminInv").bind('click', {param: "adminInv"}, menuClick);
            }
            if (flags & 4){   //distribution
                $("#distribution").bind('click', {param: "distribution"}, menuClick);
            }
            if (flags & 2){   //production
                $("#production").bind('click', {param: "production"}, menuClick);
            }
            if (flags & 1){   //report
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