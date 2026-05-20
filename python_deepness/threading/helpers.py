from datetime import datetime

def get_timestamp():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H%M%S")
    microseconds = now.strftime("%f")

    return '[' + year + month + day + "_" + time + "_" + microseconds + '] '
