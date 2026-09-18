"""
URL configuration for smart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from patient_data import views
from django.conf.urls.static import static

from patient_data.views import views_doctor
from.import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navigation_bar/',views.navigation_bar,name='navigation_bar'),
    path('register/', views.register, name='register'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('aboutus/', views.aboutus, name='about'),
    path('contactus/', views.contactus, name='contact'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('views_doctor/', views.views_doctor, name='view_doctor'),
    path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_patient/', views.views_patient, name='view_patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('delete_patient/<int:pid>/', views.delete_patient, name='delete_patient'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('logout/', views.logout_admin, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('view_prescription/',views.view_prescription, name='view_prescription'),
path( 'delete_prescription/<int:pid>/', views.delete_prescription, name='delete_prescription' ),
]
