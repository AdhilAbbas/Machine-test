from django.urls import path
from . import views
from .views import Loginview,Userview,Logoutview

urlpatterns =[
    path('login/',Loginview.as_view()),
    path('user/',Userview.as_view()),
    path('logout/',Logoutview.as_view()),
]