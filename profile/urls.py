from . import views
from django.urls import path
from .views import ProfileListView

app_name = 'profile'

urlpatterns = [
     path('',ProfileListView.as_view(),name='profile_list'),
]
