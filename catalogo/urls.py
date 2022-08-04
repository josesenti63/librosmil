from django.urls import include, path 
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('__debug__/', include('debug_toolbar.urls'),)
    ]