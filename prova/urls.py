from django.urls import path
from prova import views

urlpatterns = [
    path('test', views.test_view),
]
