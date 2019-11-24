from PySide2 import QtWidgets
import sys
import math
import sys,os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.show()

        self.first_value = None
        self.second_value = None
        self.result = None
        self.example = ""
        self.equal = ""

    def digit_pressed(self):
        # sender - функция, которая возвращает отправителя сигнала (какая кнопка была нажата, от какой идет сигнал)
        button = self.sender()
        if self.lineEdit.text() == '0':
            self.lineEdit.setText(button.text())
        else:
            if self.result == self.lineEdit.text():
                self.lineEdit.setText(button.text())
            else:
                self.lineEdit.setText(self.lineEdit.text() + button.text())
        self.result = 0

    def form_result(self):
        self.result = str(self.result)
        if self.result[-2:] == '.0':
            self.result = self.result[:-2]
        self.lineEdit.setText(str(self.result))
        self.label.clear()

    def make_fractional(self):
        value = self.lineEdit.text()
        if '.' not in value:
            self.lineEdit.setText(value + '.')

    def function_delete(self):
        value = self.lineEdit.text()
        self.lineEdit.setText(value[:-1])

    def function_clear(self):
        self.lineEdit.setText('0')

    def pressed_equal(self):
        button = self.sender()
        self.first_value = float(self.lineEdit.text())
        self.lineEdit.clear()
        self.label.setText(str(self.first_value) + button.text())
        self.equal = button.text()

    def function_addition(self):
        self.determinate_second_value()
        self.result = float(self.first_value + self.second_value)
        self.form_result()

    def function_subtraction(self):
        self.determinate_second_value()
        self.result = float(self.first_value - self.second_value)
        self.form_result()

    def function_divison(self):
        self.determinate_second_value()
        self.result = float(self.first_value / self.second_value)
        self.form_result()

    def function_multiply(self):
        self.determinate_second_value()
        self.result = float(self.first_value * self.second_value)
        self.form_result()

    def function_exponentiation(self):
        self.determinate_second_value()
        self.result = float(self.first_value ** self.second_value)
        self.form_result()

    def function_percent(self):
        self.determinate_second_value()
        self.result = float(self.first_value * (self.second_value / 100))
        self.form_result()

    def function_log(self):
        self.determinate_second_value()
        self.result = float(math.log(self.first_value, self.second_value))
        self.form_result()

    def determinate_second_value(self):
        self.second_value = float(self.lineEdit.text())
        self.lineEdit.clear()
        self.label.setText(str(self.first_value) + self.equal + str(self.second_value))

    def function_result(self):
        if self.equal == '+':
            self.function_addition()
        elif self.equal == '-':
            self.function_subtraction()
        elif self.equal == "/":
            self.function_divison()
        elif self.equal == '*':
            self.function_multiply()
        elif self.equal == "^":
            self.exponentiation()
        elif self.equal == "%":
            self.function_percent()
        elif self.equal == "log":
            self.function_log()

if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    calc = Calculator()
    # Запуск
    sys.exit(app.exec_())
