from PyQt5.QtWidgets import QApplication,QWidget,QMenu,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter,QBrush,QColor,QFont
from PyQt5.QtCore import Qt,QPoint
import sys
import pandas as pd


class win(QWidget):

    def __init__(self,master=None):
        super(win,self).__init__(master)
        left=800;top=100;width=1360;height=1200
        self.setGeometry(left,top,width,height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.table = QTableWidget(10,3,self)
        self.table.setHorizontalHeaderLabels(["Name","Street","City"])
        self.table.horizontalHeader().setStyleSheet('QHeaderView::section{font-family:"Times New Roman";font-size:12pt;color:darkBlue;background-color:rgb(255,239,239);font-weight:400;border:2px solid rgba(0,0,126,255);border-radius:16px}')
        self.table.verticalHeader().setStyleSheet('QHeaderView::section{font-family:"Times New Roman";font-size:9pt;color:darkBlue;background-color:rgb(255,239,239);font-weight:400;border:2px solid rgba(0,0,126,255);border-radius:16px}')
        self.table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table.setStyleSheet("QScrollBar:horizontal{border:2px solid grey;background:#32CC99;height:14px}QScrollBar:vertical{border:2px solid grey;background:#32CC99;width:15px}")
        self.table.verticalHeader().setFixedWidth(35)
        self.table.setColumnWidth(0,300)
        self.table.setColumnWidth(1,300)
        self.table.setColumnWidth(2,300)
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("QTableView{alternate-background-color:rgba(220,254,218,255);background-color:rgba(201,254,198,255);color:rgba(200,0,0,255);font-family:Century725 Cn BT;font-size:12pt;padding:10px;border:2px outset rgba(0,0,126,255);border-radius:30px}QTableWidget::item{padding-left:20px;border:0px}QTableView::item:selected:active{background:#4B94FF;}")
        self.table.setGeometry(200,300,960,400)

        col = ['Name','Street','City']
        data = [['James','Oxford','London'],['Robert','Abbey','Liverpool'],['John','Carnaby','Bristol']]
        df = pd.DataFrame(columns=col,data=data)

        self.LoadTable(df)


    def LoadTable(self,df):

        self.table.blockSignals(True)
        self.table.setSortingEnabled(False)
        while (self.table.rowCount() > 0):
            self.table.removeRow(0)

        for index,row in df.iterrows():
            self.table.insertRow(index)

            font = QFont('Brush Script MT',20)
            item = QTableWidgetItem(row['Name'])
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0,0,255)))
            item.setBackground(QBrush(QColor(255,221,255)))
            self.table.setItem(index,0,item)
            self.table.resizeRowsToContents()

            item = QTableWidgetItem(row['Street'])
            item.setTextAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            self.table.setItem(index,1,item)

            item = QTableWidgetItem(row['City'])
            item.setTextAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            self.table.setItem(index,2,item)

        self.table.setSortingEnabled(True)
        self.table.blockSignals(False)


    def paintEvent(self,ev):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing,True)
        painter.begin(self)
        painter.setBrush(QColor(76,77,0,120))
        painter.drawRoundedRect(self.rect(),140,140)
        painter.end()

    def mousePressEvent(self,event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos()-self.oldPos)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPos = event.globalPos()

    def contextMenuEvent(self,event):
        contextMenu = QMenu(self)
        actionDue = contextMenu.addAction("Exit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == actionDue:
            quit()


App = QApplication(sys.argv)
widget = win()
widget.show()
sys.exit(App.exec_())
