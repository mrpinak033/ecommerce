from django.contrib import admin
from .models import SignUp

# Register your models here.
class Regadmin(admin.ModelAdmin):
    list_display = ('uname','fname','lname','dob','mobno','email','pwd','cpwd')
    class meta:
        model=SignUp


admin.site.register(SignUp, Regadmin)
