class Finalwin(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_heidth)
        self.move(win_x,win_y)
    def initUI(self):
        self.l_line = QVBoxLayout()
        self.text7 = QLabel(txt_workheart)
        self.text8 = QLabel(txt_index)
        self.l_line.addWidget(self.text7)
        self.l_line.addWidget(self.text8)
        self.setLayout(self.l_line)