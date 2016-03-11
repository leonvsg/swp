from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=False)
    author = models.ForeignKey(User, related_name='question_set_1', null=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)
    def __unicode__(self):
        return self.title
    def get_url(self):
        return '/question/%d/' %self.id
    class Meta:
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User)
