from django.contrib import admin
from .models import Info, Department ,teaching, continuingphdstudents,continuingmtstudents,continuingbtstudents,completephdstudents,completemtstudents,completebtstudents, publication, recognition, project

# Register your models here.

admin.site.register(Info)
admin.site.register(Department)
admin.site.register(completemtstudents)
admin.site.register(completebtstudents)
admin.site.register(completephdstudents)
admin.site.register(continuingbtstudents)
admin.site.register(continuingmtstudents)
admin.site.register(continuingphdstudents)
admin.site.register(publication)
admin.site.register(recognition)
admin.site.register(project)
admin.site.register(teaching)