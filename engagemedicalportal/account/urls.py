from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('viewdatabase/',views.viewdb,name='viewdatabase')
    # path('doctor/', views.doctor, name='doctor'),
    # path('patient/', views.patient, name='patient'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)