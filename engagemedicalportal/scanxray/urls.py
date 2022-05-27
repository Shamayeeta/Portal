from django.urls import path
from scanxray import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.scanxray,name='scanxray'),
    path('predictImage',views.predictImage,name='predictImage'),
    path('viewDataBasexray',views.viewDataBase,name='viewDataBasexray'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
