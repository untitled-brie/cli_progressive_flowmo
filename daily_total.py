import datetime as dt

# class to record daily totals across days and sessions
class DailyTotal:
    def __init__(self, date, recorded_total, goal_total) -> None:
        self.__date = date
        self.__recorded_total = recorded_total  #float # minutes
        self.__goal_total = goal_total  # minutes 

    # getters
    def get_date(self):
        return self.__date
    def get_recorded_total(self):
        return self.__recorded_total
    def get_goal_total(self):
        return self.__goal_total

    # setters
    def set_recorded_total(self, recorded_total):
        self.__recorded_total = recorded_total
    def increase_recorded_total(self, session_length):
        self.__recorded_total += session_length
    def set_goal_total(self, goal_total):
        self.__goal_total = goal_total

    # methods
    def display_info(self):
        print(self.__date, self.__recorded_total, self.__goal_total)

    # get goal status (true=met, false=unmet)
    def goal_status(self):
        if self.__recorded_total >= self.__goal_total:
            return True
        else:
            return False 
        
    # check if the DailyTotal is today (true=yes, false=no)
    def is_today(self):
        if self.__date == dt.date.today():
            return True
        else:
            return False

