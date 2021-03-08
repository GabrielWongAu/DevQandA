from selenium import webdriver
from main.models import Question, Answer
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.utils import timezone

import time
import os 

class TestAboutPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())

    def tearDown(self):
        self.browser.close()
    
    def test_no_answers_alert_is_displayed(self):
        self.browser.get('http://127.0.0.1:8000/about/')
        
        #The user requests the page for the first time
        alert = self.browser.find_element_by_class_name('pb-2')
        self.assertEquals(
            alert.find_element_by_tag_name('p').text,
            'Dev Q and A is an open-source Question and Answer forum for developers of all levels (aspiring developers, CS students, bootcamp students, self-learners, professional developers, etc).'
        )