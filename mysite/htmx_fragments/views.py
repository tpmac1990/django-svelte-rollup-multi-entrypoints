from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from .forms import NameForm, ImageForm
from .models import Image
from render_block import render_block_to_string


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


def img_app(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        else:
            HttpResponseForbidden()

    context = {
        "images": Image.objects.all(),
        "form": ImageForm()
    }

    return render(request, 'htmx_fragments/partials/images.html', context)


def img_app_prev(request, pk):
    img = Image.objects.filter(id__lt=pk).order_by('id').last()
    return render(request, 'htmx_fragments/partials/image_large.html', {'img': img})
    # html = render_block_to_string('htmx_fragments/partials/images.html', 'lg-img', {'img': img})
    # return HttpResponse(html)


def img_app_next(request, pk):
    img = Image.objects.filter(id__gt=pk).order_by('id').first()
    return render(request, 'htmx_fragments/partials/image_large.html', {'img': img})
    # html = render_block_to_string('htmx_fragments/partials/images.html', 'lg-img', {'img': img})
    # return HttpResponse(html)