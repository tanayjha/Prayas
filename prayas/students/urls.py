from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student/add$',views.addstudent, name='add-student'),  
]
