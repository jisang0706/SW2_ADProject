from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

app_main = 'rank'
urlpatterns = [
    path('', views.intro, name='rankintro'),
    path('list', views.rank_list, name='ranklist'),
    path('save/<str:getuserName>/<str:getscore>', views.saverank, name='ranksave'),
]