from django.urls import path
from prova import views

urlpatterns = [
    path('test/<int:post_id>', views.test_view),
]
