import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def isnum(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_two = QHBoxLayout()
        self.hbox_three = QHBoxLayout()
        self.hbox_thour = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_two)
        self.vbox.addLayout(self.hbox_three)
        self.vbox.addLayout(self.hbox_thour)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_nul = QPushButton("0", self)
        self.hbox_three.addWidget(self.b_nul)
        self.b_devyt = QPushButton("9", self)
        self.hbox_three.addWidget(self.b_devyt)
        self.b_vosem = QPushButton("8", self)
        self.hbox_three.addWidget(self.b_vosem)
        self.b_sem = QPushButton("7", self)
        self.hbox_two.addWidget(self.b_sem)
        self.b_shest = QPushButton("6", self)
        self.hbox_two.addWidget(self.b_shest)
        self.b_pyt = QPushButton("5", self)
        self.hbox_two.addWidget(self.b_pyt)
        self.b_chetiri = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_chetiri)
        self.b_tri = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_tri)
        self.b_dva = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_dva)
        self.b_odin = QPushButton("1", self)
        self.hbox_thour.addWidget(self.b_odin)
        self.b_plus = QPushButton("+", self)
        self.hbox_two.addWidget(self.b_plus)
        self.b_minus = QPushButton("-", self)
        self.hbox_three.addWidget(self.b_minus)
        self.b_mult = QPushButton("*", self)
        self.hbox_thour.addWidget(self.b_mult)
        self.b_div = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_div)
        self.b_dot = QPushButton(".", self)
        self.hbox_thour.addWidget(self.b_dot)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_dot.clicked.connect(lambda: self._button("."))
        self.b_result.clicked.connect(self._result)
        self.b_nul.clicked.connect(lambda: self._button("0"))
        self.b_devyt.clicked.connect(lambda: self._button("9"))
        self.b_vosem.clicked.connect(lambda: self._button("8"))
        self.b_sem.clicked.connect(lambda: self._button("7"))
        self.b_shest.clicked.connect(lambda: self._button("6"))
        self.b_pyt.clicked.connect(lambda: self._button("5"))
        self.b_chetiri.clicked.connect(lambda: self._button("4"))
        self.b_tri.clicked.connect(lambda: self._button("3"))
        self.b_dva.clicked.connect(lambda: self._button("2"))
        self.b_odin.clicked.connect(lambda: self._button("1"))
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
    def _operation(self, op):
        if not self.isnum(self.input.text()):
            return self.input.setText("Error")
        else:
            self.num_1 = fN(float(self.input.text()))
            self.op = op
            self.input.setText("")
    def _result(self):
        if not self.isnum(self.input.text()):
            return self.input.setText("Error")
        if self.input.text() and self.op:
            self.num_2 = fN(float(self.input.text()))
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))
            if self.op == "/" and self.num_1 != 0 and self.num_2 != 0:
                self.input.setText(str(self.num_1 / self.num_2))
            if self.num_1 == 0 or self.num_2 == 0:
                return self.input.setText("Нельзя делить на ноль")

def application():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()

fN = lambda n: n \
    if n % 1 \
    else int(n)