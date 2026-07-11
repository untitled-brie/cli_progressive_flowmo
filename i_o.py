import datetime as dt
from timer_functions import get_current_date
from daily_total import DailyTotal

IO_totals_file = "totals.csv"

def init_first_session():
    date = get_current_date()
    recorded_total = 0.0
    goal_total = 60.0
    met_goal = False
    line = f"{date},{recorded_total},{goal_total},{met_goal}"
    with open(IO_totals_file, "w") as f:
        f.write(line)


def read_recent_daily_to_object():
    with open(IO_totals_file, "r") as f:
        last_session = f.readline()

        if last_session == "":
            init_first_session()
            last_session = f.readline()

        fields = last_session.split(",")
        date = dt.date.fromisoformat(fields[0])
        recorded_total = float(fields[1])
        goal_total = float(fields[2])

        met_goal = fields[3]
        if met_goal == "True":
            met_goal = True
        else:
            met_goal = False

        recent_daily_object = DailyTotal(date, recorded_total, goal_total, met_goal)
        return recent_daily_object
