from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

# delete the image from s3 bucket
@receiver(models.signals.post_delete, sender=Image)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image.delete(save=False)