
from django.urls import path
from . import views

urlpatterns = [
    path("questions", views.questions, name="questions"),
    path("has_taken_quiz/", views.has_taken_quiz, name="has_taken_quiz"),
    path("submit_quiz/", views.submit_quiz, name="submit_quiz"),
    path('quiz_settings/', views.quiz_settings, name="quiz_settings"),
    
]
