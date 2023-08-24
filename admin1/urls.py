from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin, name = 'adminlogin'),
    path('dashboard/',views.dashboard, name= 'dashboard'),
    path('dashboard/user',views.users, name = 'user'),
    path('dashboard/adduser',views.adduser, name = 'adduser'),
    path('dashboard/deleteuser',views.deleteuser, name="delete user"),
    path('dashboard/update', views.updateuser , name='update user'),
    path('dashboard/updateuserdata', views.user_update_data, name='updating data'),
    path('dashboard/search',views.search_user,name='searching'),
    path('dashboard/search_back',views.search_back,name='go back'),
    path('dashboard/view_data',views.view_data,name='View'),
    path('dashboard/logout',views.logouting,name='Log out'),

]
