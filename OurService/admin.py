from django.contrib import admin
from OurService.models import ServiceModel
class OurAdmin(admin.ModelAdmin):
    list_display=('ourserviceTitle','iconImg','titleName','descMessage','readmoreLink')
admin.site.register(ServiceModel,OurAdmin)
# Register your models here.
