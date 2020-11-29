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

import integral


week = {'monday': {}, 'tuesday': {}, 'wednesday': {}, 'thursday': {}, 'friday': {}, 'saturday': {}, 'sunday': {}}

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.addCoursesB.clicked.connect(self.openScheduleGen)
        self.dashboardB.clicked.connect(self.openDashboard)

        w = self.scheduleLabel.width()
        h = self.scheduleLabel.height()
        self.scheduleLabel.setPixmap(QtGui.QPixmap("./Weekdays/monday.png").scaled(w, h, QtCore.Qt.KeepAspectRatio))
        self.scheduleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.monB.clicked.connect(lambda: self.changeDay("./Weekdays/monday.png"))
        self.tueB.clicked.connect(lambda: self.changeDay("./Weekdays/tuesday.png"))
        self.wedB.clicked.connect(lambda: self.changeDay("./Weekdays/wednesday.png"))
        self.thuB.clicked.connect(lambda: self.changeDay("./Weekdays/thursday.png"))
        self.friB.clicked.connect(lambda: self.changeDay("./Weekdays/friday.png"))
        self.satB.clicked.connect(lambda: self.changeDay("./Weekdays/saturday.png"))
        self.sunB.clicked.connect(lambda: self.changeDay("./Weekdays/sunday.png"))

        self.cardLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.setCardText()
        self.flipCardB.clicked.connect(lambda: self.cardFlipEvent())
        self.shuffleDeckB.clicked.connect(lambda: self.shuffleEvent())
        self.rightCardB.clicked.connect(lambda: self.changeCardEvent(1))
        self.leftCardB.clicked.connect(lambda: self.changeCardEvent(-1))

        self.generate()

        # creating a timer object
        timer = QtCore.QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.run_scheduler)

        # update the timer every second
        timer.start(1000)

        for button in [self.monB, self.tueB, self.wedB, self.thuB, self.friB, self.satB, self.sunB]:
            button.setCheckable(True)

        self.stackedWidget.setCurrentIndex(0)

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
    #----------------------------------------THE CODE BELOW IS USED FOR DESKTOP NOTIFICATIONS----------------------------------

    def generate(self):
        schedule_file = 'schedule.xlsx'  # excel file containing user's schedule
        schedule_data = pd.read_excel(schedule_file)  # turning the excel file into a dataframe for processing

        for i in range(len(schedule_data)):  # This whole section of code is used to process the dataframe and add it to the week dictionary
            days = schedule_data['Days'][i].replace(' ', '').split(',')
            # print(days)
            self.add_to_schedule(schedule_data['Event'][i], schedule_data['Type'][i], days, schedule_data['Start'][i],
                                 schedule_data['End'][i], schedule_data['Location'][i], schedule_data['Host'][i])

        for i in week:
            if len(week[i]) != 0:
                daily_schedule = pd.DataFrame(week[i])
                daily_schedule_styled = daily_schedule.transpose().style.set_properties(**{'background-color': 'white',
                                                                                           'color': 'black',
                                                                                           'border-color': 'black'})
                dfi.export(daily_schedule_styled, "./Weekdays/" + i + '.png')

    def class_alert(self, class_name, end_time):
        msg = QMessageBox()
        msg.setWindowTitle("ALERT")
        msg.setText(class_name + " class starts now and ends at " + end_time)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
        print(class_name + " class starts now and ends at " + end_time)

    def add_to_schedule(self, event_name, event_type, days, start_time, end_time, location, host):  # days is a list of week days.
        event = {'Course Type': event_type, 'Start Time': start_time, 'End Time': end_time, 'Location': location, 'Professor': host}
        # event = {'type': event_type, 'start_time': start_time, 'end_time': end_time, 'location': location, 'host': host}
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

    def run_scheduler(self):
        schedule.run_pending()

    #---------------------------------------THE CODE BELOW IS USED FOR THE FLASH CARD SYSTEM-----------------------------------------
    def cardFlipEvent(self):
        flash.card_flip(flash.card_toggle, flash.screen_card, flash.card_count, flash.prompt_list, flash.answer_list)
        self.setCardText()

    def shuffleEvent(self):
        flash.shuffle(flash.prompt_list, flash.answer_list, flash.current_prompt, flash.current_answer)
        flash.refresh(flash.prompt_list, flash.answer_list, flash.current_prompt, flash.current_answer, flash.card_toggle, flash.screen_card, flash.card_count)
        self.setCardText()

    def changeCardEvent(self, direction):
        if direction == 1:
            flash.next_card(flash.card_count, flash.card_toggle, flash.screen_card, flash.prompt_list)
            self.setCardText()
        else:
            flash.prev_card(flash.card_count, flash.card_toggle, flash.screen_card, flash.prompt_list)
            self.setCardText()

    def getScreenCard(self):
        return flash.screen_card[0]

    def getCardPosition(self):
        return str(flash.card_count[0] + 1) + " of " + str(flash.deck_length)

    def setCardText(self):
        text = """ <div>
 <div>
    <h1><b>{} </b></h1>
    <br> </br>
    <br> </br>
    <br> </br>
    <h3>(Card {})</h3>
  </div>
</div> 
""".format(self.getScreenCard(), self.getCardPosition())
        self.cardLabel.setText(text)


#---------------------------RUNNING THE MAIN CODE---------------------------
app = QtWidgets.QApplication([])

application = Main()

application.show()

sys.exit(app.exec())

print()
