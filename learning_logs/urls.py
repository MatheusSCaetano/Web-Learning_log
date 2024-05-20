from django.urls import path
from learning_logs import views


urlpatterns = [
    path('', views.index),
 
]