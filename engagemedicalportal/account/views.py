from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login
from .authenticate import FaceIdAuthBackend
from .utils import prepare_image

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            face_image = prepare_image(form.cleaned_data['image'])
            face_id = FaceIdAuthBackend()
            user = face_id.authenticate(
                username=username, 
                password=password,
                face_id=face_image
                )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg= 'Invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})

def home(request):
    return render(request,'account/home.html')

def viewdb(request):
    return render(request,'viewdb.html')