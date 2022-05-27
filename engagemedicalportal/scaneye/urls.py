from django.contrib import admin
from django.urls import path
from scaneye import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.scaneye,name='scaneye'),
    path('predictImage',views.predictImage,name='predictImage'),
    path('viewDataBaseeye',views.viewDataBase,name='viewDataBaseeye'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
