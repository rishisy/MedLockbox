from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'main/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MedicalRecord
from .forms import MedicalRecordForm

@login_required
def create_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()  # The 'patient' field is already set in the form
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm(user=request.user)

    return render(request, 'main/create_medical_record.html', {'form': form})

from rest_framework import generics
from rest_framework.response import Response
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class MedicalRecordListByAadhaar(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        aadhaar_number = self.kwargs['aadhaar_number']
        return MedicalRecord.objects.filter(aadhaar_number=aadhaar_number)