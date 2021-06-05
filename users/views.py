from django.shortcuts import render
from django.views import generic 
from .forms import UserCreation
from django.urls import reverse_lazy
class SignUpView(generic.CreateView):
    form_class = UserCreation
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"