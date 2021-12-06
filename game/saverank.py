from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QApplication, QToolButton, QPushButton


class SaveRank(QWidget):

    def __init__(self, parent=None, score=None):
        super().__init__()
        print(parent)
        print(score)
        self.score = score
        self.par = parent

        layout = QGridLayout()

        self.usernameLabel = QLabel()
        self.usernameLabel.setText("이름")
        layout.addWidget(self.usernameLabel, 0, 0, 1, 2)

        self.usernameEdit = QLineEdit()
        self.usernameEdit.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.usernameEdit, 1, 0, 1, 2)

        self.okButton = QPushButton()
        self.okButton.setText("저장하기")
        self.okButton.clicked.connect(self.buttonClose)
        layout.addWidget(self.okButton, 2, 1, 1, 1)

        self.setLayout(layout)
        print("WOW")

    def buttonClose(self):
        self.close()

    def closeEvent(self, QCloseEvent):
        if self.par:
            self.par.saveRank(self.usernameEdit.text(), self.score)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    saveRank = SaveRank()
    saveRank.show()
    sys.exit(app.exec_())