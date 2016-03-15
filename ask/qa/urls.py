from django.conf.urls import url

from qa import views

urlpatterns = [
    url(r'^$', views.get_index, name='index'),
    url(r'^login', views.test, name='login'),
    url(r'^signup', views.test, name='signup'),
    url(r'^ask', views.add_ask, name='ask'),
    url(r'^popular', views.get_popular, name='popular'),
    url(r'^new', views.test, name='new'),
    url(r'^question/(?P<id>\d+)/$', views.get_question, name='question'),
    url(r'^answer', views.add_answer, name='answer')
]