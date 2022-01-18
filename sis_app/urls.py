from django.urls import path
from django.conf import settings
from . import views


app_name = 'sis_app'

urlpatterns=[
    path('studentList',views.StudentList, name="student_list"),
    path('studentForm',views.studentForm, name="student_form"),
]
