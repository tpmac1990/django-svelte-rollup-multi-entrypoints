from django.db import models
from django.db.models.functions import Lower
from registration.models import User
from django_extensions.db.fields import AutoSlugField


class Film(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='films', through='UserFilms')
    photo = models.ImageField(upload_to='film_photos', null=True, blank=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = [Lower('name')]

    def slugify_function(self, content):
        return content.replace('_', '-').lower()

class UserFilms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']