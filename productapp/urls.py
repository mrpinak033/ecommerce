from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'productapp'
urlpatterns = [
    path('search', views.search),
]
