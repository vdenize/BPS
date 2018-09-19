$(document).ready(function () {
    let get_events_json;

    function get_all_events() {
        $.ajax({
            url: '/reservation/get_events',
            type: 'GET',
            dataType: 'json',
            success: function (json) {
                get_events_json = json;
            }
        });
    };
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
        events: get_all_events()
        ,
        eventRender: function (event, element, view) {
            if (event.allDay === 'true') {
                event.allDay = true;
            } else {
                event.allDay = false;
            }
        },
        selectable: true,
        selectHelper: true,
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
        eventClick: function (Event) {
            var decision = confirm("Do you really want to do that?");
            if (decision) {
                $.ajax({
                    url: "/reservation/del_event/",
                    data: "&title=" + Event.title,
                    success: function (json) {
                        $('#calendar').fullCalendar('removeEvents', Event.title);
                        alert("Delete Successfully");
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
    })
});

