"""
적군 or 총알

QLabel 사용
"""

from PyQt5.QtCore import QRectF, pyqtSignal
from PyQt5.QtWidgets import QLabel, QSizePolicy
from object import Object

class Thing (Object):

    def __init__(self, parent): # 생성자
        super().__init__(parent, 0, 0, 15, 15, 'enemy', 1, 'T', "background-color: red")

    def __init__(self, parent, x, y, kind):
        if kind == 'enemy':
            super().__init__(parent, x, y, 15, 15, 'enemy', 1, 'T', "background-color: red")
            self.score = 5
            self.shot = 0
        elif kind == 'bullet':
            super().__init__(parent, x, y, 5, 5, 'bullet', 1, 'i', "background-color:cyan")
            self.score = 0
            self.follow = False