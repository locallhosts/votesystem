from django.db import models

from django.db import models


# Create your models here.
# The Question class is a model that has a question_text and a pub_date.
# The Choice class is a model that has a question, a choice_text, and a votes.
#
# The Question class has a ForeignKey that links each Choice to a single Question.
# The Question class is said to have a relationship to the Choice class,
# because it has a ForeignKey

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


# The Choice model is a database table that has two fields: choice_text and votes.
#
# Each Choice is associated with a Question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



