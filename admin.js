$(function() {
   var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
   today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
   tomorrow = new Intl.DateTimeFormat('es-CL',dateFormat).format((new Date()).getDate+1);
   var usageData{today: 20, tomorrow: 30, pastValues: [20,15,14], proyectedValues:[18,25,20], precision: 95}; //change this
   makeForm(usageData);
});

function makeForm(data){
    makeGraph(data.values);
    
    $("#divRequisition").append('<label>Hoy debes pedir</label></br>')
    $("#divRequisition").append('<label>'+ today +' : '+ usageData.today +' Quintales</label></br>')
    $("#divRequisition").append('<label>El proximo pedido debe ser</label></br>')
    $("#divRequisition").append('<label>'+ tomorrow +' : '+ usageData.tomorrow +' Quintales</label></br>')
}

function makeGraph(xValues){
    var data = {
        x:xValues,
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
    Plotly.newPlot('graph', data, layout, {displayModeBar: false});
}