from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Post,Comment


class SignupForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','email','username','password1','password2']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','category','image','detail']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['author','title']