from django.urls import path
from .views import SignUpViews
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', SignUpViews.as_view(), name='signup'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)