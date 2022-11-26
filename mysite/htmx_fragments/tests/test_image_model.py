# from django.test import TestCase

from htmx_fragments.models import Image
from common.test_utils import BaseTest
from common.factories import ImageFactory

class ImageTests(BaseTest):

    def test_image_fields(self):
        """Image fields as expected"""
        ImageFactory.create(title="image 1", image="data/web/media/images/IMG_20220528_155841.jpg")
        img = Image.objects.first()
        self.assertEqual(img.title, 'image 1')
