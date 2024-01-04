from django.db import models
from ckeditor.fields import RichTextField

class Question(models.Model):
    question_text = RichTextField()
    pub_date = models.DateTimeField("date published")
