"""
본인 캐릭터, 적, 총알 등 게임의 객체를 담당하는 클래스
x, y - 화면상에 표시될 객체 좌표
width, height - 너비, 높이
tag - 해당 객체의 태그. 같은 재질의 객체를 구분하기 위한 것 (ex : 적과 적의 총알의 tag는 Enemy. 아군과 아군의 총알은 Friendly)
life - 해당 객체의 현재 생명 수
form - 객체 모습 (현재는 일단 문자열로 처리)
"""

class Object:

    def __init__(self): # 생성자
        return self.__init__(0, 0, 0, 0, 'Object', 0, "T")

    def __init__(self, x, y, width, height, tag, life, form):   # 생성자
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.tag = tag
        self.life = life
        self.form = form

    def move(self, x_plus, y_plus): # 현재 위치에 x_plus, y_plus만큼 더한 위치로 설정
        pass