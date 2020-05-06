import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    """A question has a question and a publication date"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return a string representation of the model"""
        return self.question_text

    def was_published_recently(self):
        """Published within the last day"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """A choice has text and an vote tally"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return a string representation of the model"""
        return self.choice_text
