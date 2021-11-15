"""
적군

QLabel 사용
"""
from PyQt5.QtWidgets import QLabel
from game.object import Object

class Enemy (Object, QLabel):

    def __init__(self): # 생성자
        pass
