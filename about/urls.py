from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^$', views.AboutView.as_view(), name='about'),
]
