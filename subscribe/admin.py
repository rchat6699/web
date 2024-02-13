
from django.contrib import admin

# Register your models here.
from subscribe.models import Subscribe
class SubscribeAdmin(admin.ModelAdmin):
    list_display=('fullname','email','phone','message')
admin.site.register(Subscribe,SubscribeAdmin)
