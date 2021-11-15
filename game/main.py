"""
메인 화면

wasd를 방향키로 이용. 자신의 캐릭터를 움직임
스페이스바를 누르면 총을 발사

적은 일정 시간이 지났을 때 생성
일단 맨 위에서 등장
랜덤하게 총 발사
"""
import sys

from PyQt5.QtWidgets import QWidget, QLayout, QApplication


class Main (QWidget):

    def __init__(self, parent=None):    # 생성자
        super().__init__(parent)

        self.mainLayout = QLayout()
        self.mainLayout.setSizeConstraint(100, 100)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())