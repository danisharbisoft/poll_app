from django.test import TestCase
from .models import Question
from django.utils import timezone
import datetime
from django.urls import reverse


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future = Question(pub_date=time)
        self.assertIs(future.check_recency(), False)

    def test_ws_published_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        future = Question(pub_date=time)
        self.assertIs(future.check_recency(), False)

    def test_was_published_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=14, minutes=40, seconds=1)
        future = Question(pub_date=time)
        self.assertIs(future.check_recency(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):

    def test_with_no_question(self):
        response = self.client.get(reverse('poll:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_questions'], [])

    def test_with_future_question(self):
        create_question('future_question', days=30)
        response = self.client.get(reverse('poll:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_questions'], [])

    def test_with_past_questions(self):
        question = create_question('past_questions', days=-19)
        response = self.client.get(reverse('poll:index'))
        self.assertQuerySetEqual(response.context['latest_questions'], [question], )

    def test_with_future_question_and_past_questions(self):
        question = create_question('past_questions', days=-19)
        create_question('future_question', days=30)
        response = self.client.get(reverse('poll:index'))
        self.assertQuerySetEqual(response.context['latest_questions'], [question], )

    def test_with_two_past_questions(self):
        question1 = create_question('past_questions', days=-19)
        question2 = create_question('past_questions2', days=-17)
        response = self.client.get(reverse('poll:index'))
        self.assertQuerySetEqual(response.context['latest_questions'], [question2, question1], )


class QuestionDetailsViewTest(TestCase):
    def test_with_future_question_for_detail_view(self):
        future_question = create_question('future_question', days=30)
        url = reverse("poll:details", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_with_past_question_for_detail_view(self):
        past_question = create_question('past_questions2', days=-17)
        url = reverse("poll:details", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response,past_question.question_text)
