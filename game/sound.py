"""
사운드 재생
인트로 사운드
총 발사 사운드
적 처치 사운드
적 등장 사운드
자신 캐릭터 사망 사운드
"""
import playsound as pl

def introMusic(): # 인트로 뮤직 재생
    pl.playsound('./sound/intro_music.mp3')

def shootSound(): # 총 발사 사운드 재생
    pl.playsound('./sound/shot_sound.mp3')

def enemyKill(): # 적 처치 사운드
    pl.playsound('./sound/enemy_die.mp3')

def enemyAppear(): # 적 등장 사운드
    pl.playsound('./sound/enemy_appears')

def meDie(): # 자신 캐릭터 사망 사운드
    pl.playsound('./sound/game_over.mp3')
