from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('recipe:index')


class RegisterView(View):
    def get(self, request):
        form_class = CustomUserCreationForm
        return render(request, 'myauth/register.html', {'form': form_class})

    def post(self, request):
        form_class = CustomUserCreationForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            return redirect('recipe:index')
        return render(request, 'myauth/register.html', {'form': form_class})
