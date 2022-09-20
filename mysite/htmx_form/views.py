from django.http import HttpResponse
from django.shortcuts import render
from render_block import render_block_to_string

from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': BookForm()}
        else:
            context = {'form': form}
        html = render_block_to_string('htmx_form/index.html', 'add-book-form', context)
        response = HttpResponse(html)
        if form.is_valid():
            response['HX-Trigger'] = 'book_added'
        return response
    
    context = {
        'form': BookForm(),
        'books': Book.objects.all(),
    }
    return render(request, 'htmx_form/index.html', context)

def book_list(request):
    context = {'books': Book.objects.all()}
    html = render_block_to_string('htmx_form/index.html', 'book-list', context)
    return HttpResponse(html)
    