from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from design import Ui_MainWindow  # importing our generated file

import sys
import flash
import schedule  # reminder module
from time import time, ctime  # time in seconds, calendar time
import time
import pandas as pd
import dataframe_image as dfi
import xlrd
import os
import subprocess
import integral
from datetime import datetime
import re
import fitz
from pyqt5_material import apply_stylesheet
from fuzzywuzzy import process
import re


week = {'monday': {}, 'tuesday': {}, 'wednesday': {}, 'thursday': {}, 'friday': {}, 'saturday': {}, 'sunday': {}}
# This variable is used to hold a dictionary that is used to interface between the excel file and gui


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('WHITEBOARD ~ The better blackboard')

        #---------------THIS CODE BLOCK SETS UP THE BUTTONS TO GO BACK AND FORTH BETWEEN PAGES-------------------
        self.addCoursesB.clicked.connect(self.openScheduleGen)
        self.dashboardB.clicked.connect(self.openDashboard)
        #-----------------------THIS CODE BLOCK LOADS UP LABELS WITH SCHEDULE IMAGES------------------------------
        w = self.scheduleLabel.width()
        h = self.scheduleLabel.height()
        self.scheduleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scheduleLabel.setText("")

        self.monB.clicked.connect(lambda: self.changeDay("./Weekdays/monday.png"))
        self.tueB.clicked.connect(lambda: self.changeDay("./Weekdays/tuesday.png"))
        self.wedB.clicked.connect(lambda: self.changeDay("./Weekdays/wednesday.png"))
        self.thuB.clicked.connect(lambda: self.changeDay("./Weekdays/thursday.png"))
        self.friB.clicked.connect(lambda: self.changeDay("./Weekdays/friday.png"))
        self.satB.clicked.connect(lambda: self.changeDay("./Weekdays/saturday.png"))
        self.sunB.clicked.connect(lambda: self.changeDay("./Weekdays/sunday.png"))
        #---------------------------SETS UP THE FLASH CARD TAB BUTTONS AND LABELS-----------------------------------
        self.cardLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.setCardText()
        self.flipCardB.clicked.connect(lambda: self.cardFlipEvent())
        self.shuffleDeckB.clicked.connect(lambda: self.shuffleEvent())
        self.rightCardB.clicked.connect(lambda: self.changeCardEvent(1))
        self.leftCardB.clicked.connect(lambda: self.changeCardEvent(-1))
        #----------------------------SETS UP THE INTEGRAL CALCULATOR WIDGETS--------------------------------------
        self.basicFormComboBox.addItems(integral.basic_forms.keys())

        self.calcB.clicked.connect(lambda: self.calculateEvent())
        self.scheduleEditB.clicked.connect(lambda: self.openFile("./schedule.xlsx"))
        self.flashCardEditB.clicked.connect(lambda: self.openFile("./Flash_Cards.txt"))
        #-------------------------------SETS UP CALENDAR WIDGET'S BUTTONS-------------------------------------------
        date = self.calendarWidget.selectedDate()
        self.updateTODOEvent()

        self.calendarWidget.clicked[QtCore.QDate].connect(lambda: self.updateTODOEvent())
        self.calEditB.clicked.connect(lambda: self.openFile("./TODO.txt"))
        #----------------------------SETTING UP A TIMER FOR THE ALERT SYSTEM---------------------------------------
        self.generate()

        # creating a timer object
        timer = QtCore.QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.run_scheduler)

        # update the timer every second
        timer.start(1000)

        for button in [self.monB, self.tueB, self.wedB, self.thuB, self.friB, self.satB, self.sunB]:
            button.setCheckable(True)  # make weekday buttons togglable

        self.stackedWidget.setCurrentIndex(0)  # open up the application on the dashboard
        #-----------------------------------------------------------------------------------------------------------------------

    #--------------THE CODE BELOW IS USED TO SWITCH BETWEEN THE DASHBOARD AND SCHEDULE GENERATOR---------------------------

    def openScheduleGen(self):
        self.stackedWidget.setCurrentIndex(1)

    def openDashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def changeDay(self, day):
        w = self.scheduleLabel.width()
        h = self.scheduleLabel.height()
        self.scheduleLabel.setPixmap(QtGui.QPixmap(day).scaled(w, h, QtCore.Qt.KeepAspectRatio))
        self.scheduleLabel.setAlignment(QtCore.Qt.AlignCenter)

        #-------------------------setting toggle behaviour for weekday buttons---------------------------
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        for i, button in enumerate([self.monB, self.tueB, self.wedB, self.thuB, self.friB, self.satB, self.sunB]):
            if button.isChecked() and i is not days.index(day.replace("./Weekdays/", "")[:-4]):
                button.toggle()
    #----------------------------------------THE CODE BELOW IS USED FOR SENDING DESKTOP NOTIFICATIONS----------------------------------
    # this function changes standard time to military time

    def standard_to_military(self, standard_time):
        military_time = datetime.strptime(standard_time, '%I:%M %p')
        parse_list = str(military_time).split(" ")
        return (parse_list[1])[0:5]

    # this function changes military time to standard time
    def military_to_standard(self, military_time):
        standard_time = datetime.strptime(military_time, "%H:%M")
        standard_time = standard_time.strftime('%I:%H:%M %p')
        if str(standard_time)[0] == "0":
            return str(standard_time)[1:3] + str(standard_time)[6:11]
        else:
            return str(standard_time)[0:3] + str(standard_time)[6:11]

    # this function generates the images and populates the "week" dictionary for the app after reading from the excel file
    def generate(self):
        schedule_file = 'schedule.xlsx'  # excel file containing user's schedule
        schedule_data = pd.read_excel(schedule_file)  # turning the excel file into a dataframe for processing

        for i in range(len(schedule_data)):  # This whole section of code is used to process the dataframe and add it to the week dictionary
            days = schedule_data['Days'][i].replace(' ', '').split(',')

            self.add_to_schedule(schedule_data['Event'][i], schedule_data['Type'][i], days, self.standard_to_military(schedule_data['Start'][i]),
                                 schedule_data['End'][i], schedule_data['Location'][i], schedule_data['Host'][i])

        for i in week:
            if len(week[i]) != 0:
                daily_schedule = pd.DataFrame(week[i])
                daily_schedule_styled = daily_schedule.transpose().style.set_properties(**{'background-color': 'grey',
                                                                                           'color': 'white',
                                                                                           'border-color': 'grey'})
                dfi.export(daily_schedule_styled, "./Weekdays/" + i + '.png')

    # this function is used to alert the user when a class is about to start
    def class_alert(self, class_name, end_time):
        msg = QMessageBox()
        msg.setWindowTitle("ALERT")
        msg.setText(class_name + " class starts now and ends at " + end_time)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
        print(class_name + " class starts now and ends at " + end_time)

    # this function initializes the scheduler to run at a specific time
    def add_to_schedule(self, event_name, event_type, days, start_time, end_time, location, host):  # days is a list of week days.
        standard_start_time = self.military_to_standard(start_time)
        event = {'Course Type': event_type, 'Start Time': standard_start_time, 'End Time': end_time, 'Location': location, 'Professor': host}

        for i in days:
            week[i][event_name] = event

            if i == "monday":  # the mechanism involved in directly scheduling class alerts
                schedule.every().monday.at(str(start_time)).do(self.class_alert, event_name, end_time)
            elif i == "tuesday":
                schedule.every().tuesday.at(str(start_time)).do(self.class_alert, event_name, end_time)
            elif i == "wednesday":
                schedule.every().wednesday.at(str(start_time)).do(self.class_alert, event_name, end_time)
            elif i == "thursday":
                schedule.every().thursday.at(str(start_time)).do(self.class_alert, event_name, end_time)
            elif i == "friday":
                schedule.every().friday.at(str(start_time)).do(self.class_alert, event_name, end_time)
            elif i == "saturday":
                schedule.every().saturday.at(str(start_time)).do(self.class_alert, event_name, end_time)
                pass
            elif i == "sunday":
                schedule.every().sunday.at(str(start_time)).do(self.class_alert, event_name, end_time)

    # this function runs the initialized scheduler
    def run_scheduler(self):
        schedule.run_pending()

    #---------------------------------------THE CODE BELOW IS USED FOR THE FLASH CARD SYSTEM-----------------------------------------
    # this event is called when the card flip button is clicked
    def cardFlipEvent(self):
        flash.card_flip(flash.card_toggle, flash.screen_card, flash.card_count, flash.prompt_list, flash.answer_list)
        self.setCardText()

    # this event is called when the deck shuffle button is clicked
    def shuffleEvent(self):
        flash.shuffle(flash.prompt_list, flash.answer_list, flash.current_prompt, flash.current_answer)
        flash.refresh(flash.prompt_list, flash.answer_list, flash.current_prompt, flash.current_answer, flash.card_toggle, flash.screen_card, flash.card_count)
        self.setCardText()

    # this event is called when the user wants to navigate the card deck
    def changeCardEvent(self, direction):
        if direction == 1:
            flash.next_card(flash.card_count, flash.card_toggle, flash.screen_card, flash.prompt_list)
            self.setCardText()
        else:
            flash.prev_card(flash.card_count, flash.card_toggle, flash.screen_card, flash.prompt_list)
            self.setCardText()

    # this function returns the text of the current card that is to be shown on the screen
    def getScreenCard(self):
        return flash.screen_card[0]

    # this function retrieves the position of the current card that is to be shown on the screen
    def getCardPosition(self):
        return str(flash.card_count[0] + 1) + " of " + str(flash.deck_length)

    # this function is called in each event to format the text shown on the screen
    def setCardText(self):
        text = """ <div>
 <div>
    <h1><b>{}</b></h1>
    <br> </br>
    <br> </br>
    <br> </br>
    <h3>(Card {})</h3>
  </div>
</div>
""".format(self.getScreenCard(), self.getCardPosition())
        self.cardLabel.setText(text)

    #---------------------------------------THE CODE BELOW IS USED FOR THE INTEGRAL CALCLUATOR-----------------------------------------
    # this event is used to handle the calculations and display for the integral calculator
    def calculateEvent(self):
        if self.integralLineEdit.text() == "":
            self.integralLineEdit.setText("Empty Value Not Allowed (please type a number)")
            self.integralLineEdit.setFocus()
        elif self.integralLineEdit.text().isnumeric():
            bf = self.basicFormComboBox.currentText()
            n = float(self.integralLineEdit.text())
            self.answerLabel.setText(integral.basic_forms[bf](n))
            self.answerLabel.setStyleSheet("QLabel{color:blue}")
        else:
            self.integralLineEdit.setText("Invalid Input")
            self.integralLineEdit.setFocus()

    #---------------------------------------THE CODE BELOW IS USED TO OPEN EDITORS-----------------------------------------
    # this function is used to open up the default editor for excel and txt files of any operating system
    def openFile(self, file):
        if sys.platform.startswith('linux'):
            print("linux")
            subprocess.call(["xdg-open", file])
        else:
            os.startfile(file)

    #---------------------------------------THE CODE BELOW IS USED TO FOR THE CALENDAR TAB-----------------------------------------
    # this event is called everytime a day is pressed in the calendar to display the todo list for that day
    def updateTODOEvent(self):
        # Open a file: file
        file = open('TODO.txt', mode='r')
        # read all lines at once
        all_of_it = file.read()
        # close the file
        file.close()
        selected_date = self.calendarWidget.selectedDate().toString("MM/dd/yyyy")
        self.todoCalendarLabel.setText("TODO LIST FOR " + selected_date)
        for i in all_of_it.split("@"):
            if bool(re.search(selected_date, i)):
                self.todoCalendarLabel.setText("TODO LIST FOR " + i)

    #-----------------------THE CODE BELOW IS USED TO FOR SCHEDULE GENERATION [WILL BE RELEASED IN NEXT UPDATE]---------------------------------
    # utility function used to split a string with delimeter while including the delimeter
    # def split_and_keep(self, string, sep):
    #     begin = 0
    #     while (end := string.find(sep, start) + 1) > 0:
    #         yield string[start:end]
    #         begin = end
    #     yield string[begin:]

    # def extractCourseInfo(self):
    #     doc = fitz.open("winter_2021_ugrd_timetable.pdf")

    #     searchTerm = "GENG-2200"
    #     num = 0
    #     for page in doc:
    #         text = page.searchFor(searchTerm)
    #         if len(text) != 0:
    #             num = page.number
    #             print(num)

    #     results = []
    #     for tupl in doc[num].getTextBlocks():
    #         results.append([element for element in tupl if isinstance(element, str)][0])

    #     strings_of_results = [e[0] for e in process.extract(searchTerm, results)]

    #     final_string_of_results = []
    #     for string in strings_of_results:
    #         if bool(re.search(searchTerm, string)):
    #             final_string_of_results.append(list(self.split_and_keep(string, "\nSection")))

    #     for e in final_string_of_results:
    #         e[0] = e[0].replace("\n", " ")

    #     return final_string_of_results


#---------------------------RUNNING THE MAIN CODE---------------------------
app = QtWidgets.QApplication([])

application = Main()

application.show()
apply_stylesheet(app, theme="light_blue.xml")

sys.exit(app.exec())

print()
