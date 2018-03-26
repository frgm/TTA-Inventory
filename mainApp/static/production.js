$(function() {
    //var localData = {usage:{"17-02-18":20, "18-02-18":15}, dailyItemQuotas:{"testItem1":100, "testItem2":50}, dailyUsage:20}; //change this
    var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
    today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
    $.ajax({
        method: 'GET',
        url : 'production/db',
        data: {}
    }).done(function(response){
        if(response.success){
            delete response.success;
            makeForm(response);
        }
    });
});

function makeForm(data){
    $usageReport = $('<div id="divUsageReport" class="divProdItem sliding" style="display: none"></div>');
    $.each(data.usage, function(key, value){
        $usageReport.append('<label class="lblUsageDay">'+ key +' : '+ value +'quintales</label></br>');
    });
    $("#divProduction").append('<label id="label1" class="lblProdItem slideClick">Reporte uso de Harina<label></br>');
    $("#divProduction").append($usageReport);
    $("#divProduction").append('</br>')
    
    $dailyQuota = $('<div id="divDailyQuota" class="divProdItem sliding" style="display: none"></div>');
    $dailyQuota.append('<label class="lblToDo, lblToDoDate">'+ (new Date()).getDate() +'</label></br>');
    var dailyTotal = 0;
    $.each(data.dailyItemQuotas, function(key, value){
        $dailyQuota.append('<label class="lblToDo, lblToDoItem">'+ key +' : '+ value +'</label></br>');
        dailyTotal = dailyTotal + value;
    });
    $dailyQuota.append('<label class="lblToDo, lblToDoTotal"> Total:'+ dailyTotal +'</label></br>');
    $("#divProduction").append('<label id="label2" class="lblProdItem slideClick">Cantidad de Panes por día<label></br>');
    $("#divProduction").append($dailyQuota);
    $("#divProduction").append('</br>')
    
    $totals = $('<div id="divTotals" class="divProdItem sliding" style="display: none"></div>');
    $totals.append('<label>Hoy '+ today +' debes usar: '+ data.dailyUsage +' quintales</label>')
    $totals.append('<label>Se han usado hoy <input type="text" id="txtTotalInput"></input> quintales de harina<input type="button" onClick="sendUsage"></input></label>')
    $("#divProduction").append('<label id="label3" class="lblProdItem slideClick">Totales<label></br>');    
    $("#divProduction").append($totals);
    $("#divProduction").append('</br></br>');
        
    $(".lblProdItem").click(function(){
        $(this).next(".divProdItem").slideToggle();
    });
}

function sendUsage(){
    usage = $("#txtTotalInput").val()
    $.ajax({
        method: 'POST',
        url : 'production/db',
        data: {'usage':usage}
    }).done(function(response){
        if(response.success){
            alert('Enviado')
        }
    });    
}
            
            