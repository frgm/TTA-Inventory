$(function() {
   var dateFormat = { year: 'numeric', month: 'short', day: '2-digit'};
   today = new Intl.DateTimeFormat('es-CL',dateFormat).format(new Date());
   var usageData{today: 20, tomorrow: 30, values: [20,15,14,18,25,20], firstday: '24-02-2018', precision: 95}
   makeForm(usageData);
});

function makeForm(data){
    
}