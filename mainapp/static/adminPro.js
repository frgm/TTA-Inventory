$(function() {
    $("button").not(".csv").each(function(){
        $(this).click(makeEntry($(this).attr("class")));
    });
    $("button").filter(".csv").each(function(){
        $(this).click(csvEntry($(this).attr("class").split(' ')[1]));
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

function csvEntry(table){
    csv = $("#inpCSV").val();
    $.ajax({
        method: 'POST',
        url = 'adminpro/db',
        data: {'type': 'CSV'+table, 'data': csv}
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}