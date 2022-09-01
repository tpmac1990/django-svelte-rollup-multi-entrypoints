from django.shortcuts import render
from django.views import View
from .models import Question

def index(request):
    return render(request, 'polls/index.html')


class PollQuestions(View):
    title = "Questions"
    template = 'polls/questions.html'

    def get(self, request):
        questions = list(Question.objects.values('pk', 'question_text'))

        context = {
            'question_text': self.title,
            'props': questions,
        }

        return render(request, self.template, context)


class Others(View):
    title = "Other"
    template = 'polls/other.html'

    def get(self, request):
        questions = [{'pk': 1, 'question_text': "What's different?"}, {'pk': 2, 'question_text': 'question 10'}, {'pk': 3, 'question_text': 'question 20'}, {'pk': 4, 'question_text': 'question 30'}]

        context = {
            'props': {
                'questions': questions,
                'other': "other info"
            },
        }

        return render(request, self.template, context)
