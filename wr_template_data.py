month_dict = {
    u'янв' : '1',
    u'фев' : '2',
    u'мар' : '3',
    u'апр' : '4',
    u'мая' : '5',
    u'июн' : '6',
    u'июл' : '7',
    u'авг' : '8',
    u'сен' : '9',
    u'окт' : '10',
    u'ноя' : '11',
    u'дек' : '12',
    u'jan' : '1',
    u'feb' : '2',
    u'mar' : '3',
    u'apr' : '4',
    u'may' : '5',
    u'jun' : '6',
    u'jul' : '7',
    u'aug' : '8',
    u'sep' : '9',
    u'oct' : '10',
    u'nov' : '11',
    u'dec' : '12',
}

time_re_list = [
    ur'[^\W\d][^\W\d]\s*(?P<month>[^\W\d]+)\s*(?P<day>\d{1,2}),\s*(?P<year>\d{4})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})\s*(?P<ampm>[^\W\d]{,2})$',
    ur'^[^\|]+\|\s*(?P<date>[^\W\d][^\W\d]+)\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^[^\|]+\|\s*(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<month>[^\W\d]+)\s*(?P<day>\d{1,2}),\s*(?P<year>\d{4}),\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2}):\d{2}\s*(?P<ampm>[^\W\d]{,2})',
    ur'^(?P<month>[^\W\d]+)\s*(?P<day>\d{1,2}),?\s*(?P<year>\d{4}),\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})\s*(?P<ampm>[^\W\d]{,2})',
    ur'^(?P<day>\d{1,2})[^\W\d]{,2}\s*(?P<month>[^\W\d][^\W\d]+)\s*(?P<year>\d{4}) - (?P<hours>\d{1,2}):(?P<minutes>\d{2})\s*(?P<ampm>[^\W\d]{,2})',
    ur'^от (?P<seconds_ago>\d{1,2}) секунд назад в \d{1,2}:\d{2}$',
    ur'^(?P<less_then_min>)менее минуты назад$',
    ur'^(?P<less_then_min>)меньше минуты назад$',
    ur'^позавчера (?P<day_before_yesterday>\d{1,2}:\d{2})$',
    ur'^(?P<minutes_ago>\d{1,2}) минут[у\(ы\)]* назад$',
    ur'^(?P<minutes_ago>\d{1,2}) мин\.? назад$',
    ur'^(?P<minutes_ago>\d{1,2}) Минут$',
    ur'^от (?P<minutes_ago>\d{1,2}) минут назад в \d{1,2}:\d{2}$',
    ur'^(?P<hours_ago>\d{1,2}) Часов$',
    ur'^(?P<hours_ago>\d{1,2}) час назад$',
    ur'^(?P<hours_ago>\d{1,2}) час\(?ов\)? назад$',
    ur'^(?P<hours_ago>\d{1,2}) часа назад$',
    ur'^(?P<hours_ago>\d{1,2}) ч\. назад$',
    ur'^от (?P<hours_ago>\d{1,2}) час[\.ов]* (?P<minutes_ago>\d{1,2}) минут назад в \d{1,2}:\d{2}$',
    ur'^(?P<days_ago>\d{1,2}) день назад$',
    ur'^(?P<days_ago>\d{1,2}) дн. назад$',
    ur'^(?P<weeks_ago>\d{1,2}) неделю назад$',
    ur'^(?P<weeks_ago>\d{1,2}) недель\(и\) назад$',
    ur'^[^\W\d][^\W\d]\s*(?P<month>[^\W\d]+)\s*(?P<day>\d{1,2}),\s*(?P<year>\d{4})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^[^\W\d][^\W\d]\s*(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+),\s*(?P<year>\d{4})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+),?\s*(?P<year>\d{4})\s*[,-:]?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^от (?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\s*(?P<year>\d{4}) в (?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\s*(?P<year>\d{4}) в (?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\s*(?P<year>\d{4})\s*[^\W\d]+\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\s*-?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{2,4})\s*[,-в]?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'дата/время: (?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{2,4})\s*[,-в]?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\.\s*(?P<month>\d{1,2})\.\s*(?P<year>\d{2,4}),\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2}):\d{2}',
    ur'^(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4}) г\. в (?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})-(?P<month>\d{1,2})-(?P<year>\d{2,4}),?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{2}),?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{2,4})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{2,4}),\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>\d{1,2})\s*(?P<year>\d{2,4}),\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+),?\s*(?P<year>\d{4}),?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^[^\W\d][^\W\d], (?P<day>\d{1,2})\s*(?P<month>[^\W\d]+),?\s*(?P<year>\d{4}),?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\.?,\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<hours>\d{1,2}):(?P<minutes>\d{2})\s*,?\s*(?P<day>\d{2})[\.-]?(?P<month>\d{2})[\.-]?(?P<year>\d{2,4})[ от]*',
    ur'^(?P<hours>\d{1,2}):(?P<minutes>\d{2}):\d{2},?\s*(?P<day>\d{2})\s*(?P<month>[^\W\d]+),?\s*(?P<year>\d{4})',
    ur'^(?P<date>[^\W\d]+),?\s*(?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<date>[^\W\d]+) в (?P<hours>\d{1,2}):(?P<minutes>\d{2}):\d{2}',
    ur'^(?P<date>[^\W\d]+) в (?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'(?P<date>[А-Яа-я]+) в в (?P<hours>\d{1,2}):(?P<minutes>\d{2})',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\.?\s*(?P<year>\d{4})[ г\.]*$',
    ur'^(?P<day>\d{1,2})\.(?P<month>\d{2})\.(?P<year>\d{4})$',
    ur'^(?P<day>\d{1,2})\.(?P<month>\d{2})\.(?P<year>\d{2})$',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)$',
    ur'^(?P<day>\d{1,2})\.(?P<month>\d{2})$',
    ur'^(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$',
    ur'^(?P<day>\d{1,2})-(?P<month>\d{2})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$',
    ur'(?s)^(?:(?!->).)*->\s*(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$',
    ur'(?s)^(?:(?!->).)*->\s*(?P<day>\d{1,2})-(?P<month>\d{2})\s*(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$',
    ur'^(?P<timestamp>14\d{7,9})$',
    ur'^(?P<day>\d{1,2})\s*(?P<month>[^\W\d]+)\s*(?P<year>\d{4})$',
]