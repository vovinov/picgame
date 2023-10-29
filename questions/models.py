from django.db import models
from django.urls import reverse


class QuestionList(models.Model):
    difficult = models.IntegerField()

    def get_abolute_url(self):
        return reverse('game', kwargs={'id': self.id})


class Question(models.Model):
    title = models.TextField(default="Угадайте что за фильм?")
    image = models.ImageField(upload_to='photo/%Y/%m/%d', null=True)
    difficult = models.IntegerField(default=1)


