import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')

        # Set black background color for the QWidget
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)

        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Create the buttons
        self.buttons = {}
        self.buttons['1'] = QPushButton('1')
        self.buttons['2'] = QPushButton('2')
        self.buttons['3'] = QPushButton('3')
        self.buttons['4'] = QPushButton('4')
        self.buttons['5'] = QPushButton('5')
        self.buttons['6'] = QPushButton('6')
        self.buttons['7'] = QPushButton('7')
        self.buttons['8'] = QPushButton('8')
        self.buttons['9'] = QPushButton('9')
        self.buttons['0'] = QPushButton('0')
        self.buttons['+'] = QPushButton('+')
        self.buttons['-'] = QPushButton('-')
        self.buttons['*'] = QPushButton('*')
        self.buttons['/'] = QPushButton('/')
        self.buttons['='] = QPushButton('=')
        self.buttons['C'] = QPushButton('C')
        self.buttons['√'] = QPushButton('√')
        self.buttons['^'] = QPushButton('^')
        self.buttons['sin'] = QPushButton('sin')
        self.buttons['cos'] = QPushButton('cos')
        self.buttons['tan'] = QPushButton('tan')
        self.buttons['!'] = QPushButton('!')
        self.buttons['A'] = QPushButton('A')
        self.buttons['V'] = QPushButton('V')

        # Set light green background color for the QPushButton widgets
        for button in self.buttons.values():
            button.setAutoFillBackground(True)
            button_palette = button.palette()
            button_palette.setColor(QPalette.Button, QColor(144, 238, 144))
            button.setPalette(button_palette)

        # Create the layout
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.grid.addWidget(self.buttons['√'], 1, 0)
        self.grid.addWidget(self.buttons['^'], 1, 1)
        self.grid.addWidget(self.buttons['sin'], 1, 2)
        self.grid.addWidget(self.buttons['cos'], 1, 3)

        self.grid.addWidget(self.buttons['tan'], 2, 0)
        self.grid.addWidget(self.buttons['!'], 2, 1)
        self.grid.addWidget(self.buttons['A'], 2, 2)
        self.grid.addWidget(self.buttons['V'], 2, 3)

        self.grid.addWidget(self.buttons['1'], 3, 0)
        self.grid.addWidget(self.buttons['2'], 3, 1)
        self.grid.addWidget(self.buttons['3'], 3, 2)
        self.grid.addWidget(self.buttons['+'], 3, 3)

        self.grid.addWidget(self.buttons['4'], 4, 0)
        self.grid.addWidget(self.buttons['5'], 4, 1)
        self.grid.addWidget(self.buttons['6'], 4, 2)
        self.grid.addWidget(self.buttons['-'], 4, 3)

        self.grid.addWidget(self.buttons['7'], 5, 0)
        self.grid.addWidget(self.buttons['8'], 5, 1)
        self.grid.addWidget(self.buttons['9'], 5, 2)
        self.grid.addWidget(self.buttons['*'], 5, 3)

        self.grid.addWidget(self.buttons['0'], 6, 0)
        self.grid.addWidget(self.buttons['C'], 6, 1)
        self.grid.addWidget(self.buttons['='], 6, 2)
        self.grid.addWidget(self.buttons['/'], 6, 3)

        self.setLayout(self.grid)

        # Connect the buttons to the functions
        self.buttons['1'].clicked.connect(lambda: self.button_click('1'))
        self.buttons['2'].clicked.connect(lambda: self.button_click('2'))
        self.buttons['3'].clicked.connect(lambda: self.button_click('3'))
        self.buttons['4'].clicked.connect(lambda: self.button_click('4'))
        self.buttons['5'].clicked.connect(lambda: self.button_click('5'))
        self.buttons['6'].clicked.connect(lambda: self.button_click('6'))
        self.buttons['7'].clicked.connect(lambda: self.button_click('7'))
        self.buttons['8'].clicked.connect(lambda: self.button_click('8'))
        self.buttons['9'].clicked.connect(lambda: self.button_click('9'))
        self.buttons['0'].clicked.connect(lambda: self.button_click('0'))
        self.buttons['+'].clicked.connect(lambda: self.button_click('+'))
        self.buttons['-'].clicked.connect(lambda: self.button_click('-'))
        self.buttons['*'].clicked.connect(lambda: self.button_click('*'))
        self.buttons['/'].clicked.connect(lambda: self.button_click('/'))
        self.buttons['='].clicked.connect(self.button_equal)
        self.buttons['C'].clicked.connect(self.button_clear)
        self.buttons['√'].clicked.connect(self.button_sqrt)
        self.buttons['^'].clicked.connect(lambda: self.button_click('**'))
        self.buttons['sin'].clicked.connect(self.button_sin)
        self.buttons['cos'].clicked.connect(self.button_cos)
        self.buttons['tan'].clicked.connect(self.button_tan)
        self.buttons['!'].clicked.connect(self.button_factorial)
        self.buttons['A'].clicked.connect(self.button_circle_area)
        self.grid.addWidget(self.buttons['V'], 2, 3)


    def button_click(self, char):
        current_text = self.display.text()
        new_text = current_text + char
        self.display.setText(new_text)

    def button_clear(self):
        self.display.setText('')

    def button_equal(self):
        try:
            result = eval(self.display.text())
        except Exception as e:
            result = 'Error'

        self.display.setText(str(result))

    def button_sqrt(self):
        try:
            result = math.sqrt(float(self.display.text()))
        except Exception as e:
            result = 'Error'

        self.display.setText(str(result))

    def button_sin(self):
        try:
            result = math.sin(math.radians(float(self.display.text())))
        except Exception as e:
            result = 'Error'

        self.display.setText(str(result))

    def button_cos(self):
        try:
            result = math.cos(math.radians(float(self.display.text())))
        except Exception as e:
            result = 'Error'

        self.display.setText(str(result))

    def button_tan(self):
        try:
            result = math.tan(math.radians(float(self.display.text())))
        except Exception as e:
            result = 'Error'

        self.display.setText(str(result))

    def button_factorial(self):
        try:
            result = math.factorial(int(self.display.text()))
        except Exception as e:
            result = 'Error'
        self.display.setText(str(result))

    def button_circle_area(self):
       try:
           radius = float(self.display.text())
           result = math.pi * radius ** 2
       except Exception as e:
           result = 'Error'
       self.display.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
