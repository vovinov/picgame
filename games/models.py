from django.db import models


class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    questions = models.ForeignKey(to='questions.QuestionList', on_delete=models.CASCADE)
