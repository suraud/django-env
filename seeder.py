import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

django.setup()

from django.utils import timezone
from polls.models import Question, Choice

questions = [
    {"question_text": "hoge1", "pub_date": timezone.now()},
    {"question_text": "hoge2", "pub_date": timezone.now()},
    {"question_text": "hoge3", "pub_date": timezone.now()},
    {"question_text": "hoge4", "pub_date": timezone.now()},
    {"question_text": "hoge5", "pub_date": timezone.now()},
]

for question in questions:
    q = Question(**question)
    q.save()

choices = [
    {"choice_text": "piyo1", "votes": 0},
    {"choice_text": "piyo2", "votes": 0},
    {"choice_text": "piyo3", "votes": 0},
    {"choice_text": "piyo4", "votes": 0},
    {"choice_text": "piyo5", "votes": 0},
]

for choice in choices:
    q = Question.objects.get(pk=1)
    q.choice_set.create(**choice)

choices = [
    {"choice_text": "fuga1", "votes": 0},
    {"choice_text": "fuga2", "votes": 0},
    {"choice_text": "fuga3", "votes": 0},
    {"choice_text": "fuga4", "votes": 0},
    {"choice_text": "fuga5", "votes": 0},
]

for choice in choices:
    q = Question.objects.get(pk=2)
    q.choice_set.create(**choice)