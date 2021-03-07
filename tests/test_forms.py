from django.test import SimpleTestCase
from main.models import QuestionForm

class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = QuestionForm(data={
            'title': 'This is an example question title',
            'body': 'This is an example question body'
        })

        self.assertTrue(form.is_valid())

    
    def test_expense_form_no_data(self):
        form = QuestionForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)