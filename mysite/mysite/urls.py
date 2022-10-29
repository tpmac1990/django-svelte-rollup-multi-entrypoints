"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration/', include('registration.urls')),
    path('polls/', include('polls.urls')),
    path('other/', include('other.urls')),
    path('sform/', include('sform.urls')),
    path('htmx-todo/', include('htmx_todo.urls')),
    path('htmx-lookup/', include('htmx_lookup.urls')),
    path('htmx-form/', include('htmx_form.urls')),
    path('htmx-fragments/', include('htmx_fragments.urls')),
    path('alpine/', include('alpine.urls')),
    path('hyperscript/', include('hyperscript.urls')),
    path('svelte-demo/', include('svelte_demo.urls')),
    path('svelte-leaflet/', include('svelte_leaflet.urls')),
    path('svelte-leaflet-2/', include('svelte_leaflet_2.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), # live-reload for django templates
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
