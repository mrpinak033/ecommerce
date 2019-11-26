from django.contrib import admin
from productapp.models import Cart


class Cartadmin(admin.ModelAdmin):
    list_display = ['pid', 'units', 'unitprice', 'tuprice']
    list_filter = ['pid']

    class Meta:
        model = Cart


admin.site.register(Cart, Cartadmin)

