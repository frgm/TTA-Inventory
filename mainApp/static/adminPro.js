$(function() {
    $("input").filter(".btn").on('click',function(event){
        makeEntry($(this).attr("class").split(' ')[1]);
    });    
    $("input").filter(".btncsv").on('click',function(event){
        csvEntry($(this).attr("class").split(' ')[1]);
    });
});


function  makeEntry(table){
    vals = ""
    $('.'+table).not('.btn,.btncsv').each(function(){
        vals += $(this).val() + ','
    });
    vals = vals.slice(0,-1);
    $.ajax({
        method: 'POST',
        url : 'adminPro/db',
        data: {'type': table, 'data': vals}
    }).done(function(response){
        if(response.success){
            alert("Ingresado con indice: " + response.pk);
        }
    });
}

function csvEntry(table){
    csv = $("#inpCSV").val();
    $.ajax({
        method: 'POST',
        url : 'adminPro/db',
        data: {'type': table, 'data': csv}
    }).done(function(response){
        if(response.success){
            alert("Ingresado con indice: " + response.pk);
        }
    });
}