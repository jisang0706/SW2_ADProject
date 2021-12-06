import json
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QToolButton, QApplication, QDesktopWidget, QLabel, QListWidget
import requests

from saverank import SaveRank
from main import Main


class Intro (QWidget):
    url = "https://sw-adproject-ahpjy.run.goorm.io/rank/"

    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 600)

        self.rankList = QListWidget(self)
        self.setRank()

        self.startButton = QToolButton(self)
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startGame)
        self.startButton.move(130, 435)
        self.startButton.show()

        self.tutorialLabel = QLabel(self)
        self.tutorialLabel.setText("마우스 클릭 후 드래그하여 이동\n\nTab 키를 눌러 총알 발사")
        self.tutorialLabel.move(10, 550)
        self.tutorialLabel.show()


    def saveShow(self, score):
        rank = SaveRank(self, score)
        rank.show()

    def startGame(self):
        Main(self)

    def setRank(self):
        self.rankList.clear()
        rankList = self.getRank()
        if rankList:
            for i, content in enumerate(rankList):
                self.rankList.insertItem(i, content[0] + " - " + str(content[1]))
        self.rankList.move(10, 10)
        self.rankList.show()

    def getRank(self):
        try:
            return self.jsonToList(requests.get(self.url + 'list').json())
        except:
            return False

    def saveRank(self, userName, score):
        requests.get(self.url + 'save/' + userName + "/" + str(score))
        try:
            return self.setRank()
        except:
            return False

    def jsonToList(self, content):
        ranks = []
        for obj in content.get("rank"):
            ranks.append([obj.get("userName"), obj.get("score")])
        return ranks


if __name__ == "__main__":
    app = QApplication(sys.argv)
    intro = Intro()
    intro.show()
    sys.exit(app.exec_())