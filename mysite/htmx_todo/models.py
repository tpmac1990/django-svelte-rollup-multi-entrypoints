from django.db import models


class Todo(models.Model):
    item = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item
