from django.urls import path,include
from main.views import Portfolio, about, contact, details_blog, home,blog, services, skills
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',home),
path('about',about),
path('Portfolio',Portfolio),
path('article',blog,name="blog"),
path('skills',skills),
path('article/<slug:slug>',details_blog,name="article"),
path('contact',contact),
path('services',services),
]

# Ajoutez cette ligne pour servir les fichiers médias pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)