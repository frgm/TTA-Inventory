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
    //Backend database here
}
