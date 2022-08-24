from django.test import TestCase
from prova.models import *
from prova.crud import *

class databaseTesting(TestCase):
    User1 = None
    User2 = None

    def setUp(self):
        self.User1 = User.objects.create_user(username="gigi",email="gigiemail@gmail.com", password="Gigipass6+")
        self.User2 = User.objects.create_user(username="luca",email="lucaemail@gmail.com", password="Lucapass6+")
        self.User1.first_name = "Giovanni"
        self.User2.first_name = "Luca"
        self.User1.save()
        self.User2.save()

    # Creation works
    # DONE: Getter method has some problem, gonna test direct get tomorrow
    # fixed, i forgor ( :) ) that user was actually a model
    def test_creation(self):
        rt1 = create_blog_post("Primo", "Testo del primo", self.User1, "FF0000")
        rt2 = create_blog_post("Secondo", "Testo del secondo", self.User2, "FF0000")
        rt1.save()
        rt2.save()
        self.assertEqual(rt1.user.first_name, "Giovanni")
        self.assertEqual(rt2.user.first_name, "Luca")
        self.assertEqual(rt1.user.username, "gigi")
        self.assertEqual(rt2.user.username, "luca")
        # print(BlogPost.objects.get(id=1).user.first_name)
        # print(rt1.hash)
        # print(rt2.hash)
        # print(rt1.id)
        # print(rt2.id)

    # Deletion works
    def test_deletion(self):
        rt1 = create_blog_post("Primo", "Testo del primo", self.User1, "FF0000")
        rt2 = create_blog_post("Secondo", "Testo del secondo", self.User2, "FF0000")
        rt1.save()
        rt2.save()
        self.assertEqual(delete_blog_post(self.User1, rt1.id), 204)
        self.assertEqual(delete_blog_post(self.User2, rt2.id), 204)

        self.assertEqual(get_blog_post(user=self.User1, post_id=1), None)
        self.assertEqual(get_blog_post(user=self.User2, post_id=2), None)

    # Update works
    def test_getter(self):
        self.test_creation()
        self.assertEqual(get_blog_post(self.User1, 1).user.first_name, "Giovanni")
        self.assertEqual(get_blog_post(self.User2, 2).user.first_name, "Luca")
        self.assertEqual(get_blog_post(self.User1, 1).user.username, "gigi")
        self.assertEqual(get_blog_post(self.User2, 2).user.username, "luca")

    # Update works, but doesn't update the user, another crud is needed
    def test_update(self):
        self.test_creation()
        updated_blog_post(self.User1, 1, title='amarolucano').save()
        updated_blog_post(self.User2, 2, title='amarodelcapo').save()
        self.assertEqual(get_blog_post(self.User1, 1).title, 'amarolucano')
        self.assertEqual(get_blog_post(self.User2, 2).title, 'amarodelcapo')
