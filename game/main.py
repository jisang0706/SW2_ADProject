"""
메인 화면

wasd를 방향키로 이용. 자신의 캐릭터를 움직임
스페이스바를 누르면 총을 발사

적은 일정 시간이 지났을 때 생성
일단 맨 위에서 등장
랜덤하게 총 발사
"""
import random
import sys
import threading
import time
from multiprocessing import Process

from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QWidget, QLayout, QApplication, QVBoxLayout, QLCDNumber, QLabel, QGridLayout, QMessageBox

from saverank import SaveRank
from thread import MoveThread
from thing import Thing
from me import Me
import sound

class Main (QWidget):

    def __init__(self, parent):    # 생성자
        super().__init__()
        self.isAlive = True
        self.application = QApplication
        self.par = parent

        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: black;")

        self.me = Me(self)
        self.myBullets = []

        self.scoreLabel = QLabel('0', self)
        self.scoreLabel.setGeometry(10, 10, 500, 15)
        self.scoreLabel.show()


        self.enems = []

        self.bullets = []

        self.show()
        self.startGame()

    def startGame(self): # 멀티스레드 시작
        self.isAlive = True
        self.movethread = MoveThread(self)
        self.movethread.run()
        # self.makeenemthread = MakeEnemThread(self)

        # self.movethread.start()
        # self.makeenemthread.start()


    def keyPressEvent(self, e) -> None: # 키보드 입력 이벤트
        if e.key() == Qt.Key_Space:
            pass
        elif e.key() == Qt.Key_Left:
            if self.safe(self.me.x - 15, self.me.y):
                self.me.move(-15, 0)
        elif e.key() == Qt.Key_Right:
            if self.safe(self.me.x + 15, self.me.y):
                self.me.move(15, 0)
        elif e.key() == Qt.Key_Up:
            if self.safe(self.me.x, self.me.y - 15):
                self.me.move(0, -15)
        elif e.key() == Qt.Key_Down:
            if self.safe(self.me.x, self.me.y + 15):
                self.me.move(0, 15)
        elif e.key() == Qt.Key_Tab:
            self.myBullets.append(Thing(self, self.me.x+5, self.me.y, 'bullet'))
            self.myBullets[-1].show()

    def mouseMoveEvent(self, QMouseEvent): # 마우스 위치 이벤트
        if self.safe(QMouseEvent.x() - 7, QMouseEvent.y() - 5):
            self.me.go(QMouseEvent.x() - 7, QMouseEvent.y() - 5)

    def safe(self, x, y): # 해당 좌표가 화면 안에 존재하는 좌표인지 검사
        if x >= 0 and x <= 500 and y >= 0 and y <= 485:
            return True
        return False

    def closeEvent(self, QCloseEvent): # 종료시 실행 이벤트
        self.isAlive = False
        self.deleteLater()

    def addEnem(self):
        self.enems.append(Thing(self, random.randint(0, 500 - 15), random.randint(0, 250), 'enemy'))
        self.enems[-1].show()

    def gameOver(self):
        QMessageBox.information(self, 'Game Over', f'{self.scoreLabel.text()}점 달성!', QMessageBox.Ok)
        self.par.saveRank("Unknown", self.scoreLabel.text())
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()