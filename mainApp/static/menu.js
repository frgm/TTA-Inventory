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
            if (flags & 16){    //adminPro
                //$("#adminPro").bind('click', {param: "adminPro"}, menuClick);
                ; //undo
            }
            if (flags & 8){   //adminInv
                $("#adminInv").bind('click', {param: "adminInv"}, menuClick);
                $("#adminInv").removeClass("disabled");
            }
            if (flags & 4){   //distribution
                $("#distribution").bind('click', {param: "distribution"}, menuClick);
                $("#distribution").removeClass("disabled");
            }
            if (flags & 2){   //production
                $("#production").bind('click', {param: "production"}, menuClick);
                $("#production").removeClass("disabled");
            }
            if (flags & 1){   //report
                $("#report").bind('click', {param: "report"}, menuClick);
                $("#report").removeClass("disabled");
            }else{
                alert("Roles no encontrados");
            }                
        } else {
            alert("Usuario no encontrado")
        }
    });
});

function menuClick(event){
    id = event.data.param;
    window.location.href = id; 
}