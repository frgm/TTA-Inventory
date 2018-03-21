$(function() {
   var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
   today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
   tomorrow = new Intl.DateTimeFormat('es-CL',dateFormat).format((new Date()).getDate() + 1);
   //var usageData = {today: 20, tomorrow: 30, pastValues: [170,150,140], proyectedValues:[180,150,160], precision: 95}; //change this   
   $.ajax({
        method: 'GET',
        url : 'adminInv/db',
        data: {}
    }).done(function(response){
        if(response.success){
            makeForm(response);
        }
    });
});

function makeForm(data){
    $("#divProyection").append('<div id="divGraph"></div>');
    makeGraph(data.pastValues);
    
    $("#divRequisition").append('<label>Hoy debes pedir</label></br>');
    $("#divRequisition").append('<label>'+ today +' : '+ data.today +' Quintales</label></br>');
    $("#divRequisition").append('<label>El proximo pedido debe ser</label></br>');
    $("#divRequisition").append('<label>'+ tomorrow +' : '+ data.tomorrow +' Quintales</label></br>');
    
    $(".slideClick").click(function(){
        $(this).next(".sliding").slideToggle();
    });
}

function makeGraph(xValues){
    var data = {
        x: xValues,
        y: [0,40,80,120,160,200],
        type: 'bar',
        name: 'Proyección'
    };

    var layout = {
        title: '',
        showlegend: false,
        autosize: false,
        width: 300,
        height: 200,
        margin: {
        l: 25,
        r: 15,
        b: 20,
        t: 20,
        pad: 4
    }};
    Plotly.newPlot('divGraph', [data], layout, {displayModeBar: false});
}