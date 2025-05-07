class TestWin(Qwidget):
    def __init__(self):
        super().__init__(self):
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        pass
    def initUI(self):
        self.h_line = 
        self.r_line = 
        self.l_line = 
        self.text1 = QLabel(txt_hello)
        self.text2 = QLabel(txt_age)
        self.text3 = QLabel(txt_test1)
        self.text4 = QLabel(txt_test2)
        self.text5 = QLabel(txt_test3)
        self.text6 = QLabel()
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)
        self.line1 = QLineEdit(txt_hintname)
        self.line2 = QLineEdit(txt_hintage)
        self.line3 = QLineEdit(txt_hinttest1)
        self.line4 = QLineEdit(txt_hinttest2)
        self.line5 = QLineEdit(txt_hinttest3)
    def connects(self):


class Finalwin(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()

        self.show()
    def set_appear(self):
        pass
    def initUI(self):
        self.text7 = QLabel()
        self.text8 = QLabel()
        