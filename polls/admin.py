from django.contrib import admin

from polls.models import Question
admin.site.register(Question)

from polls.models import Choice
admin.site.register(Choice)
