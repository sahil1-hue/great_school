from django.urls import path
from .import views
urlpatterns = [
    path('',  views.school_look_up, name =' look_up_school')


]