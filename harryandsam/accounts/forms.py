from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import authenticate



from .models import Accounts

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required, please add a valid email address.')
    number = PhoneNumberField(help_text='We prefer your mobile number if possible. ')
    waiver = forms.BooleanField(help_text='By ticking this box, you agree to the policies and waivers listed above.', label='I Agree')

    class Meta:
        model = Accounts
        fields = ('email','username', 'first_name','last_name','number','address','sprc','city','postal','password1','password2','waiver')

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Accounts
        fields = ('email','password')
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('email','username', 'first_name','last_name','number','address','sprc','city','postal')

    def clean_email(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            try:
                email = Accounts.objects.exclude(pk=self.instance.pk).get(email=email)
            except Accounts.DoesNotExist:
                return email
            raise forms.ValidationError('username "%s" is already in use.' % account.email)


    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data['username']
            try:
                account = Accounts.objects.exclude(pk=self.instance.pk).get(username=username)
            except Accounts.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use.' % account.username)

