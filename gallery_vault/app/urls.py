from django.urls import path
from . import views

urlpatterns = [
    path('',views.gal_login),
    path('gal_home',views.gal_home),
    path('gal_logout',views.gal_logout),
    path('register',views.register),









#*********************USER*******************
path('user_home',views.user_home),
path('file_upd',views.file_upd),



]