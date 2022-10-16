from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name