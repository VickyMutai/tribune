from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.vicky = Editor(first_name = 'Vicky',last_name = 'Toms',email='vicky@legacy.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.vicky,Editor))

    #testing save method
    def test_save_method(self):
        self.vicky.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_delete_method(self):
        self.vicky.save_editor()
        editors=Editor.objects.all()
        self.vicky.delete_editor()
        self.assertTrue(len(editors)<1)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.vicky = Editor(first_name = 'Vicky',last_name = 'Toms',email='vicky@legacy.com')
        self.vicky.save_editor()
        self.Sports = Article(title = 'Sports',post='Sports post',editor=self.vicky)

    def test_instance(self):
        self.assertTrue(isinstance(self.Sports,Article))

    def test_save_method(self):
        self.Sports.save_article()
        articles = Article.objects.all()
        self.assertTrue(len(articles)>0)

    def test_delete_method(self):
        self.Sports.save_article()
        articles = Article.objects.all()
        self.Sports.delete_article()
        self.assertTrue(len(articles)<1)