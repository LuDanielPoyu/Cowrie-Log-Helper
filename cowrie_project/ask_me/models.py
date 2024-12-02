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
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add = True)
    input_log = models.TextField(default = "None")
    attack_type = models.CharField(max_length = 128)
    actual_type = models.CharField(max_length = 128)
    probability = models.TextField(default = "None")


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