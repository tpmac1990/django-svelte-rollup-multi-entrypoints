from django.db.models import Max
from .models import UserFilms
from django_htmx.http import trigger_client_event
from render_block import render_block_to_string 
from django.shortcuts import render
from django.http.response import HttpResponse


def get_max_order(user) -> int:
    existing_films = UserFilms.objects.filter(user=user)
    if not existing_films.exists():
        return 1
    else:
        current_max = existing_films.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1

def reorder(user):
    existing_films = UserFilms.objects.filter(user=user)
    if not existing_films.exists():
        return
    number_of_films = existing_films.count()
    new_ordering = range(1, number_of_films+1)
    
    for order, user_film in zip(new_ordering, existing_films):
        user_film.order = order
        user_film.save()

def render_trigger_block(request, template, context, trigger=None, block=None):
    if block:
        html = render_block_to_string(template, block, context)
        response = HttpResponse(html)
    else:
        response = render(request, template, context)
    if trigger:
        # response['HX-Trigger'] = trigger
        trigger_client_event(response, trigger, {})
    return response
