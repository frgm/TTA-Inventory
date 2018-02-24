$(function() {
    var localList = {"test Location 1":{address:"test address", items:{"testItem1":100, "testItem2":50}}, "test Location 3":{address:"test address 2", items:{"testItem4":100, "testItem3":50}}}; //change this
    var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
    today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
    makeForm(localList);
});

function makeForm(locals){
    var date = new Date();
    var d = date.getDate();
    $.each(locals, function(key, value){
        $location = $('<div id="div'+ key +'" class="divLocation sliding" style="display: none"></div>');
        $location.append('<label class="lblAddress">'+ value.address +'</label></br>');
        //google map here
        $location.append('</br>')
        $location.append('<label class="lblLocation">En este local hoy"'+ d +'"debes entregar:</label></br>');
        $items = $('<div id="divItems'+ key +'" class="divItems"></div>');
        $.each(value.items, function(key2, value2){
            $items.append('<label class="lblItem">'+ key2 +':'+ value2 +'</label></br>');
        });
        $location.append($items)
        $label = $('<label id="lbl'+ key +'" class="slideClick">'+ key +'</label>')
        $label.click(function(){
            $(this).next(".divLocation").slideToggle();
        });
        $("#divDistribution").append($label)
        $("#divDistribution").append($location)
        $("#divDistribution").append("</br>")
    });
}