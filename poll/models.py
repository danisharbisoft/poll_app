from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def check_recency(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f'Question:{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=70)
    votes = models.IntegerField(default=0)
