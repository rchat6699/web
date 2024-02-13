from django.contrib import admin

# Register your models here.
from SignUp.models import Signupform
class SignAdmin(admin.ModelAdmin):
    list_display=('Email','Password','RepeatPassword')
admin.site.register(Signupform,SignAdmin)