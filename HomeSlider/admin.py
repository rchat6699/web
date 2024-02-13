from django.contrib import admin
from HomeSlider.models import SliderModel
class HomeAdmin(admin.ModelAdmin):
    list_display=('homesliderTitle','iconImg','descMessage','readmoreLink')
admin.site.register(SliderModel,HomeAdmin)

# Register your models here.
