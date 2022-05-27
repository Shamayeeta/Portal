from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserFaceImage,User
from .utils import base64_file
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    image = forms.CharField(widget=forms.HiddenInput())


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    image = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 
                'email', 
                'password1', 
                'password2', 
                'is_doctor', 
                'is_patient'
                )


    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't Create User Without Database Save")
        user = super(SignUpForm, self).save(commit=True)
        image = base64_file(self.data['image'])
        face_image = UserFaceImage(user=user, image=image)
        face_image.save()
        return user
