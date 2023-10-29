from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

from .models import MedicalRecord

from django import forms
from .models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['date_of_visit', 'type_of_record', 'medical_notes', 'image', 'aadhaar_number']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.patient = user  # Set the user for the current instance


