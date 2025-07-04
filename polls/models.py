from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text: str = models.CharField(max_length=200)
    pub_date: datetime = models.DateTimeField("date published")

    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question: models.ForeignKey = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
