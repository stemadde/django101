from django.urls import path
from prova import views

urlpatterns = [
    path('test/<int:post_id>', views.test_view),
    path('test/<int:post_id>/comments', views.commentView)
]

# By writing a path here redirecting to a view, I can load said view through the defined path written in the browser
# Therefore, if I want to create a new view which allows for comment insertion, I need to define a new path, triggered
# by a link, that sends the user to the path defined as entry point for the commentView