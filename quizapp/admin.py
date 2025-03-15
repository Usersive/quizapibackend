from django.contrib import admin

from quizapp.models import Student, Question, QuestionOption, QuizConfig, QuizSetting

# Register your models here.
# from django.contrib.auth.models import User

# admin.site.register(User)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['matricNum', 'score', 'status']
    list_display_links= ['matricNum']
    search_fields = ['matricNum', 'score', 'status']
    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ['question']

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'is_correct', 'question')


@admin.register(QuizSetting)
class QuizSettingAdmin(admin.ModelAdmin):
    list_display = ['seconds_per_question', 'score_per_question']

@admin.register(QuizConfig)
class QuizConfigAdmin(admin.ModelAdmin):
    list_display = ['num_questions']

  