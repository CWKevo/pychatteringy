from datetime import datetime, time


def is_time_between(start: time, end: time): 
    now = datetime.now().time()

    if start < end: 
        return now >= start and now <= end 

    else:  
        return now >= start or now <= end
