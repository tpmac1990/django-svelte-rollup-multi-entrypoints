from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.middleware import csrf
from django import forms
from .models import Hobby
from .utils import JsonModelForm
from django.shortcuts import get_object_or_404


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



class HobbyForm(JsonModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'


def hobbies(request, pk=None):
    if request.method == 'GET':
        if pk:
            # pass initial values of an instance
            hobby = get_object_or_404(Hobby, pk=pk)
            form = HobbyForm(instance=hobby).to_dict()
        else:
            form = HobbyForm().to_dict()
        hobbies = list(Hobby.objects.all().values())
        return JsonResponse({'form': form, 'hobbies': hobbies})

    elif request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
            hobbies = list(Hobby.objects.all().values())
            return JsonResponse({'msg': 'Successfully saved', 'hobbies': hobbies})
        return JsonResponse({'msg': 'Error'})

    elif request.method == 'DELETE':
        hobby = get_object_or_404(Hobby, pk=pk)
        hobby.delete()
        return JsonResponse({'msg': 'Successfully deleted'})

