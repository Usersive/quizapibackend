from django.contrib import admin

from quizapp.models import Student, Question, QuestionOption, QuizConfig, QuizSetting

# Register your models here.
# from django.contrib.auth.models import User

# admin.site.register(User)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricNum', 'score', 'status')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'is_correct', 'question')

admin.site.register(QuizSetting)
admin.site.register(QuizConfig)