from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
class Experiment():
    def __init__(self, age, test1, test2,tset3):
        self.age = age
        self.t1 = t1 
        self.t2 = t2 
        self.t3 = t3
class TestWin(Qwidget):
    def __init__(self):
        super().__init__(self):
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_heidth)
        self.move(win_x,win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.text1 = QLabel(txt_hello)
        self.text2 = QLabel(txt_age)
        self.text3 = QLabel(txt_test1)
        self.text4 = QLabel(txt_test2)
        self.text5 = QLabel(txt_test3)
        self.text6 = QLabel(txt_timer)
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)
        self.line1 = QLineEdit(txt_hintname)
        self.line2 = QLineEdit(txt_hintage)
        self.line3 = QLineEdit(txt_hinttest1)
        self.line4 = QLineEdit(txt_hinttest2)
        self.line5 = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.text1)
        self.l_line.addWidget(self.line1)
        self.l_line.addWidget(self.text2)
        self.l_line.addWidget(self.line2)
        self.l_line.addWidget(self.text3)
        self.l_line.addWidget(self.button1)
        self.l_line.addWidget(self.line3)
        self.l_line.addWidget(self.button2)
        self.l_line.addWidget(self.text5)
        self.l_line.addWidget(self.button3)
        self.l_line.addWidget(self.line4)
        self.l_line.addWidget(self.line5)
        self.r_line.addWidget(self.text6)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.tw = FinalWin(self,exp)
        self.exp = Experiment(self.line_age.test(),self.line_test1.text(),self.line_test2.text(),self.line_atest3.text(),)
        self.hide()
    def timer_test(self):
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        time = QTime(0,1,0)
        self,timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
    def timer1Event(self):

    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
    