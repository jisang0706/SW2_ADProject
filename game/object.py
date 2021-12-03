"""
본인 캐릭터, 적, 총알 등 게임의 객체를 담당하는 클래스
x, y - 화면상에 표시될 객체 좌표
width, height - 너비, 높이
tag - 해당 객체의 태그. 같은 재질의 객체를 구분하기 위한 것 (ex : 적과 적의 총알의 tag는 Enemy. 아군과 아군의 총알은 Friendly)
life - 해당 객체의 현재 생명 수
form - 객체 모습 (현재는 일단 문자열로 처리)
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSizePolicy


class Object (QLabel):

    def __init__(self, parent): # 생성자
        return self.__init__(parent, 0, 0, 0, 0, 'Object', 0, "T")

    def __init__(self, parent, x, y, width, height, tag, life, form, background):   # 생성자
        super().__init__(tag, parent)

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.setText(form)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.isAlive = True
        super().move(x, y)
        super().setFixedSize(width, height)
        super().setStyleSheet(background)
        super().setAlignment(Qt.AlignCenter)

    @property
    def tag(self):
        return self._tag

    @property
    def form(self):
        return self._form

    def move(self, x_plus, y_plus): # 현재 위치에 x_plus, y_plus만큼 더한 위치로 설정
        self.x += x_plus
        self.y += y_plus
        super().move(self.x, self.y)

    def go(self, x, y): # 해당 위치로 이동
        self.x = x
        self.y = y
        super().move(self.x, self.y)

    def overlap(self, obj): # 두 오브젝트가 겹치는지 검사
        x_end = self.x + self.width
        y_end = self.y + self.height
        obj_x_end = obj.x + obj.width
        obj_y_end = obj.y + obj.height
        if ((self.x <= obj.x and obj.x <= x_end) or (self.x <= obj_x_end and obj_x_end <= x_end)) and \
            ((self.y <= obj.y and obj.y <= y_end) or (self.y <= obj_y_end and obj_y_end <= y_end)):
            return True
        return False