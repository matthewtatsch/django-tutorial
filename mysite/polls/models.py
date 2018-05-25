"""
polls models
"""

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Question model

    A question with text and a published date.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Indicates if question was published within the last 1 days.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Choice model

    Choice to be associated with a question.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
