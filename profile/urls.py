from . import views
from django.urls import path
from .views import ProfileListView,ProfileCreateView

app_name = 'profile'

urlpatterns = [
     path('',ProfileListView.as_view(),name='list'),
     path('create/',ProfileCreateView.as_view(), name='create')
]
