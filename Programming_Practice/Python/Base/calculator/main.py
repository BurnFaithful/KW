import sys
import math
import operator
import enum

from PyQt5.QtWidgets import QMainWindow, QApplication

from calcwin import Ui_MainWindow


class CalcState(enum.Enum):
    WAIT = 0
    INPUT = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.state = CalcState.WAIT
        self.stack = []
        self.cur_operator = None
        self.dot_clicked = False
        self.decimal_point = 0
        self.digit = 1

        for n in range(10):
            getattr(self, f"pushButton_num{n}").pressed.connect(
                lambda value=n: self.input_number(value))

        self.pushButton_add.pressed.connect(
            lambda: self.operator(operator.add))
        self.pushButton_sub.pressed.connect(
            lambda: self.operator(operator.sub))
        self.pushButton_mul.pressed.connect(
            lambda: self.operator(operator.mul))
        self.pushButton_div.pressed.connect(
            lambda: self.operator(operator.truediv))
        self.pushButton_equal.pressed.connect(self.equal)
        self.pushButton_dot.pressed.connect(self.dot)
        self.pushButton_plusminus.pressed.connect(self.sign_toggle)

        self.pushButton_clear.pressed.connect(self.clear)
        self.pushButton_sqrt.pressed.connect(self.sqr)
        self.pushButton_pow.pressed.connect(self.pow)
        self.pushButton_inverse.pressed.connect(self.inverse)

        self.show()

    def input_number(self, value):
        if self.state == CalcState.WAIT:
            self.state = CalcState.INPUT
            self.stack.append(value)
        else:
            if not self.dot_clicked:
                self.stack[-1] = self.stack[-1] * 10 + value
            else:
                self.digit *= 0.1
                self.decimal_point += value * self.digit
                self.stack[-1] = self.stack[-1] + self.decimal_point

        self.lineEdit_display.setText(str(self.stack[-1]))

    def operator(self, op):
        if self.state == CalcState.INPUT:
            self.state = CalcState.WAIT
            self.cur_operator = op

    def equal(self):
        if self.cur_operator and len(self.stack) == 2:
            right = self.stack.pop()
            left = self.stack.pop()
            self.stack.append(self.cur_operator(left, right))
            self.lineEdit_display.setText(str(self.stack[-1]))

    def clear(self):
        self.state = CalcState.WAIT
        self.cur_operator = None
        self.dot_clicked = False
        self.decimal_point = 0
        self.digit = 1
        self.stack.clear()
        self.lineEdit_display.setText('0')

    def sqr(self):
        if self.state == CalcState.INPUT:
            self.stack[-1] = math.sqrt(self.stack[-1])
            self.lineEdit_display.setText(str(self.stack[-1]))

    def pow(self):
        if self.state == CalcState.INPUT:
            self.stack[-1] = self.stack[-1] * self.stack[-1]
            self.lineEdit_display.setText(str(self.stack[-1]))

    def inverse(self):
        if self.state == CalcState.INPUT:
            self.stack[-1] = 1 / self.stack[-1]
            self.lineEdit_display.setText(str(self.stack[-1]))

    def sign_toggle(self):
        if self.state == CalcState.INPUT:
            self.stack[-1] = -self.stack[-1]
            self.lineEdit_display.setText(str(self.stack[-1]))

    def dot(self):
        if self.state == CalcState.INPUT:
            self.dot_clicked = True
            self.lineEdit_display.setText(str(self.stack[-1]) + ".")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("계산기")

    window = MainWindow()
    sys.exit(app.exec_())
