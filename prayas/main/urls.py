from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/$',views.handleLogin, name='login'),
	url(r'^logout/$',views.handleLogout, name='logout'),
	url(r'^manageMain/$',views.manageMain, name='mainEditing'),
	url(r'^manageNotices/$',views.manageNotices, name='manageNotices'),
	url(r'^notices/(?P<pageNo>[0-9]+)/$',views.notice, name='allNotices'),
	url(r'^manageEvent/$',views.addEvent, name='addEvent'),
	url(r'^removeEvent/(?P<pk>[0-9]+)/$',views.removeEvent, name='removeEvent'),
	url(r'^removeGallery/(?P<galleryPk>[0-9]+)/$',views.removeGallery, name='removeGallery'),
	url(r'^manageGallery/(?P<pk>[0-9]+)/$',views.addGallery, name='addGallery'),
	url(r'^allEvents/$', views.mainEvents, name= 'mainEvents'),
	url(r'^allgallery/(?P<pk>[0-9]+)/$', views.mainGallery, name='mainGallery'),
	url(r'^$',views.homePage, name='home'),
]