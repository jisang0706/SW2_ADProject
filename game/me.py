"""
본인

QLabel 사용
"""
from PyQt5.QtWidgets import QLabel
from object import Object

class Me (Object):

    def __init__(self, parent): # 생성자
        super().__init__(parent, 250, 450, 15, 30, 'friend', 3, 'O', "background-color:yellow")