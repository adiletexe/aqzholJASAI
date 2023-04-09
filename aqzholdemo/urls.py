"""aqzholdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from aqzhol import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #telephone
    path('admin/', admin.site.urls),
    path('next', views.next, name='next'),
    path('info/<int:info_pk>/', views.info, name='info'),
    path('info2/<int:info_pk>/', views.info2, name='info2'),
    path('info3/<int:info_pk>/', views.info3, name='info3'),

    #computer
    path('admin/', admin.site.urls),
    path('nextcomp', views.nextcomp, name='nextcomp'),
    path('infocomp/<int:info_pk>/', views.infocomp, name='infocomp'),
    path('info2comp/<int:info_pk>/', views.info2comp, name='info2comp'),
    path('info3comp/<int:info_pk>/', views.info3comp, name='info3comp'),
    path('comp', views.loginsystemcomp, name='loginsystemcomp'),
    path('logoutcomp/', views.logoutsystemcomp, name='logoutsystemcomp'),

    #authentication
    path('', views.loginsystem, name='loginsystem'),
    path('logout/', views.logoutsystem, name='logoutsystem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

