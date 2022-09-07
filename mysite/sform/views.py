from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.middleware import csrf
from django.views.decorators.http import require_GET


class Sform(View):
    template = 'sform/sform.html'

    def get(self, request):
        context = {
            'props': {
                'csrfToken': csrf.get_token(request),
            },
        }

        return render(request, self.template, context)

@require_GET
def todo(request):
    return JsonResponse(data={'success': True, 'html': "hello"})
