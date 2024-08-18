from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from demoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
