from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on', 'id']
        indexes = [models.Index(fields=['created_on'])]

    def __str__(self):
        return self.title

