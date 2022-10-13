from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.middleware import csrf
from django import forms
from .models import Hobby
import json
# from django_remote_forms.forms import RemoteForm


class SvelteDemos(View):
    template = 'svelte_demo/index.html'

    def get(self, request):
        context = {
            'props': {
                'csrfToken': csrf.get_token(request),
            },
        }
        return render(request, self.template, context)

def clubs(request):
    if request.method == 'GET':
        data = {
            'clubs': [
                {'id': 1, 'name': 'Storm'},
                {'id': 2, 'name': 'Broncos'},
                {'id': 3, 'name': 'Roosters'},
                {'id': 4, 'name': 'Panthers'},
            ]
        }
        return JsonResponse(data=data)



# class HobbyForm(forms.ModelForm):
#     class Meta:
#         model = Hobby
#         fields = '__all__'


def hobbies(request):
    if request.method == 'GET':
        # I need to use drf serializer in stead of a form
        pass
        # form = HobbyForm()
        # remote_form = RemoteForm(form)
        # return JsonResponse(data={'form': remote_form.as_dict()})

        # if I send values through, can I create a form like object on response in order to save it easily
        # perhaps drf is a better option. I can't remember how to save it
        # serializers.ModelSerializer: should be the way to go. use instead of ModelForm


