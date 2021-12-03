import time

from PyQt5.QtCore import QThread

class MoveThread(QThread): # 총알 이동 스레드
    def __init__(self, parent=None):
        super().__init__(parent)
        self.par = parent

    def run(self):
        print(self.par.me)
        while self.par.isAlive:
            for i in range(len(self.par.myBullets)):
                self.par.myBullets[i].move(0, -5)
                if self.par.myBullets[i].y < 0:
                    self.par.myBullets[i].isAlive = False
                    self.par.myBullets[i].close()
                    self.par.myBullets[i].deleteLater()
            self.myBullets = [bullets for bullets in self.par.myBullets if bullets.isVisible()]
            for i in range(len(self.par.bullets)):
                self.par.bullets[i].move(0, 5)
                if self.par.bullets[i].y >= 500:
                    self.parparent().bullets[i].move(0, -250)

            for i in range(len(self.par.myBullets)):
                if self.par.enem.overlap(self.par.myBullets[i]):
                    self.par.enem.close()
                    self.par.enem.deleteLater()
                    self.par.enem.isAlive = False

            self.redraw()
            self.par.QApplication.processEvents()
            time.sleep(0.01)

    def redraw(self):
        if self.parent().width() > 500:
            self.parent().resize(self.parent().width()-1, self.parent().height())
        else:
            self.parent().resize(self.parent().width()+1, self.parent().height())

class MakeEnemThread(QThread): # 적 생성 스레드
    def __init__(self, parent=None):
        super().__init__(parent)
        self.par = parent

    def run(self):
        while self.par.isAlive:
            print(1)
            time.sleep(10)