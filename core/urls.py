from django.urls import path

from .views import index, ios

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('ios.html', ios),


]
