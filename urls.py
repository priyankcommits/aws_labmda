from django.conf.urls import url
from aws_watson.views import test

urlpatterns = [
    url(r'^api_crawler_agent_post/$', api_crawler_agent_post, name='api_crawler_agent_post'),
]
