from django.urls import path
from . import views
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('create', views.createClient, name='createInfo'),
    path('view', views.showClient, name='viewInfo'),
    path('add', views.saveInfo, name='addInfo'),
    path('edit/<int:id>', views.editInfo, name='editInfo'),
    path('delete/<int:id>', views.deleteInfo, name='deleteInfo'),
    path('fullInfo/<int:id>', views.fullInfo, name='fullInfo'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)