"""
URL configuration for phd_admission_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #type:ignore
from applications import views #type:ignore


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signup, name="signup"),
    path('', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('index/',views.index,name='index'),
    path('personal/', views.personal, name='personal'),
    path('School_form/', views.School_form, name='School_form'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('master/', views.Masterform, name='Masterform'),
    path('experience', views.experience, name='experience'),
    path('guide/', views.guide_view, name='guide_view'),
    path('Dcmember', views.dc_member_view, name='dc_member_view'),
    path('approval/', views.approval_view, name='approval'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),
    path('check_form',views.check_form,name='check_form'),
    path('approving',views.approving,name='approving'),


    path('Dcmembers/check_register_number', views.check_register_number, name="check_register_number"),
    path('generate_qrcode/', views.generate_qrcode, name='generate_qrcode'),
    path('display_qrcode/', views.display_qrcode, name='display_qrcode'),



        path('check_form',views.check_form,name='check_form'),
        path('edit_form/', views.edit_form, name="edit_form"),

    path('upload_images/<str:register_number>/', views.upload_images, name='upload_images'),



]
