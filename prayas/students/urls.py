from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student/add$',views.addstudent, name='add-student'),
    url(r'^student/search$',views.searchstudent, name='search-student'),  
    url(r'^(?P<student_rollNo>[0-9]+)$',views.studentProfile,name='studentprofile'),
]
