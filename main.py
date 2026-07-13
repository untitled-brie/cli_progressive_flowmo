from count_up import start_flow_session
from i_o import start_up_read


# -------------------------------------
def draw_main_menu(daily_goal_met_status):
    program_name = "progressive flowmodoro"
    status = daily_goal_met_status # display  goal met today or nah
    start_main_menu = "[1] start flow \n[2] exit program"
    print(program_name)
    print(start_main_menu)
