from django import contrib
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
