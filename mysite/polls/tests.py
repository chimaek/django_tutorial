import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_question_count(self):
        Question.objects.create(question_text="test",pub_date=timezone.now())
        self.assertEqual(Question.objects.count(),1)

    def test_question_instance(self):
        Question.objects.create(question_text="test",pub_date=timezone.now())
        self.assertIsInstance(Question.objects.first(),Question)

    def test_question_update(self):
        question = Question.objects.create(question_text="test",pub_date=timezone.now())
        question.question_text = "update"
        question.save()
        self.assertEqual(Question.objects.first().question_text,"update")

    def test_delete_question(self):
        question = Question.objects.create(question_text="test",pub_date=timezone.now())
        question.delete()
        self.assertEqual(Question.objects.count(),0)

    def test_num1(self):
        li = [x for x in range(1,101)]
        self.assertEqual(sum(li),5050)
        self.assertEqual(len(li),100)

    def test_num2(self):
        dic = {x:x**2 for x in range(1,11)}
        self.assertEqual(sum(dic.values()),385)

    def test_num3(self):
        dic = {"x":1,"y":2,"z":3}
        self.assertIsInstance(dic,dict)

    def test_num4(self):
        data = None
        self.assertIsNone(data)

    def test_num5(self):
        data = False
        self.assertFalse(data)

