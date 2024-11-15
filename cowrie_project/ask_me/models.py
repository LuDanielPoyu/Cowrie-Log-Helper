from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AttackType(models.Model):
    attack_type = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.attack_type


class Tips(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class ClassificationHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length = 256, null = True)
    input = models.CharField(max_length = 256, null = True)
    protocol = models.CharField(max_length = 256, null = True)
    duration = models.CharField(max_length = 256, null = True)
    dataAttr = models.CharField(max_length = 256, null = True)
    keyAlgs = models.CharField(max_length = 256, null = True)
    message = models.CharField(max_length = 256, null = True)
    eventid = models.CharField(max_length = 256, null = True)
    kexAlgs = models.CharField(max_length = 256, null = True)
    attack_type = models.CharField(max_length = 128)


class QAHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    question = models.TextField()
    answer = models.TextField()


class SummaryHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    paragraph = models.TextField()
    summary = models.TextField()