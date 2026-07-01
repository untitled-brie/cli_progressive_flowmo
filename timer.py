import time as ti
import datetime as dt
import subprocess as sp


timer = dt.timedelta(seconds=5)
now = dt.datetime.now()
timer_ends_at = now + timer


while now <= timer_ends_at:
    sp.call("clear")

    time_remaining = timer_ends_at - now

    print(now.time().strftime("%H:%M:%S"))
    now = dt.datetime.now()

    print(int(time_remaining.total_seconds()))

    print(timer_ends_at.time().strftime("%H:%M:%S"))
    now = dt.datetime.now()

    ti.sleep(1)

print("timer ends")
