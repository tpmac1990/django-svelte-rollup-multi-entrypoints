from django.shortcuts import render
from .models import Film
from .serializers import FilmSerializer
from rest_framework.generics import ListAPIView
from taggit.models import Tag


def alpine_index(request):
    context = {
        'tags': Tag.objects.all()
    }
    return render(request, 'alpine/index.html', context)

class FilmListAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

