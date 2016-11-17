from django.conf.urls import url
from . import views
  # ^ So we can call functions from our routes!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^add$', views.add_course),
  url(r'^delete/(?P<id>\d+)$', views.delete_confirm),
  url(r'^deleteentry/(?P<id>\d+)$', views.delete)
]
