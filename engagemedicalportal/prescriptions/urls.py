from django.urls import path
from prescriptions import views
urlpatterns = [
    path('', views.prescriptions, name = "prescriptions"),
    # path('mailprescription', views.mailprescription, name = "mailprescription"),
    path('delete_prescription/<int:pk>', views.delete_prescription, name = "delete_prescription"),
    path('<int:pk>', views.Prescriptiondetailview.as_view(), name = "prescriptiondetail"),
    path('duplicateprescription/<int:pk>', views.duplicateprescription, name = "duplicateprescription"),
    # path('api/upload/xray', UploadView.as_view(), name = 'prediction'),
    # path('api/upload/ct', CTUploadView.as_view(), name = 'ct_prediction'),
    # # path('notedetail/updatenote', views.updatenote, name = "updatenote"),
    # # path('homework', views.homework, name = "homework")

]