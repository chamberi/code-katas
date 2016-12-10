"""This module contains the function that produces the Fizz Buzz Cuckoo Clock function."""


def fizz_buzz_cuckoo_clock(time):
    """The clock function produces Fizz Buzz Cuckoo combinations at the right time."""
    hour_list = []
    if len(time) == 4:
        hour = int(time[:1])
        min = int(time[2:])
    else:
        hour = int(time[:2])
        min = int(time[3:])
    if hour > 12:
        hour -= 12
    if min == 0:
        if hour == 0:
            hour = 12
        for i in range(hour - 1):
            hour_list.append("Cuckoo ")
        hour_list.append("Cuckoo")
        a = "".join(hour_list)
        return a
    elif min == 30:
        return "Cuckoo"
    elif min % 5 == 0 and min % 3 == 0:
        return "Fizz Buzz"
    elif min % 3 == 0:
        return"Fizz"
    elif min % 5 == 0:
        return "Buzz"
    else:
        return "tick"
