#=================================LIBRARIES=========================================================================
import schedule  # reminder module
from time import time, ctime  # time in seconds, calendar time
import time
from PyQt5.QtWidgets import QMessageBox
# import pandas as pd
# import dataframe_image as dfi

#=================================FUNCTIONS=========================================================================

week = {'monday': {}, 'tuesday': {}, 'wednesday': {}, 'thursday': {}, 'friday': {}, 'saturday': {}, 'sunday': {}}


def class_warning(class_name, start_time):
    print(class_name + " class will start in 5 minutes at " + start_time)


def class_alert(class_name, end_time):
	showPopup()
    print(class_name + " class starts now and ends at " + end_time)


def add_to_schedule(event_name, event_type, days, start_time, end_time, location, host):  # days is a list of week days.
    event = {'type': event_type, 'start_time': start_time, 'end_time': end_time, 'location': location, 'host': host}
    for i in days:
        week[i][event_name] = event

        if i == "monday":  # the mechanism involved in directly scheduling class alerts
            schedule.every().monday.at(str(start_time)).do(class_alert, event_name, end_time)
        elif i == "tuesday":
            schedule.every().tuesday.at(str(start_time)).do(class_alert, event_name, end_time)
        elif i == "wednesday":
            schedule.every().wednesday.at(str(start_time)).do(class_alert, event_name, end_time)
        elif i == "thursday":
            schedule.every().thursday.at(str(start_time)).do(class_alert, event_name, end_time)
        elif i == "friday":
            schedule.every().friday.at(str(start_time)).do(class_alert, event_name, end_time)
        elif i == "saturday":
            schedule.every().saturday.at(str(start_time)).do(class_alert, event_name, end_time)
            pass
        elif i == "sunday":
            schedule.every().sunday.at(str(start_time)).do(class_alert, event_name, end_time)
