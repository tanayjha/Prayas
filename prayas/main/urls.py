from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/$',views.handleLogin, name='login'),
	url(r'^logout/$',views.handleLogout, name='logout'),
]