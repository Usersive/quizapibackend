from rest_framework import serializers
from .models import Student, Question, QuestionOption,QuizSetting


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ["id", "matric_number", "score", "status"]




class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ["id", "question", "option", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ["id", "question", "options"]
        
        
class QuizSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSetting
        fields = ["seconds_per_question", "score_per_question"]