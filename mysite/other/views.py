from django.shortcuts import render
from django.views import View


class Others(View):
    title = "Other"
    template = 'other/other.html'

    def get(self, request):
        questions = [{'pk': 1, 'question_text': "What's different?"}, {'pk': 2, 'question_text': 'question 10'}, {'pk': 3, 'question_text': 'question 20'}, {'pk': 4, 'question_text': 'question 30'}]

        context = {
            'props': {
                'questions': questions,
                'other': "other info"
            },
        }

        return render(request, self.template, context)