import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout,QHBoxLayout,QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore
import random
from PyQt5.QtCore import QTimer
from datetime import date, datetime

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.richtig = 0
        self.falsch = 0
        self.count = 0
        self.windowWid = QWidget(self)
        self.winlayout = QHBoxLayout()
        self.mainWidget = QWidget(self)
        self.winlayout.addWidget(self.mainWidget)
        self.windowWid.setLayout(self.winlayout)

        layout = QGridLayout()
        mul1l =QLabel("Zahl")
        mul2l =QLabel("Zahl")
        ergl =QLabel("Ergebnis")
        self.ergproof = QLabel()

        layout.addWidget(mul1l, 0, 0)
        layout.addWidget(mul2l, 0, 1)
        layout.addWidget(ergl, 0, 2)

        self.mul1 = QLabel()
        self.mul2 = QLabel()
        self.erg = QLineEdit()
        self.erg.setMinimumHeight(60)
        layout.addWidget(self.mul1, 1, 0)
        layout.addWidget(self.mul2, 1, 1)
        layout.addWidget(self.erg, 1, 2)
        layout.addWidget(self.ergproof, 3, 2)

        self.text = QLabel()
        layout.addWidget(self.text,4,0, 1, 3)
        self.timerLab = QLabel("Zeit:")
        layout.addWidget(self.timerLab, 5,0,1,3)
        self.mainWidget.setLayout(layout)
        self.setCentralWidget(self.windowWid)

        self.mylist = self.createList()
        self.z1 = 0
        self.z2 = 0
        self.index = 0
        self.createRandomVal()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.elapsetime = 0
        self.setMinimumSize(1000,650)
        self.file1 = open("Maxi.txt", "a+")

    def tick(self):
        self.elapsetime += 1
        self.timerLab.setText("Zeit: "+ str(self.elapsetime) + " Sekunden")
        self.timer.start(1000)

    def createRandomVal(self):
        self.erg.setText("")
        print(self.mylist.__len__())
        if self.mylist.__len__() == 0:
            self.ergproof.setText("Super, du hast alle Zahlen")
            return
        self.index = random.randrange(0, self.mylist.__len__(), 1)
        m1 = self.mylist[self.index]
        self.z1 = m1[0]
        self.z2 = m1[1]
        self.mul1.setText(str(m1[0]) + "   * ")
        self.mul2.setText(str(m1[1]) + "   = ")


    def on_click(self):
        print("push")
        self.count += 1
        if self.mylist.__len__() == 0:
            self.ergproof.setText("Super, du hast alle Zahlen")
            today = date.today()
            return
        if self.erg.text() == "":
            return
        multi = self.z1 * self.z2
        today = date.today()
        if int(self.erg.text()) == multi:
            with open('Maxi.txt', 'a') as f:
                f.write(str(today) + ": " +  str(self.elapsetime) + "s for: " + str(self.z1) + "*" + str(self.z2)
                        + "=" + self.erg.text() +" : RICHTIG\n")
            self.ergproof.setText("Richtig")
            self.richtig += 1
            del(self.mylist[self.index])
            self.createRandomVal()
        else:
            with open('Maxi.txt', 'a') as f:
                f.write(str(today) + ": " +  str(self.elapsetime) + "s for: " + str(self.z1) + "*" + str(self.z2)
                        + "=" + self.erg.text() +" : FALSCH\n")
            self.ergproof.setText("Falsch! Nochmal")
            self.erg.setText("")
            self.falsch += 1

        self.text.setText("Du hast "+ str(self.richtig) + " richtig und "+
                          str(self.falsch) + " falsch von " + str(self.count))

    def createList(self):
        l = []
        for i in range(11, 14):
            for j in range (0, 14):
                l.append([i,j])
        return l

    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.on_click()
        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    font = app.font()
    font.setPointSize(32)
    app.setFont(font)
    main = Window()
    main.show()
    sys.exit(app.exec_())

