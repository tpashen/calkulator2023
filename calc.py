from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt


app=QApplication([])

app.setStyleSheet('''QWidget 
                  {background:lightblue;
                   font-size: 12pt;
                   color:blue;} ''')
w=QWidget()
w.show()
w.resize(350,400)
w.setWindowTitle('Калькулятор')
line=QLineEdit()
line0=QHBoxLayout()
line0.addWidget(line)

b_plus=QPushButton("+")
b_minus=QPushButton("-")
b_multiply=QPushButton("*")
b_divide=QPushButton("/")

b_point=QPushButton(".")
b_equal=QPushButton("=")
b_c=QPushButton("C")
b_pr=QPushButton("%")

b1=QPushButton("1")
b2=QPushButton("2")
b3=QPushButton("3")

line1=QHBoxLayout()
line1.addWidget(b_c)
line1.addWidget(b_equal)
line2=QHBoxLayout()
line2.addWidget(b1)
line2.addWidget(b2)
line2.addWidget(b3)
line2.addWidget(b_plus)

b4=QPushButton("4")
b5=QPushButton("5")
b6=QPushButton("6")

line3=QHBoxLayout()
line3.addWidget(b4)
line3.addWidget(b5)
line3.addWidget(b6)
line3.addWidget(b_minus)

b7=QPushButton("7")
b8=QPushButton("8")
b9=QPushButton("9")

line4=QHBoxLayout()
line4.addWidget(b7)
line4.addWidget(b8)
line4.addWidget(b9)
line4.addWidget(b_multiply)


line5=QHBoxLayout()

b0=QPushButton("0")
line5.addWidget(b_pr)
line5.addWidget(b0)
line5.addWidget(b_point)
line5.addWidget(b_divide)

line_v=QVBoxLayout()
line_v.addLayout(line0)
line_v.addLayout(line1)
line_v.addLayout(line2)
line_v.addLayout(line3)
line_v.addLayout(line4)
line_v.addLayout(line5)
w.setLayout(line_v)

def b1_click():
    line.insert('1')
    line.setAlignment(Qt.AlignRight)
b1.clicked.connect(b1_click)

def b2_click():
    line.insert('2')
    line.setAlignment(Qt.AlignRight)
b2.clicked.connect(b2_click)

def b3_click():
    line.insert('3')
    line.setAlignment(Qt.AlignRight)
b3.clicked.connect(b3_click)

def b4_click():
    line.insert('4')
    line.setAlignment(Qt.AlignRight)
b4.clicked.connect(b4_click)

def b5_click():
    line.insert('5')
    line.setAlignment(Qt.AlignRight)
b5.clicked.connect(b5_click)

def b6_click():
    line.insert('6')
    line.setAlignment(Qt.AlignRight)
b6.clicked.connect(b6_click)

def b7_click():
    line.insert('7')
    line.setAlignment(Qt.AlignRight)
b7.clicked.connect(b7_click)

def b8_click():
    line.insert('8')
    line.setAlignment(Qt.AlignRight)
b8.clicked.connect(b4_click)

def b9_click():
    line.insert('9')
    line.setAlignment(Qt.AlignRight)
b9.clicked.connect(b9_click)

def b0_click():
    line.insert('0')
    line.setAlignment(Qt.AlignRight)
b0.clicked.connect(b0_click)

def b_point_click():
    line.insert('.')
    line.setAlignment(Qt.AlignRight)
b_point.clicked.connect(b_point_click)

def bc_click():
    line.setText('')
b_c.clicked.connect(bc_click)

def b_plus_click():
    global a,b
    a=float(line.text())
    b='+'
    line.setText('')
b_plus.clicked.connect(b_plus_click)

def b_minus_click():
    global a,b
    a=float(line.text())
    b='-'
    line.setText('')

b_minus.clicked.connect(b_minus_click)

def b_multiply_click():
    global a,b
    a=float(line.text())
    b='*'
    line.setText('')

b_multiply.clicked.connect(b_multiply_click)

def b_divide_click():
    global a,b
    a=float(line.text())
    b='/'
    line.setText('')
b_divide.clicked.connect(b_divide_click)
def b_pr_click():
    global a,b
    a=float(line.text())
    b='%'
    line.setText('')
b_pr.clicked.connect(b_pr_click)
def b_equal_click():
    global a,b,c
    c=float(line.text())
    line.setText('')-
    if b=='+':
        line.setText(str(a+c))
    if b=='-':
        line.setText(str(a-c)) 
    if b=='*':
        line.setText(str(a*c)) 
    if b=='/':
        line.setText(str(a/c))
    if b=='%':
        line.setText(str(c/100*a))
b_equal.clicked.connect(b_equal_click)
app.exec()
