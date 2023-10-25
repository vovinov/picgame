from django.db import models


class QuestionList(models.Model):
    pass


class Question(models.Model):
    title = models.TextField(default="Угадайте что за фильм?")
    image = models.ImageField(upload_to='photo/%Y/%m/%d', null=True)
    difficult = models.IntegerField(default=1)


