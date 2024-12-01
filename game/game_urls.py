import game.views
from django.urls import path

urlpatterns = [
    path('', game.views.index, name='home')
]
