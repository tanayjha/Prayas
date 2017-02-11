from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'prayas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^student/',include('students.urls')),
    url(r'^volunteer/',include('volunteers.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
