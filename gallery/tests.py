from django.test import TestCase, override_settings
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

import tempfile
from .models import ImagePost
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

small_gif = (b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b')

class ImagePostModelTests(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_image_name_description(self):
        """
        Tests ImagePost's string representation and description.
        """
        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        post = ImagePost.objects.create(image=image, description="DUMMY")
        self.assertTrue(isinstance(post, ImagePost))
        self.assertEqual(post.__str__(), "/media/images/small.gif")
        self.assertEqual(post.description, "DUMMY")

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_add_tags(self):
        """
        Tests adding tags to ImagePost using update_tags().
        """

        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        post = ImagePost.objects.create(image=image, description="DUMMY")
        tags = ['gif', 'black', 'white', 'post']
        post.update_tags(tags)
        self.assertEqual(set(post.tags.names()), set(tags))
        
    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_remove_tags(self):
        """
        Tests adding then removing some tags from an ImagePost using update_tags().
        """

        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        post = ImagePost.objects.create(image=image, description="DUMMY")
        tags = ['gif', 'black', 'white', 'post']
        post.update_tags(tags)
        post.update_tags(['gif', 'black'])
        self.assertEqual(set(post.tags.names()), set(['gif', 'black']))

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_remove_all_tags(self):
        """
        Tests adding then removing all tags from an ImagePost using update_tags().
        """

        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        post = ImagePost.objects.create(image=image, description="DUMMY")
        tags = ['gif', 'black', 'white', 'post']
        post.update_tags(tags)
        post.update_tags([])
        self.assertTrue(not post.tags.all())



'''
# views (uses reverse)

    def test_whatever_list_view(self):
        w = self.create_whatever()
        url = reverse("whatever.views.whatever")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)
'''

