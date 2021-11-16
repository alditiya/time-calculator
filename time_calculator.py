def add_time(start, duration, day_name=None):
    day_count = 0
    name_in_week = {
        1: 'Saturday',
        2: 'Sunday',
        3: 'Monday',
        4: 'Tuesday',
        5: 'Wednesday',
        6: 'Thursday',
        7: 'Friday'
    }
    start_time_list = start.split()
    hour = int(start_time_list[0].split(':')[0])
    minute = int(start_time_list[0].split(':')[1])
    time_meridian = start_time_list[1].upper()
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])
    # print(hour, minute, time_meridian)
    # print(duration_hour, duration_minute)
    if duration_hour >= 24:
        day_count = duration_hour // 24
        duration_hour = duration_hour % 24
    new_hour = hour + duration_hour
    new_minute = minute + duration_minute
    # print(new_hour, new_minute, time_meridian)
    if new_minute > 60:
        new_hour += new_minute // 60
        new_minute = new_minute % 60
    # print(new_hour, new_minute, time_meridian)
    if new_hour >= 12:
        if new_hour > 24:
            day_count += new_hour // 24
        # print(new_hour)
        if new_hour % 12 == 0:
            new_hour = 12
        else:
            new_hour %= 12
        # print(new_hour, new_minute, time_meridian)
        if time_meridian == 'AM' and (duration_hour != 24 and duration_minute != 0):
            time_meridian = 'PM'
        elif time_meridian == 'PM' and (duration_hour != 24 and duration_minute != 0):
            time_meridian = 'AM'
            day_count += 1

    # print(day_count)
    # print(new_hour, new_minute, time_meridian)

    new_time = '{:d}:{:02d} {time_meridian}'.format(new_hour, new_minute, time_meridian=time_meridian)
    if day_name:
        key = [k for k, v in name_in_week.items() if v == day_name.capitalize()][0]
        key += day_count
        if key % 7 == 0:
            key = 7
        else:
            key %= 7
        # print(key)
        new_day_name = name_in_week[key]
        new_time += f', {new_day_name}'
    if day_count != 0:
        if day_count == 1:
            new_time += ' (next day)'
        else:
            new_time += f' ({day_count} days later)'
    return new_time