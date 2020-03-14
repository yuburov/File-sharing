from django.contrib.auth.models import User
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('accounts:login')

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

