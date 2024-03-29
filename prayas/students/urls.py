from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$',views.addstudent, name='add-student'),
    url(r'^search$',views.searchstudent, name='search-student'),  
    url(r'^(?P<student_rollNo>[0-9]+)$',views.studentProfile,name='studentprofile'),
    url(r'^edit/(?P<student_rollNo>[0-9]+)$',views.editStudent,name='edit-student'),
]
