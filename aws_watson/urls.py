from django.conf.urls import url
from aws_watson.views import test

urlpatterns = [
    url(r'^test/$', test, name='test'),
]
