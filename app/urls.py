from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.home,name='home'),

    path('login/',views.user_login,name='login'),

    path('logout/',views.user_logout,name='logout'),


    path('bank_get',views.bank_get,name='bank_get'),
    path('bank_give',views.bank_give,name='bank_give'),

    path('telecom_get/',views.telecom_get,name='telecom_get'),
    path('telecom_give/',views.telecom_give,name='telecom_give'),

    path('cement_get/',views.cement_get,name='cement_get'),
    path('cement_give/',views.cement_give,name='cement_give'),

    path('personal_get/',views.personal_get,name='personal_get'),
    path('personal_give/',views.personal_give,name='personal_give'),

    path('home/',views.home,name='home'),
    path('rahi/',views.rahi,name='rahi'),

]
