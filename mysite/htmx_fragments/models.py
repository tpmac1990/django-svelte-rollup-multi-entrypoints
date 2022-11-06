from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title