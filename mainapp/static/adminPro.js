$(function() {
    $(".btn").each(function(){
        $(this).click(makeEntry($(this).attr("class")));
    });
});


function  makeEntry(table){
    vals = {}
    $('.'+table).each(function(){
        vals[$(this).attr("class")] = $(this).val();
    });
    $.ajax({
        method: 'POST',
        url = 'adminpro/db',
        data: {'type': table, 'data': vals}
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}

function csvEntry(){
    csv = $("#inpCSV").val();
    $.ajax({
        method: 'POST',
        url = 'adminpro/db',
        data: {'type': 'CSV', 'data': csv}
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}