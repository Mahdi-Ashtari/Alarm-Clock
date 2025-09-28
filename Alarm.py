from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel, QTextEdit , QPushButton , QSpinBox
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import sys
from datetime import datetime
import time
import pygame

class UI(QMainWindow):
    def __init__(self):
        super(UI , self).__init__()
        
        #load the ui file
        uic.loadUi("Alarm.ui" , self)

        self.spin1 = self.findChild(QSpinBox, "spinBox")
        self.spin2 = self.findChild(QSpinBox , "spinBox_2")
        self.setAlarm = self.findChild(QPushButton , "pushButton")
        self.reset = self.findChild(QPushButton , "pushButton_2")
        

        self.time = datetime.now()
        self.t1 = self.time.strftime("%H")
        self.spin1.setValue(int(self.t1))
        self.t2 = self.time.strftime("%M")
        self.spin2.setValue(int(self.t2))

        self.setAlarm.clicked.connect(self.Alarm)
        self.reset.clicked.connect(self.Stop)
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.checkAlarm)
        

        self.show()


    def checkAlarm(self):
        while True :
            Time = datetime.now()
            Hour = Time.strftime("%H")
            Minute = Time.strftime("%M")
            if (self.spin1.value() == int(Hour) and self.spin2.value() == int(Minute)):
                self.setAlarm.setText("It's Time...")
                pygame.mixer.init()
                pygame.mixer.music.load("alarm1.mp3")
                pygame.mixer.music.play()
                self.timer.stop()
                break
            else :
                continue        
        
        
    def Alarm(self):
        self.setAlarm.setText("The Alarm has set, Wait for the music...")
        self.timer.start()

                
    def Stop(self):
        pygame.mixer.music.stop()
        self.setAlarm.setText("set the Alarm")

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()