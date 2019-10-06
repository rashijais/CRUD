from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic




def index(request):
	return HttpResponse('Heyya, Blogger ? ')

class RegisterUserView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'register.html'
	success_url = reverse_lazy('login')