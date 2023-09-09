from django.urls import path
from . import views

urlpatterns = [
    path('', views.email, name='send_email'),
]
