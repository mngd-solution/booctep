# from django.urls import path
from django.conf.urls import include, url, i18n
from video.views import *

urlpatterns = [
    url(r'^save_cache_str/$', saveCacheStr, name='save cache str'),
    url(r'^check_answer/$', checkAnswer),
]