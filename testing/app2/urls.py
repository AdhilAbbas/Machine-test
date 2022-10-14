from distutils.command.upload import upload
from django import views
from django.urls import path
from .views import Uploadview

urlpatterns = [
    path('',Uploadview.as_view()),
]