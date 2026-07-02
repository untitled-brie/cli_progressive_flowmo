import time as ti
import datetime as dt
import subprocess as sp


# get current time
def get_current_time():
    now = dt.datetime.now()
    return now


# set session length
def set_session_length(minute_in):
    format_min = float(minute_in)
    session_length = dt.timedelta(minutes=format_min)
    return session_length


# return session end time
def session_ends(time_start, session_length):
    timer_ends_at = time_start + session_length
    return timer_ends_at


# return break time length
def get_break_length(ratio, session_length):
    format_ratio = float(ratio)
    break_length = session_length * format_ratio
    return break_length

# run the timer
def run_timer_session(minute, status):

    # initialize session
    now = get_current_time()
    session_length = set_session_length(minute)    # minutes 
    session_end_time = session_ends(now, session_length)
    status_string = status

    # session loop
    while now <= session_end_time:
        sp.call("clear")

        # print status string
        print("-" * len(status_string))
        print(status_string)
        print("-" * len(status_string))

        time_remaining = session_end_time - now

        print("current time: ")
        print(now.time().strftime("%H:%M:%S"))
        print("")
        now = dt.datetime.now()

        print(f"{int(time_remaining.total_seconds())} secs left")
        print("")

        print("end time: ")
        print(session_end_time.time().strftime("%H:%M:%S"))
        
        # update current time
        now = dt.datetime.now()

        # pause
        ti.sleep(1)


# program
def work_break_loop():
    work_session_length = 0.2
    break_session_length = get_break_length(0.3, work_session_length)

    run_timer_session(work_session_length, "focus time")
    run_timer_session(break_session_length, "break time")


work_break_loop()