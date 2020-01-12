from . import views
from django.urls import path

app_name = 'foosball'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'), #TODO: Flytt hjemmesiden til en egen dashboard app som ikke er Foosball-spesifikk
]
