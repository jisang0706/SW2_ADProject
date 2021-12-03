import random
import time

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication

import sound
from thing import Thing


class MoveThread(): # 오브젝트 이동
    def __init__(self, parent=None):
        self.par = parent

    def moveMyBullets(self): # 발사한 총알 이동
        for i in range(len(self.par.myBullets)):
            self.par.myBullets[i].move(0, -3)
            if self.par.myBullets[i].y < 0:
                self.par.myBullets[i].isAlive = False
                self.par.myBullets[i].close()
                self.par.myBullets[i].deleteLater()

    def moveEnemyBullets(self): # 적군 총알 이동
        for i in range(len(self.par.bullets)):
            self.par.bullets[i].move(0, 3)
            if self.par.me.overlap(self.par.bullets[i]):
                sound.meDie()
                self.par.gameOver()
            if self.par.bullets[i].y >= 500:
                self.par.bullets[i].close()
                self.par.bullets[i].deleteLater()

    def checkEnemyMeetBullet(self): # 적군이 자신이 발사한 총알과 닿았는지 검사
        for i in range(len(self.par.myBullets)):
            for j in range(len(self.par.enems)):
                if self.par.enems[j].overlap(self.par.myBullets[i]):
                    self.par.scoreLabel.setText(f'{int(self.par.scoreLabel.text()) + self.par.enems[j].score}')
                    self.par.enems[j].close()
                    self.par.enems[j].deleteLater()
                    self.par.myBullets[i].close()
                    self.par.myBullets[i].deleteLater()
                    sound.enemyKill()
                    break

    def makeEnemyBullet(self, now): # 적군 총알 생성
        for j in range(len(self.par.enems)):
            if self.par.enems[j].shot <= now:
                if int(self.par.scoreLabel.text()) >= 1000:
                    self.par.enems[j].shot = now + 1
                elif int(self.par.scoreLabel.text()) >= 500:
                    self.par.enems[j].shot = now + 2
                else:
                    self.par.enems[j].shot = now + 3
                self.par.bullets.append(
                    Thing(self.par, self.par.enems[j].x, self.par.enems[j].y, 'bullet'))
                self.par.bullets[-1].show()

    def deleteTrash(self): # 삭제된 총알, 적군 배열에서 제거
        self.par.enems = [enem for enem in self.par.enems if enem.isVisible()]
        self.par.bullets = [bullet for bullet in self.par.bullets if bullet.isVisible()]
        self.par.myBullets = [bullets for bullets in self.par.myBullets if bullets.isVisible()]

    def run(self):
        self.flag = int(time.time()) + 5
        while self.par.isAlive:

            self.moveMyBullets()
            self.moveEnemyBullets()
            self.checkEnemyMeetBullet()
            self.deleteTrash()
            self.makeEnemyBullet(time.time())

            if time.time() >= self.flag:
                self.flag += random.uniform(0.0, 1.0)
                self.par.addEnem()
                sound.enemyAppear()

            self.redraw()
            QApplication.processEvents()
            time.sleep(0.01)

    def redraw(self): # 메인 화면 갱신
        if self.par.width() > 500:
            self.par.resize(self.par.width()-1, self.par.height())
        else:
            self.par.resize(self.par.width()+1, self.par.height())