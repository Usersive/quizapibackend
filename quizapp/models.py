from django.db import models

# Create your models here.

class Student(models.Model):
    matricNum = models.CharField(max_length=20, unique=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='active')
    
    def __str__(self):
        return self.matricNum
    
class Question(models.Model):
    question = models.CharField(max_length=500, unique=True)
    
    def __str__(self):
        return self.question


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.option} for {self.question.question}"

class QuizConfig(models.Model):
    num_questions = models.IntegerField( default=5)
    
    def __str__(self):
        return f" QuizConfig: {self.num_questions} questions"

class QuizSetting(models.Model):
    seconds_per_question = models.IntegerField(default=0)
    score_per_question = models.IntegerField(default=1) 
    
    def __str__(self):
        return f"Seconds Per Question: {self.seconds_per_question}, Score Per Question: {self.score_per_question}"
    

