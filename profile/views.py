from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Profile
from django.urls import reverse_lazy

# Create your views here.


class ProfileListView(ListView):
    ListView.model  = Profile
    ListView.template_name = 'profile/profile_list.html'
    ListView.context_object_name = 'profile_list'

class ProfileCreateView(CreateView):
    model = Profile
    template_name = "profile/profile_create.html"
    fields= '__all__'
    success_url = reverse_lazy('profile:list')
    
