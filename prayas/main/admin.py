from django.contrib import admin

# Register your models here.

from main.models import *

admin.site.register(mainPage)
admin.site.register(students)
admin.site.register(volunteers)
admin.site.register(notices)
admin.site.register(events)