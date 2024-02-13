from django.contrib import admin
from AboutUs.models import AboutModel
class UsAdmin(admin.ModelAdmin):
    list_display=('aboutusTitle','iconImg','titleName','descMessage','readmoreLink')
admin.site.register(AboutModel,UsAdmin)

# Register your models here.
