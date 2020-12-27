def alarm_clock(day, vacation):
    if vacation and day == 0 or day == 6:
        return "off"
    elif (vacation and day in range(1, 6)) or (day == 0 or day == 6):
        return "10:00"
    elif day in range(1, 6):
        return "7:00"

Saturday
No Vacation
