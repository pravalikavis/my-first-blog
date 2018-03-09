from django.test import TestCase

# Create your tests here.
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
