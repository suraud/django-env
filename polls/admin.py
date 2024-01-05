from polls.models import Choice, Question
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    """ fields = ["question_text", "pub_date"] """
    fieldsets = [
        ("テキスト編集", {"fields": ["question_text"]}),
        ("日付変更", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
