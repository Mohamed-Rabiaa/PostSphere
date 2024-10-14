from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django import forms
from .models import User

class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', max_length=50,
                                       widget=forms.PasswordInput)

    # Custom validation for the password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match.')
        return cleaned_data

    # Unique email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    # Password validation
    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Ensure email is in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Invalid Email.")

        # Check if password matches
        if not user.check_password(password):
            raise ValidationError("Invalid Password.")

        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'image']
