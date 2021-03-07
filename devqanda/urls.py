from django.contrib import admin
from django.urls import path, include
from main.views import homeFeedView, testView
from pages.views import aboutPageView
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, voteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeFeedView, name='homefeed'),
    path('test/', testView),
    path('about/', aboutPageView, name='about'),
    path('accounts/', include('allauth.urls')),
    path('question/<int:id>/', questionView, name='questionview'),
    path('question/<int:id>/vote', voteView, name='voteview'),
    path('question/<int:id>/answer', answerView, name='answerview'),
    path('question/new/', newView, name='newquestion'),
    path('question/my_answers/', myAnswersView, name='my-answers'),
    path('question/my_questions/', myQuestionsView, name='my-questions'),
]
