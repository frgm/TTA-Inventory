$(function() {
    $("input").filter(".btn").each(function(){
        $(this).one('click',makeEntry($(this).attr("class").split(' ')[1]));
    });
    $("input").filter(".btncsv").each(function(){
        $(this).one('click',csvEntry($(this).attr("class").split(' ')[1]));
    });
});


function  makeEntry(table){
    vals = {}
    $('.'+table).each(function(){
        vals[$(this).attr("class")] = $(this).val();
    });
    $.ajax({
        method: 'POST',
        url : 'adminPro/db',
        data: {'type': table, 'data': vals}
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}

function csvEntry(table){
    csv = $("#inpCSV").val();
    $.ajax({
        method: 'POST',
        url : 'adminPro/db',
        data: {'type': 'CSV'+table, 'data': csv}
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}