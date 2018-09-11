$(document).ready(function () {
    $.ajax({
        url: '/reservation/get_events/',
        success: function (data) {

            $('#calendar').fullCalendar({
                height: 600,
                contentHeight: 600,
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month, agendaWeek, agendaDay'
                },
                events: [
                        {
                            title: data.titles,
                            start: data.starts,
                            end: data.ends
                        },

                ],

            })
        },
    });
});
