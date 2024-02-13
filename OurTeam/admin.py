from django.contrib import admin
from OurTeam.models import EmpModel
class TeamAdmin(admin.ModelAdmin):
    list_display=('teamTitle','teamImg','employeeName','designation')
admin.site.register(EmpModel,TeamAdmin)

# Register your models here.