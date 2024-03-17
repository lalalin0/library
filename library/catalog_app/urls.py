from django.urls import path, re_path
from catalog_app.views import index


urlpatterns = [
    path('', index, name='index'),
]



