$(document).ready(function() {
    if($("#id_room").value != "") {
        alert('SET');
    }
    $("#id_room").change(function() {
        alert('CHANGE');
    });
});