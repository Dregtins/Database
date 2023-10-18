import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget 
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit, QVBoxLayout
from PyQt5 import QtGui


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
# подключить базу данных
        self.conn = psycopg2.connect(user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432",
                                     database="vlad")
        self.cur = self.conn.cursor()
        print('connected')

        self.cur.execute("SELECT * FROM sheet.vlad2")

        # retrieve the records from the database
        records = self.cur.fetchall()
        print(records)
# параметры окна
        self.setGeometry(100, 100, 1600, 1200)
        self.setWindowTitle('Коррупция')
# создать табличку
        self.Tables()
# здесь идентификатор
        self.idp = QLineEdit(self)
        self.idp.resize(150, 40)
        self.idp.move(1400, 60)
# здесь username
        self.username = QLineEdit(self)
        self.username.resize(150, 40)
        self.username.move(1400, 110)
# здесь time
        self.time = QLineEdit(self)
        self.time.resize(150, 40)
        self.time.move(1400, 160)
# здесь text
        self.text = QLineEdit(self)
        self.text.resize(150, 40)
        self.text.move(1400, 210)
# кнопка поиска
        self.btn = QPushButton('Поиск', self)
        self.btn.resize(150, 40)
        self.btn.move(1400, 260)
# кнопка сброса фильтра
        self.btn = QPushButton('Сбросить', self)
        self.btn.resize(150, 40)
        self.btn.move(1400, 310)
# создание таблицы в интерфейсе
    def Tables(self):
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("ID"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("USERNAME"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("VOICE_MESSAGE"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("VOICE_MESSAGE_TEXT"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("TIME"))
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)

        self.tableWidget.setItem(1, 0, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("dregtin"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("C:Programming\Python\vlad\voice\svz.mp3"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("взятка"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("12:50"))

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
