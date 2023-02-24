from django.contrib import admin
from django.urls import path
from app.views import home , page
urlpatterns = [
    path('home/', home , name='home' ),
    path('page/', page , name='page' ),
]
