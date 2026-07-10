from timer_functions import get_current_time, get_user_in, timedelta_s_to_min
from daily_total import DailyTotal

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


def start_flow_session(daily_total_object):  # daily_total object
    session_length = count_up()

    if session_length != "session cancelled":
        daily_total_object.increase_recorded_total(session_length)
        daily_total_object.display_info()

        if daily_total_object.goal_status() is True:
            return session_length, "daily goal met"
        
        return session_length
    
    else:
        return session_length
