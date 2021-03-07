from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import listing, homeFeedView
from pages.views import aboutPageView
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, voteView)

class TestUrls(SimpleTestCase):

    def test_homefeed_url_is_resolved(self):
        url = reverse('homefeed')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homeFeedView)

    def test_aboutpage_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, aboutPageView)

    def test_newquestion_url_is_resolved(self):
        url = reverse('newquestion')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newView)

    def test_myanswersview_url_is_resolved(self):
        url = reverse('my-answers')
        print(resolve(url))
        self.assertEquals(resolve(url).func, myAnswersView)

    def test_myquestionsview_url_is_resolved(self):
        url = reverse('my-questions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, myQuestionsView)

    def test_questionview_url_is_resolved(self):
        url = reverse('questionview', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, questionView)

    def test_voteview_url_is_resolved(self):
        url = reverse('voteview', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, voteView)

    def test_answerview_url_is_resolved(self):
        url = reverse('answerview', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, answerView)