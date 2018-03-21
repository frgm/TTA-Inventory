$(function() {
    //var itemList = ["testItem1","testItem2","testItem3"]; //change this
    today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
    var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
        $.ajax({
        method: 'GET',
        url : 'report/db',
        data: {}
    }).done(function(response){
        if(response.success){
            delete response.success;
            $("#btnReport").click(makeReport(itemList));
            makeForm(itemList);
        }
    });
    

});

function makeForm(items){
    $form=$('<form id="frmReport" action=""></form>');
    for(var i = 0; i < items.length; i++){
        $form.append('<label class="lblForm">'+ items[i] +'</label>');
        $form.append('<input type="text" name="'+ items[i] +'" id="'+ items[i] +'" class="inpForm">');
        $form.append('</br>')
    }
    $("#divReport").append($form);
    
    $("#lblRegister").click(function(){
        $("#divReport").slideToggle();
    });
}

function makeReport(items){
    report = {};
    for(var i = 0; i < items.length; i++){
        report[items[i]] = $('#'+items[i]).val;
    }
    $.ajax({
        method: 'POST',
        url = 'report/db',
        data: report
    }).done(function(response){
        if(response.success){
            alert('OK');
        }
    });
}