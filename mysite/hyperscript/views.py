from django.shortcuts import render
import time

def htmx_get(request):
    time.sleep(2)
    return render(request, 'hyperscript/partial.html', {})
