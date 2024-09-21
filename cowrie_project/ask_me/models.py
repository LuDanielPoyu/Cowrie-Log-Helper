from django.db import models

# Create your models here.
class AttackType(models.Model):
    attack_type = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.attack_type


