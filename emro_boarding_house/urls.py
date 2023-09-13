from django.urls import path
from . import views

urlpatterns = [
    path('emro_boarding_house/', views.emro_boarding_house , name='emro_boarding_house'),

]
