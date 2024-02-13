from django.contrib import admin
from WhyChooseUs.models import ChooseModel
class UsAdmin(admin.ModelAdmin):
    list_display=('whychooseusTitle','iconImg','titleName','descMessage','readmoreLink')
admin.site.register(ChooseModel,UsAdmin)

# Register your models here.
