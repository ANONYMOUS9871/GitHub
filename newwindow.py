#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget
import random
 
#declaring constants
win_width, win_height = 800, 300
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "Entry field"
 
class NewWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.questions_list = []
        self.questions_dict = dict()
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
        #determines how the window will look (text, size, location)
        self.set_appear()
        # start:
        self.show()
 
 
    def initUI(self):
        ''' creates graphical elements '''
        self.lable_intrebare = QLabel("Intrebare")
        questions = QVBoxLayout()
        self.r1 = QPushButton("Raspunsul 1")
        self.r2 = QPushButton("Raspunsul 2")
        self.r3 = QPushButton("Raspunsul 3")
        self.r4 = QPushButton("Raspunsul 4")
        questions.addWidget(self.lable_intrebare)
        questions.addWidget(self.r1)
        questions.addWidget(self.r2)
        questions.addWidget(self.r3)
        questions.addWidget(self.r4)
        self.setLayout(questions)
 
 
    def set_questions(self,questions):
        self.questions_dict = questions
        self.questions_list = list(self.questions_dict.keys())
        self.changeQuestion()
 
 
    def changeQuestion(self):
        if len(self.questions_list) > 1:
            self.currenct_question = random.choice(self.questions_list) #alegere random
            self.questions_list.remove(self.currenct_question)
        elif len(self.questions_list) == 1:
            self.currenct_question = self.questions_list.pop(0)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setText("You have no more questions !!")
            msg.exec_()
            return 0
        # question = self.questions_list[0] # aceeasi ordine tot timpul
 
 
 
        self.lable_intrebare.setText(self.currenct_question) #alegere random
        answer_dict = self.questions_dict[self.currenct_question]
        self.r1.setText(answer_dict['answer'])
        self.r2.setText(answer_dict['answer_g1'])
        self.r3.setText(answer_dict['answer_g2'])
        self.r4.setText(answer_dict['answer_g3'])
 
 
    def check_answer(self, bt):
        answer_dict = self.questions_dict[self.currenct_question]
        msg = QMessageBox()
        msg.setWindowTitle("Your answer is:")
 
        print(bt.text(),'==',self.questions_dict[self.currenct_question]['answer'] )
        if bt.text() == self.questions_dict[self.currenct_question]['answer']:
            msg.setText("Correct !!")
        else:
            msg.setText("Wrong !!")
        msg.exec_()
        self.changeQuestion()
 
    def bt_1(self):
        self.check_answer(self.r1)
    def bt_2(self):
        self.check_answer(self.r2)
    def bt_3(self):
        self.check_answer(self.r3)
    def bt_4(self):
        self.check_answer(self.r4)
 
 
    def connects(self):
        self.r1.clicked.connect(self.bt_1)
        self.r2.clicked.connect(self.bt_2)
        self.r3.clicked.connect(self.bt_3)
        self.r4.clicked.connect(self.bt_4)
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
if __name__ == "__main__":
    app = QApplication([])
    mw = SeccondWindow()
    app.exec_()

