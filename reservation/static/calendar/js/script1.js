$(document).ready(function () {
    var calendar = $('#calendar').fullCalendar({
        editable: true,
        height: 600,
        contentHeight: 400,
        defaultView: 'agendaWeek',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        eventRender: function (event, element, view) {
            if (event.allDay === 'true') {
                event.allDay = true;
            } else {
                event.allDay = false;
            }
        },
        selectable: true,
        selectHelper: true,

        events:'/reservation/get_events/',
        select: function (start, end, allDay) {
            var title = prompt('Event Title:');
            if (title) {
                var start = $.fullCalendar.formatDate(start, "Y-MM-DD HH:mm:ss");
                var end = $.fullCalendar.formatDate(end, "Y-MM-DD HH:mm:ss");
                $.ajax({
                    url: '/reservation/add_event/',
                    data: 'title=' + title + '&start=' + start + '&end=' + end,
                    success: function (json) {
                        alert('Added Successfully');
                        window.location.replace('/reservation/payment/')
                    }
                });
                calendar.fullCalendar('renderEvent',
                    {
                        title: title,
                        start: start,
                        end: end,
                        allDay: allDay
                    },
                    true
                );
            }
            calendar.fullCalendar('unselect');
        },
        editable: true,

    })
});

