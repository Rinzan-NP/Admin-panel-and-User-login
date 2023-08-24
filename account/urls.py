from django.urls import path,include
from . import views

urlpatterns = [

    path('signup/',views.register,name='register'),
    path('login/',views.logining, name = 'login'),
    path('', views.logining),
    path('home/',views.home,name = 'home'),
    path('logout/',views.logouting, name = 'logout')
]
