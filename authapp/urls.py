from django.urls import path
from . import views
app_name = 'authapp'
urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('signup/otpvalidation', views.otpvalidation),
    path('my_logout', views.my_logout),
 ]

