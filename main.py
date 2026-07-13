from count_up import start_flow_session
from daily_total import DailyTotal
from break_count_down import break_count_down
from i_o import start_up_read, write_daily_object_to_file
from timer_functions import get_user_in
import subprocess as sp
# -------------------------------------
def clear_UI():
    sp.call("clear")


def draw_main_menu(session_daily_object:DailyTotal, daily_goal_met_status):
    program_name = "progressive flowmodoro"
    progress = session_daily_object.calculate_progress()
    status = daily_goal_met_status # display  goal met today or nah
    if status == True:
        status = "Goal already met today"
    else:
        status = "Goal haven't been met today"
    start_main_menu = "[1] start flow \n[2] exit program"
    print(program_name)
    print(progress)
    print(status)
    print(start_main_menu)


def draw_break_menu(variant):
    if variant == "pre_break":
        menu = "[1] start break \n[2] exit program"
        print("time to take a break!")
        print(menu)
    if variant == "post_break":
        menu = "[1] end break \n[2] exit program"
        print("break ended, time to get back to work!")
        print(menu)


def main():
    while True:
        clear_UI()
        session_daily_object, goal_status = start_up_read()

        draw_main_menu(session_daily_object, goal_status)
        choice = get_user_in(">>> ")
        if choice in "2":
            write_daily_object_to_file(session_daily_object)
            clear_UI()
            break
        
        if choice in "1":
            clear_UI()
            flow_session_status = start_flow_session(session_daily_object)
            if flow_session_status is None:
                continue
            else:
                clear_UI()
                write_daily_object_to_file(flow_session_status[0])
                draw_break_menu("pre_break")
                choice = get_user_in(">>> ")
                if choice in "2":
                    clear_UI()
                    break
                elif choice in "1":
                    clear_UI()
                    break_count_down(flow_session_status[1])
                    draw_break_menu("post_break")
                    choice = get_user_in(">>> ")
                    if choice in "2":
                        clear_UI()
                        break
                    else:
                        continue


main()