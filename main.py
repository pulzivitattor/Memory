from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,  QGroupBox, QButtonGroup, QRadioButton,QPushButton, QLabel)
from random import shuffle, randint

class Question(): #содержит вопрос, правильный ответ и три неправильных'
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        # неправильный ответ!
        show_correct('Неверно!')
        print('Рейтинг:', (window.score/window.total*100), '%')
def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    if cur_question >= len(questions_list):
        cur_question = 0
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

questions_list = []
questions_list.append(Question('Моё любимое число?', '17', '56', '63', 'Аркадий'))
questions_list.append(Question('Какое животное мяукает?' ,'кот', 'игуана', 'крокодил', 'Алексей'))
questions_list.append(Question('Когда я родился?', '1 марта 2009 г', '24 ноября 1861 г', '5 декабря 536 г',
'трансформатор'))
questions_list.append(Question('Какая страна самая лучшая в HOI4?', 'Япония', 'СССР',
'Ян-Майен', 'Временное Правительство'))
questions_list.append(Question('Когда гуси спасли Рим?', '390 г до н.э.', '520 г до н.э',
'3250 г до н.э.', 'арбуз'))
questions_list.append(Question('Кто такой скуф?', 'мужик, не ухаживающий за собой',
'Алексей', 'Сквидвард', 'Чебурашка'))
questions_list.append(Question('Когда вышел Губка Боб?', '1 января 2000 г', '32 декабря 1375 г до н.э.',
'5 декабря 1999 г', '21 ноября 2024 г'))


app = QApplication([])
btn_OK = QPushButton('Ответить') # кнопка ответа
btn_OK.setStyleSheet('background-color: Green')
btn_OK.setFont(QFont("Verdana", 20))
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
lb_Question.setStyleSheet('background-color: Orange')
lb_Question.setFont(QFont("Verdana", 20, QFont.Bold))
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_1.setStyleSheet('font: 14pt Arial')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_2.setStyleSheet('font: 14pt Arial')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_3.setStyleSheet('font: 14pt Arial')
rbtn_4 = QRadioButton('Вариант 4')
rbtn_4.setStyleSheet('font: 14pt Arial')

RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 

AnsGroupBox = QGroupBox("Результат теста")
AnsGroupBox.setFont(QFont("Verdana", 20))
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Result.setFont(QFont("Verdana", 20))
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
lb_Correct.setFont(QFont("Verdana", 20))

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0
q = Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing')
ask(q)
btn_OK.clicked.connect(click_OK) # убрали тест, здесь нужна проверка ответа
next_question()
window.resize(600, 400)
window.show()
app.exec()
