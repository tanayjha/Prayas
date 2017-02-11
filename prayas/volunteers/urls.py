from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$',views.addvolunteer, name='add-volunteer'),
    url(r'^search$',views.searchvolunteer, name='search-volunteer'),  
    url(r'^(?P<volunteer_roll_no>[0-9]+-[A-Z]+-[0-9]+)$',views.volunteerProfile,name='volunteerprofile'),
    # url(r'^edit/(?P<volunteer_roll_no>[0-9]+)$',views.editStudent,name='edit-student'),
]
