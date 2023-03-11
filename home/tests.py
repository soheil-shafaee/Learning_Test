from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user1")
        self.post1 = Post.objects.create(
            title="Post1",
            text="This is Post 1",
            status=Post.STATUS_CHOICES[0][0],
            author=self.user
        )
        self.post2 = Post.objects.create(
            title="Post2",
            text="This is Post 2",
            status=Post.STATUS_CHOICES[1][0],
            author=self.user
        )

    def test_post_by_urls(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_post_urls_by_name(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_text(self):
        response = self.client.get("")
        self.assertContains(response, "This is Post 1")

    def test_post_pub(self):
        response = self.client.get("")
        self.assertContains(response, self.post1.text)
