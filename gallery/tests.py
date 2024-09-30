from django.test import TestCase, override_settings
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

import tempfile
from .models import ImagePost
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

class ImagePostModelTests(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_image_name_description(self):
        """
        Tests ImagePost's string representation and description.
        """
        small_gif = (b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
                    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
                    b'\x02\x4c\x01\x00\x3b')
        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        post = ImagePost.objects.create(image=image, description="DUMMY")
        self.assertTrue(isinstance(post, ImagePost))
        self.assertEqual(post.__str__(), "/media/images/small.gif")
        self.assertEqual(post.description, "DUMMY")

