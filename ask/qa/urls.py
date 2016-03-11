from django.conf.urls import url, include

from qa import views

urlpatterns = [
    url(r'^$', views.get_index),
    url(r'^login', views.test),
    url(r'^signup', views.test),
    url(r'^ask', views.test),
    url(r'^get_popular', views.get_popular),
    url(r'^new', views.test),
    url(r'^question/(&P<id>\d+)/$', views.get_question),
]