from django import forms
from .models import Profile
    


class RegisterForm(forms.Form):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  user_name = forms.CharField(max_length=100)
  email = forms.EmailField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput())
  confirm_password = forms.CharField(widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):
  avatar = forms.ImageField(widget=forms.FileInput)
  class Meta:
    model = Profile
    fields = ('first_name', 'last_name', 'avatar', 'website', 'location', 'bio', 'email', 'facebook', 'twitter', 'pinterest', 'instagram')



