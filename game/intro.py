import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QToolButton, QApplication, QDesktopWidget, QLabel

from main import Main


class Intro (QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 300)

        self.startButton = QToolButton(self)
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startGame)
        self.startButton.move(130, 135)
        self.startButton.show()

        self.tutorialLabel = QLabel(self)
        self.tutorialLabel.setText("마우스 클릭 후 드래그하여 이동\n\nTab 키를 눌러 총알 발사")
        self.tutorialLabel.move(10, 250)
        self.tutorialLabel.show()

    def startGame(self):
        Main()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    intro = Intro()
    intro.show()
    sys.exit(app.exec_())