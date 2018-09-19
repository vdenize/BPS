$(document).ready(function () {
    $.ajax({
        url: '/reservation/get_events/',
        dataType: 'json',
        type: 'GET',
        success: function (data) {
            $('#calendar).fullCalendar(data)
        },
    });
});