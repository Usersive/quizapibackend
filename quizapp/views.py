from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from quizapp.models import Question, QuizConfig,  QuizSetting, Student
from quizapp.serializers import QuestionSerializer, QuizSettingSerializer
from rest_framework.decorators import api_view
import random
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def questions(request):
    quiz_config = QuizConfig.objects.first()
    num_questions = quiz_config.num_questions if quiz_config else 5  # Default to 5 if not set

    all_questions = list(Question.objects.all())
    selected_questions = random.sample(all_questions, min(num_questions, len(all_questions)))

    serializer = QuestionSerializer(selected_questions, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def has_taken_quiz(request):
    matricNum = request.data.get("matricNum", "").upper()
    
    # Check if student exists in the system
    student = Student.objects.filter(matricNum=matricNum).first()
    if not student:
        return Response({"error": f"{matricNum} is not registered and cannot take the quiz"}, status=status.HTTP_403_FORBIDDEN)

    # Check if the student has already taken the quiz
    if student.status == "done":
        return Response({"error": f"{matricNum} has already taken the quiz and cannot retake it"}, status=status.HTTP_403_FORBIDDEN)

    return Response({"message": "Proceed to take your quiz"})



@api_view(['POST'])
def submit_quiz(request):
    matricNum = request.data.get("matricNum", "").upper()
    score = request.data.get("score")

    student = Student.objects.filter(matricNum=matricNum).first()
    if not student:
        return Response({"error": f"{matricNum} is not registered"}, status=status.HTTP_404_NOT_FOUND)

    student.score = score
    student.status = "done"
    student.save()

    return Response({"message": "Quiz submitted successfully!"})


@api_view(['GET'])
def quiz_settings(request):
    check = QuizSetting.objects.first()
    if check:
        serializer = QuizSettingSerializer(check)
        return Response(serializer.data)
    return Response({"error": "Quiz configuration not found"}, status=404)