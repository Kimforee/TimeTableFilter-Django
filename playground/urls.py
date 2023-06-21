from django.urls import path
from.import views

urlpatterns = [
    path('hello/',views.timetable ,name='timetable'),
    path('filtered/', views.filtered, name='filtered')
]
