from selenium import webdriver
from main.models import Question, Answer
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

import time
import os 

User = get_user_model()

class TestSignUpPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())

    def tearDown(self):
        self.browser.close()

    def test_signup_to_ask_question_button(self):
        self.browser.get('http://127.0.0.1:8000/')

        add_url = 'http://127.0.0.1:8000' + reverse('account_signup')

        self.browser.find_element_by_link_text('Sign Up to Ask Question').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

