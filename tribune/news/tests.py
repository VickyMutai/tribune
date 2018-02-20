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

    # def test_delete_method(self):
    #     self.vicky.save_editor()
    #     editors=Editor.objects.all()
    #     self.vicky.delete_editor()
    #     self.assertTrue(len(editors)<1)

class ArticleTestClass(TestCase):
    def setUp(self):
        #creating a new editor and saving it
        self.vicky = Editor(first_name = 'Vicky',last_name = 'Toms',email='vicky@legacy.com')
        self.vicky.save_editor()
        
        #creating a new tag and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Sports',post='Sports post',editor=self.vicky)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_article,Article))

    # def test_save_method(self):
    #     self.new_article.save_article()
    #     articles = Article.objects.all()
    #     self.assertTrue(len(articles)>0)

    # def test_delete_method(self):
    #     self.new_article.save_article()
    #     articles = Article.objects.all()
    #     self.new_article.delete_article()
    #     self.assertTrue(len(articles)<1)