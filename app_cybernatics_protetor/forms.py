import re
from django import forms
from app_cybernatics_protetor.models import Defence_Login,Staff,CreateAgent,adminlogin
class Defenceform(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model=Defence_Login
        fields="__all__"
    def user(self):
        username=self.cleaned_data['username']
        check=re.findall('^[A-Za-z]*$',username)
        if check:
            return username
        else:
            raise forms.ValidationError("Must use correct format A-Z and a-z")

class Staff_validation(forms.ModelForm):
    Username=forms.CharField(help_text="Must be Char's Only")
    Password=forms.CharField(label="Password", widget=forms.PasswordInput)
    Email=forms.EmailField(label="Email",widget=forms.EmailInput)
    Contact=forms.IntegerField(help_text="Must be 10 digit Only")
    class Meta:
        model=Staff
        fields=('Username','Contact','Email','Password','Photo')
        labels={'Username':'Username','Contact':'Contact'}

class Agent(forms.ModelForm):
    Agent_Name = forms.CharField(help_text="Must be Char's Only")
    Email = forms.EmailField(label="Email", widget=forms.EmailInput)
    Password = forms.CharField(label="Password", widget=forms.PasswordInput,help_text="change password or use old password")
    class Meta:
        model=CreateAgent
        fields="__all__"

class Adminform(forms.ModelForm):
    username = forms.CharField(help_text="Must be Char's Only")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = adminlogin
        fields = ('username','password','department','photo')

