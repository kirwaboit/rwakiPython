import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chep\'s App Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    kirwasFirstForm = LoginForm()
    kirwasFirstForm.show()


    sys.exit(app.exec_())