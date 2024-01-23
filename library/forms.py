from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'enrollment_no', 'password1', 'password2', 'pic')


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password')
    
    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid login")
        return cleaned_data



class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'name', 'username', 'pic')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

