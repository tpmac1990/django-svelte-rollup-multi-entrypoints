from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm


def item_list(request):
    items = [{'id': x, 'name': f'dummy value {x}'} for x in list('012345')]
    context = {
        'items': items
    }
    return render(request, 'htmx_fragments/partials/items_list.html', context)

def delete_item(request, id):
    # delete instance in database
    return HttpResponse("")



def form_page(request):
    context = {
        'first_name': 'john',
        'last_name': 'doe'
    }
    return render(request, 'htmx_fragments/form_templates/form_page.html', context)


def basic_form(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            context = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name']
            }
            return render(request, 'htmx_fragments/form_templates/table.html', context)
        else:
            HttpResponseForbidden()

    form = NameForm()

    return render(request, 'htmx_fragments/form_templates/form.html', {'form': form})