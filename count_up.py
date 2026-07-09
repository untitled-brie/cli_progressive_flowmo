import time as ti
from timer_functions import get_current_time, get_user_in, timedelta_s_to_min

# start count up and return session length upon ending
def count_up():
    start_time = get_current_time()

    while True:
        end_input = get_user_in("[end] or [cancel] to stop flow: ")
        options = ["end", "cancel"]

        if end_input == options[0]:
            end_time = get_current_time()
            session_length = end_time - start_time
            session_length = timedelta_s_to_min(session_length)
            return session_length

        if end_input == options[1]:
            return "session cancelled"


print(count_up())



