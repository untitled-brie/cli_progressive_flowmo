from timer_functions import *
import time as ti
import datetime as dt
from count_up import *


def break_count_down(flow_ses_length):      # minutes
    print("break time!")
    # time stamp at break start
    start_break_time  = get_current_time()   # dt
    # timedelta (break length), float
    break_length_min = get_break_length(flow_ses_length)    # default ratio 0.3
    break_length_tdt = dt.timedelta(minutes=break_length_min)
    # end time (now + break ti delta)
    end_break_time = start_break_time + break_length_tdt

    now = get_current_time()

    while now < end_break_time:
        now = get_current_time()
        ti.sleep(0.1)

    ring_bell()