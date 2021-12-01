"""
메인 화면

wasd를 방향키로 이용. 자신의 캐릭터를 움직임
스페이스바를 누르면 총을 발사

적은 일정 시간이 지났을 때 생성
일단 맨 위에서 등장
랜덤하게 총 발사
"""
import sys
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLayout, QApplication, QVBoxLayout, QLCDNumber, QLabel

from enemy import Enemy
from me import Me


class Main (QWidget):

    def __init__(self):    # 생성자
        super().__init__()

        self.resize(500, 500)

        enem = Enemy(self, 250, 250, 'enemy')

        self.me = Me(self)

        self.bullets = [Enemy(self, _*50, _*50, 'bullet') for _ in range(3)]

        self.show()

        self.moveBullet()

    def redraw(self):
        if self.width() > 500:
            self.resize(self.height()-1, self.width()-1)
        else:
            self.resize(self.height()+1, self.width()+1)

    def moveBullet(self):
        for i in range(len(self.bullets)):
            self.bullets[i].move(0, 5)
        self.redraw()
        QApplication.processEvents()
        timer = threading.Timer(0.2, self.moveBullet)
        timer.start()

    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Space:
            pass
        elif e.key() == Qt.Key_Left:
            self.me.move(-15, 0)
        elif e.key() == Qt.Key_Right:
            self.me.move(15, 0)
        elif e.key() == Qt.Key_Up:
            self.me.move(0, -15)
        elif e.key() == Qt.Key_Down:
            self.me.move(0, 15)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())