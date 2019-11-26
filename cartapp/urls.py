from django.urls import path
from . import views
app_name = 'cartapp'
urlpatterns = [
    path('addcart', views.addcart),
    path('insertcart', views.insertcart),
    path('viewcart', views.cart),
    path('display', views.display),
    path('deletecart', views.deletecart),
    path('modifycart', views.modifycart),
    path('modifiedcart', views.modifiedcart),
 ]

