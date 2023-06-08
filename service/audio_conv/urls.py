from django.urls import path

from .views import *

urlpatterns = [
    path('regis', UserRegis.as_view()),
    path('add', AddAudio.as_view()),
    path('record/?uuid=<str:uuid>&id=<int:id>', get_audio),
]
