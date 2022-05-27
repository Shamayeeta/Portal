from django.urls import path
from prescriptions import views
urlpatterns = [
    path('', views.prescriptions, name = "prescriptions"),
    path('delete_prescription/<int:pk>', views.delete_prescription, name = "delete_prescription"),
    path('<int:pk>', views.Prescriptiondetailview.as_view(), name = "prescriptiondetail"),
    path('duplicateprescription/<int:pk>', views.duplicateprescription, name = "duplicateprescription"),
]