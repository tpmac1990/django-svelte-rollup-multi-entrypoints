import math
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Film, UserFilms
from .utils import get_max_order, reorder, render_trigger_block
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class FilmList(LoginRequiredMixin, ListView):
    template_name = 'htmx_lookup/films.html'
    model = UserFilms
    paginate_by = settings.PAGINATE_BY
    context_object_name = 'films'

    def get_template_names(self):
        if self.request.htmx:
            return 'htmx_lookup/partials/film-list-elements.html'
        return 'htmx_lookup/films.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film_count'] = context['page_obj'].paginator.count
        return context

    def get_queryset(self):
        user_films = UserFilms.objects.prefetch_related('film').filter(user=self.request.user)
        return user_films


class FilmDetail(LoginRequiredMixin, DetailView):
    template_name = 'film.html'
    model = Film

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userfilm = UserFilms.objects.filter(user=self.request.user).filter(film=kwargs['object']).first()
        context = {'userfilm': userfilm}
        return context


@login_required
def add_film(request):
    name = request.POST.get('filmname')
    
    # add film
    film = Film.objects.get_or_create(name=name)[0]
    
    # add the film to the user's list
    if not UserFilms.objects.filter(film=film, user=request.user).exists():
        UserFilms.objects.create(
            film=film, 
            user=request.user, 
            order=get_max_order(request.user)
        )

    # return template fragment with all the user's films
    films = UserFilms.objects.filter(user=request.user)
    messages.success(request, f"Added {name} to list of films")
    return render_trigger_block(request, 'htmx_lookup/partials/film-list.html', {'films': films}, 'filmCount')


@require_http_methods(['DELETE'])
@login_required
def delete_film(request, pk):
    ...
    # remove the film from the user's list
    UserFilms.objects.get(pk=pk).delete()

    reorder(request.user)

    # return template fragment with all the user's films
    films = UserFilms.objects.filter(user=request.user)
    return render_trigger_block(request, 'htmx_lookup/partials/film-list.html', {'films': films}, "filmCount")


@login_required
def search_film(request):
    search_text = request.POST.get('search')

    # look up all films that contain the text
    # exclude user films
    userfilms = UserFilms.objects.filter(user=request.user)
    results = Film.objects.filter(name__icontains=search_text).exclude(
        name__in=userfilms.values_list('film__name', flat=True)
    )
    context = {"results": results}
    return render(request, 'htmx_lookup/partials/search-results.html', context)

def clear(request):
    return HttpResponse("")

def sort(request):
    film_pks_order = request.POST.getlist('film_order')
    films = []
    updated_films = []

    # fetch user's films in advance (rather than once per loop)
    userfilms = UserFilms.objects.prefetch_related('film').filter(user=request.user)

    for idx, film_pk in enumerate(film_pks_order, start=1):
        # find instance w/ the correct PK
        userfilm = next(u for u in userfilms if u.pk == int(film_pk))

        # add changed movies only to an updated_films list
        if userfilm.order != idx:
            userfilm.order = idx
            updated_films.append(userfilm)

        films.append(userfilm)
    
    # bulk_update changed UserFilms's 'order' field
    UserFilms.objects.bulk_update(updated_films, ['order'])

    paginator = Paginator(userfilms, settings.PAGINATE_BY)
    page_number = math.ceil(len(film_pks_order) / settings.PAGINATE_BY)
    page_obj = paginator.get_page(page_number)
    context = {'films': films, 'page_obj': page_obj}

    return render(request, 'htmx_lookup/partials/film-list.html', context)

@login_required
def detail(request, pk):
    userfilm = get_object_or_404(UserFilms, pk=pk)
    context = {'userfilm': userfilm}
    return render(request, 'htmx_lookup/partials/film-detail.html', context)

@login_required
def films_partial(request):
    films = UserFilms.objects.filter(user=request.user)
    return render(request, 'htmx_lookup/partials/film-list.html', {'films': films})

@login_required
def upload_photo(request, pk):
    userfilm = get_object_or_404(UserFilms, pk=pk)
    print(request.FILES)
    photo = request.FILES.get('photo')
    userfilm.film.photo.save(photo.name, photo)
    context = {'userfilm': userfilm}
    return render(request, 'htmx_lookup/partials/film-detail.html', context)


def film_count(request):
    context = {
        'film_count': UserFilms.objects.count()
    }
    return render_trigger_block(request, 'htmx_lookup/films.html', context, None, 'film-count')
