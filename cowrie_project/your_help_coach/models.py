from django.db import models

# Create your models here.

class CowrieLogAttack(models.Model):
    attack_name = models.CharField(max_length=255)
    description = models.TextField(default = "no description available")
    affected = models.TextField()
    mitigation = models.TextField() 
    solutions = models.TextField()
    learn_more = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.attack_name

    def get_learn_more_links(self):
        """Splits the learn_more field into a list of URLs."""
        return self.learn_more.split(', ') if self.learn_more else []



