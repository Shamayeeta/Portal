from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login,logout
from .authenticate import check_user,face_exists
from .utils import prepare_image
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#returns main page for login or register
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        face_id = face_exists()
        if form.is_valid():
            face_image = prepare_image(form.cleaned_data['image'])
            if face_id.check_face_exists(face_id=face_image):
                user = form.save()                    
                # messages.success(request,f"User Created Succesfully.")
                return redirect('login_view')
        #     else:
        #         messages.success(request,f"No face detected. Please register again.")
        # else:
        #     messages.success(request,f"Form is not valid.")
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            face_image = prepare_image(form.cleaned_data['image'])
            face_id = check_user()
            user = face_id.authenticate(
                username=username, 
                password=password,
                face_id=face_image
                )
            if user is not None:
                login(request, user)
                return redirect('home')
        #     else:
        #         messages.success(request,f"Invalid Credentials.")
        # else:
        #     messages.success(request,f"Error Validating Form.")
    return render(request, 'account/login.html', {'form': form})

@login_required(login_url='/')
def home(request):
    return render(request,'account/home.html')

#returns view database page for patients
@login_required(login_url='/')
def viewdb(request):
    return render(request,'database/viewdb.html')

@login_required(login_url='/')
def Logout(request):
    logout(request)
    return render(request, 'index.html')