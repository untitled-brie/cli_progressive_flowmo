import time as ti
import datetime as dt
import subprocess as sp


# get current time
def get_current_time():
    now = dt.datetime.now()
    return now

def get_current_date():
    date = dt.date.today()
    return date

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
def get_break_length(session_length, ratio=0.3):
    format_ratio = float(ratio)
    break_length = session_length * format_ratio
    return break_length


def get_user_in(prompt):
    user_in = input(prompt).strip().lower()
    return user_in


def timedelta_s_to_min(timedelta):
    secs = timedelta.total_seconds()
    return secs / 60


# session end bell:
def ring_bell():
    for i in range(2):
        sp.run(["tput","bel"])
        ti.sleep(1)