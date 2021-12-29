import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class BasicTheory(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("C:/Users/Uchenik/Desktop/dfg/Theory_tmp.ui", self)
        self.textBrowser.setHtml("<h3>How are you?</h3>"
                                 "<br/>В русском языке мы спрашиваем "
                                 "<font size='3' color='#137CF2'><b>Как дела?</b></font>"
                                 " или <font size='3' color='#137CF2'><b>Как ты/вы?</b></font> "
                                 "В английском этот вопрос не подразумевает подробного ответа. Обычно на него отвечают"
                                 "просто <font size='3' color='#137CF2'><b>I'm fine, thanks</b></font>"
                                 "<h3>Общие фразы</h3>"
                                 "<br/>В русском мы употреюляем слово <b>пожалуйста</b> когда кого-то о чем-то просим"
                                 "или в ответ на слова благодарности. В английском <b>please</b> потребляется только с"
                                 " просьбой. Но в ответ на слова благодарногсти обычно оворят "
                                 "<font size='3' color='#137CF2'><b>You are welcome.</b></font>"
                                 "Так же <font size='3' color='#137CF2'><b>welcome</b></font> может означать "
                                 "<b>Добро пожаловать.</b>")


class IamfromTheory(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("C:/Users/Uchenik/Desktop/dfg/Theory_tmp.ui", self)
        self.textBrowser.setHtml("<h3>I am a student!</h3>"
                                 "<br/>В русском языке мы используем <b>быть</b> только в прошедшем (был/а/и)"
                                 "и будущем (буду/ет/ут), но в английском использовать "
                                 "<font size='3' color='#137CF2'><b>to be</b></font>(быть) также и в настоящем. "
                                 "По-русски мы скажем <b>Я студент</b> или <b>Он мальчик</b>, а по-английски нужно"
                                 "сказать <b>I <font size='3' color='#137CF2'>am</font> a student</b> or "
                                 "<b>He <font size='3' color='#137CF2'>is</font> a boy</b>."
                                 "Чтобы задать вопрос обязательно нужно поменять порядок слов и начать предложение с "
                                 "глагола <b>to be</b>"
                                 "<table border='1'><tr><td>I <b>am</b> a girl</td><td><b>Am</b> i a girl?</td></tr>"
                                 "<tr><td>He <b>is</b> a boy</td><td><b>Is</b> he a boy</td></tr>"
                                 "<tr><td>She <b>is</b> a woman</td><td><b>Is</b> she a woman</td></tr></table>"
                                 "Обратите внимание - форма глагола для <b>he</b> и <b>she</b> одинаковая."
                                 "<h3>I am a student!</h3>"
                                 "<br/>По-оусски мы говорим <b>я ем, ты ешь, она ест</b> и т.д. А в английском "
                                 "форма глагола меняется реже. Нужно только добавить "
                                 "<font size='3' color='#137CF2'><b>-s</b></font> когда глагол употребляется с "
                                 "местоимениями <b>he</b> и <b>she</b>.")


class LessonTmp(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("C:/Users/Uchenik/Desktop/dfg/Lesson_tmp.ui", self)
        # self.basic_btn.clicked.connect(self.window2)


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("C:/Users/Uchenik/Desktop/dfg/Duolingo2.ui", self)
        # self.basic_btn.clicked.connect(self.window2)
        self.lesson_tmp = LessonTmp()
        self.basic_theory = BasicTheory()
        self.iamfrom_theory = IamfromTheory()
        self.basic_btn.clicked.connect(self.lesson_tmp.show)
        self.basic_th.clicked.connect(self.basic_theory.show)
        self.iamfrom_th.clicked.connect(self.iamfrom_theory.show)
        # self.basic.dict = {}


    def main_window(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
