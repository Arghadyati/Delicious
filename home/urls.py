from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),
    path('signup',views.handelsignup,name='handelsignup'),
    path('login',views.handellogin,name='handellogin'),
    path('logout',views.handellogout,name='handellogout')

]