from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required(login_url='/')
def prescriptions(request):
    if request.method == "POST":
        form = Prescriptionsform(request.POST)
        if form.is_valid():
            note = Prescriptions(user=request.user,patient=request.POST['patient'],description=request.POST['description'],email=request.POST['email'])
            user=request.user
            description=request.POST['description']
            patient=request.POST['patient']
            email=request.POST['email']
            note.save()
            send_mail('Prescription for '+ patient+': Doctor - ' + user.username, description,settings.EMAIL_HOST_USER,[email],fail_silently=False )
        messages.success(request,f"Prescription added and mailed successfully")
    else:
        form = Prescriptionsform()
    prescriptions = Prescriptions.objects.filter(user = request.user)
    context = {"prescriptions" : prescriptions, "form" : form}
    return render(request, 'prescriptions/prescriptions.html', context)

@login_required(login_url='/')
def delete_prescription(request,pk=None):
    Prescriptions.objects.get(id=pk).delete()
    messages.success(request,f"Prescription deleted successfully")
    return redirect("prescriptions")

class Prescriptiondetailview(generic.DetailView):
    model = Prescriptions

@login_required(login_url='/')
def duplicateprescription(request,pk=None):
    note = Prescriptions.objects.filter(user = request.user, id=pk)
    note1 = note[0]
    note1.id = None
    note1.save()
    messages.success(request,f"Prescription duplicated successfully")
    return redirect("prescriptions")

