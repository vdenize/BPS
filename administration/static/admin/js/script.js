 $(document).ready(function(){
    alert('HI');
     $(function () {

        $('#calendar').fullCalendar({
            height : 600,
            contentHeight: 600,
            header:{
                left:'prev,next today',
                center: 'title',
                right: 'month, agendaWeek, agendaDay'
            },
            events: [
            {
                title  : 'MASS',
                start  : '2018-08-27'
            },
            {
                title  : 'Holiday',
                 start  : '2018-08-27',

            },
            ],

        })
     });
    });
