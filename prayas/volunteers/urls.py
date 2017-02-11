from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$',views.addvolunteer, name='add-volunteer'),
    # url(r'^volunteer/search$',views.searchstudent, name='search-student'),  
    # url(r'^(?P<volunteer_roll_no>[0-9]+)$',views.studentProfile,name='studentprofile'),
    # url(r'^edit/(?P<volunteer_roll_no>[0-9]+)$',views.editStudent,name='edit-student'),
]
