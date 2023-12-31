from doctor.models import Doctor, DoctorsProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

class DoctorStatusForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['is_active']
        
class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model=Doctor
        fields=('bmdc_registration_number','name', 'email', 'phone','fees','about','doc_image','department','password1','password2')
        

class DoctorLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    class Meta:
        model=Doctor
        fields=('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid Credentials")
            
            
class DoctorProfileUpdate(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['id','name','email','phone','fees','about','department']

class DoctorProfileDetails(forms.ModelForm):
    class Meta:
        model = DoctorsProfile
        exclude=['doctor_id']
            
            